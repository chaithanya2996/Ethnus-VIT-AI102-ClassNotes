from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *
import json

endpoint = ""
key = ""

client = FaceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

feature_to_client = [
    FaceAttributeTypeDetection01.HEAD_POSE,
    # FaceAttributeTypeDetection01.AGE,
    FaceAttributeTypeDetection01.OCCLUSION,
    FaceAttributeTypeDetection01.ACCESSORIES
]

with open("satya.jpg", mode="rb") as image_data:
    response = client.detect(
        image_content=image_data.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=False,
        return_face_attributes=feature_to_client
    )

# print(json.dumps(response, indent=4, default=str))
print(json.dumps(response[0].as_dict(), indent=4 ))