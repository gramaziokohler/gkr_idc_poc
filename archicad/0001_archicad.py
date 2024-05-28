import os

from compas.geometry import Box
from compas.data import json_dump
from compas_viewer.viewer import Viewer
from compas_timber.elements import Wall
from compas_timber.model import TimberModel

from archicad import ACConnection


def create_viewer():
    # draw inflated centerlines
    viewer = Viewer()
    viewer.renderer.camera.far = 1000000.0
    viewer.renderer.camera.position = [10000.0, 10000.0, 10000.0]
    viewer.renderer.camera.pan_delta = 5.0
    viewer.renderer.rendermode = "ghosted"
    return viewer

conn = ACConnection.connect()

cmds = conn.commands
utils = conn.utilities
types = conn.types

# get elemetns from Archicad
elements = cmds.GetAllElements()

# create bounding boxes from them (how otherwise to get the location/orientation?)
e_bboxes = cmds.Get3DBoundingBoxes(elements)

boxes = []
for e_bbox in e_bboxes:
    min_max = e_bbox.boundingBox3D
    box = Box.from_diagonal(
        [
            [min_max.xMin * 1000.0, min_max.yMin * 1000.0, min_max.zMin * 1000.0],
            [min_max.xMax * 1000.0, min_max.yMax * 1000.0, min_max.zMax * 1000.0]
        ]
    )
    boxes.append(box)

# create Walls from each element
walls = []
for index, box in enumerate(boxes):
    wall = Wall.from_box(box)
    wall.name = f"Wall0{index}"
    walls.append(wall)

# add elements to model
model = TimberModel()

for wall in walls:
    model.add_wall(wall)

# show model
viewer = create_viewer()
for wall in model.walls:
    viewer.scene.add(wall.geometry)

viewer.show()

# save to file
PATH = os.path.join(os.path.dirname(__file__), "model.json")
json_dump(model, PATH)