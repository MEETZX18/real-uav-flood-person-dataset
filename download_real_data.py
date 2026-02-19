!pip install roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="nQthic6XObCx429GuIpG")
project = rf.workspace("meet-utouk").project("final_people_detection_in_flood-wyxzo")
version = project.version(1)
dataset = version.download("yolov11")
                