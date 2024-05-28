import os

from compas.data import json_load
from compas_viewer.viewer import Viewer


def create_viewer():
    # draw inflated centerlines
    viewer = Viewer()
    viewer.renderer.camera.far = 1000000.0
    viewer.renderer.camera.position = [10000.0, 10000.0, 10000.0]
    viewer.renderer.camera.pan_delta = 5.0
    viewer.renderer.rendermode = "ghosted"
    return viewer

# add elements to model
# load to file
PATH = os.path.join(os.path.dirname(__file__), "model_w_beams.json")
model = json_load(PATH)

# show model
viewer = create_viewer()
for wall in model.walls:
    viewer.scene.add(wall.geometry)
    
for beam in model.beams:
    viewer.scene.add(beam.geometry)

viewer.show()
