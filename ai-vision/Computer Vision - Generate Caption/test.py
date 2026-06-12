from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json

endpoint = ""
key =""

client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

with open("street.jpg", "rb") as image_file:
    image_details = image_file.read()

response = client.analyze(
    image_data=image_details, 
    visual_features=[VisualFeatures.TAGS, VisualFeatures.CAPTION],)


print(json.dumps(response.as_dict(), indent=4))