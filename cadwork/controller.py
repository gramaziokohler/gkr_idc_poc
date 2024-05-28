from compas.data import json_load, json_dump
from compas.geometry import Line, Plane

from compas_timber.connections import LMiterJoint
from compas_timber.connections import TButtJoint
from compas_timber.connections import LButtJoint
from compas_timber.elements import DrillFeature
from compas_timber.elements import CutFeature

from compas_cadwork.utilities.events import ElementDelta
from compas_cadwork.utilities import remove_elements
from compas_cadwork.utilities import get_all_element_ids
from compas_cadwork.conversions import point_to_cadwork
from compas_cadwork.conversions import vector_to_cadwork

import cadwork
from attribute_controller import set_name
from attribute_controller import is_connector_axis
from element_controller import create_rectangular_beam_vectors
from element_controller import cut_elements_with_miter
from element_controller import cut_corner_lap
from element_controller import cut_t_lap
from element_controller import cut_element_with_plane
from element_controller import create_rectangular_panel_vectors

from cwmath.cwplane3d import CwPlane3d
from cwmath.cwvector3d import CwVector3d


def _apply_l_miter(beam_a, beam_b):
    id_a, id_b = beam_a.attributes["cadwork_id"], beam_b.attributes["cadwork_id"]
    cut_elements_with_miter(id_a, id_b)


def _extend_l_butt(beam_a, beam_b):
    id_a, id_b = beam_a.attributes["cadwork_id"], beam_b.attributes["cadwork_id"]
    cut_corner_lap([id_a, id_b], 0, 0,0, 0, 0, 0, 0)  # this extends

    
def _extend_t_butt(beam_a, beam_b):
    id_a, id_b = beam_a.attributes["cadwork_id"], beam_b.attributes["cadwork_id"]
    cut_t_lap([id_a, id_b], 0, 0,0, 0, 0, 0, 0)


def apply_cuts(beam):
    for f in filter(lambda x: isinstance(x, CutFeature), beam.features):
        print(f"applying cut owner: {f.owner}")
        if f.owner and f.owner == LMiterJoint.__name__:
            continue
        plane_normal = CwVector3d(*f.cutting_plane.normal)
        plane = CwPlane3d(CwVector3d(*f.cutting_plane.point),plane_normal)
        distance = plane.distance_to_point(CwVector3d(0.0, 0.0, 0.0))
        if plane_normal.z < 0 or plane_normal.x < 0 or plane_normal.y < 0:
            distance = -distance  # geil!
        cut_element_with_plane(beam.attributes["cadwork_id"], cadwork.point_3d(*plane_normal), distance)


def point_from_corner_to_face_center(frame, ysize, zsize):
    origin = frame.point
    yaxis = frame.yaxis
    zaxis = frame.normal
    yaxis = yaxis * ysize * 0.5
    zaxis = zaxis * zsize * 0.5
    return origin + yaxis + zaxis


class Controller:

    def __init__(self):
        # TODO: iterate on building groups, make model from each
        self.model = None
        self._delta = ElementDelta()

    def load_model_from_file(self, file_path):
        self.clear_model()
        model = json_load(file_path)
        self.create_walls(model)
        self.create_beams(model)
        self.create_connections(model)
        self.model = model
        self._delta.reset()
        return model        
    
    def clear_model(self):
        remove_elements(list(get_all_element_ids()))

    def export_model_to_file(self, file_path):
        new_elements, removed_elements = self._delta.check_for_changed_elements()
        if new_elements:
            self.handle_new_elements(new_elements)
        if removed_elements:
            self.handle_removed_elements(removed_elements)
        json_dump(self.model, file_path)
    
    def handle_new_elements(self, new_elements):
        print(f"new elements:{new_elements}")
        for element in new_elements:
            if element.is_drilling:
                drilled_elements = element.get_elements_in_contact()
                self.add_drilling(element, drilled_elements)
    
    def add_drilling(self, e_drill, e_beams):
        for e_b in e_beams:
            beam = self.model.element_map[e_b.id]
            drill_line = Line.from_point_direction_length(e_drill.frame.point, e_drill.frame.xaxis, e_drill.length)
            beam.add_features(
                [DrillFeature(drill_line, diameter=e_drill.width, length=e_drill.length, is_joinery=False)]
            )

    @staticmethod
    def create_beams(model):
        model.element_map = {}
        for beam in model.beams:
            origin = cadwork.point_3d(*beam.frame.point)
            xaxis = cadwork.point_3d(*beam.frame.xaxis)
            zaxis = cadwork.point_3d(*beam.frame.normal)
            element_id = create_rectangular_beam_vectors(beam.width, beam.height, beam.length, origin, xaxis, zaxis)
            beam.attributes["cadwork_id"] = element_id
            beam.attributes["name"] = f"beam_{beam.key}"
            model.element_map[element_id] = beam
            set_name([element_id], beam.attributes["name"])

    @staticmethod
    def create_walls(model):
        for wall in model.walls:
            origin = point_from_corner_to_face_center(wall.frame, wall.width, wall.height) 
            origin = point_to_cadwork(origin)
            xaxis = vector_to_cadwork(wall.frame.xaxis)
            zaxis = vector_to_cadwork(wall.frame.normal)
            element_id = create_rectangular_panel_vectors(wall.width, wall.height, wall.length, origin, xaxis, zaxis)
            set_name([element_id], wall.name)

    
    @staticmethod
    def create_connections(model):
        joint_map = {
            LMiterJoint: _apply_l_miter,
            TButtJoint: _extend_t_butt,
            LButtJoint: _extend_l_butt
        }
        for joint in model.joints:
            beam_a, beam_b = joint.beams
            applier = joint_map[type(joint)]
            applier(beam_a, beam_b)
        for beam in model.beams:
            apply_cuts(beam)
