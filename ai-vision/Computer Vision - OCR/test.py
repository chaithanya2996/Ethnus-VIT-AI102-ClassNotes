from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json

endpoint = ""
key =""

client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

with open("quote.png", "rb") as image_file:
    image_details = image_file.read()

response = client.analyze(
    image_data=image_details, 
    visual_features=[VisualFeatures.READ],)


# print(json.dumps(response.as_dict(), indent=4))
for line in response.read.blocks[0].lines:
    print(f"{line.text}")