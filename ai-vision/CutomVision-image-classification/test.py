from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

endpoint = ""
key = ""

credentials = ApiKeyCredentials(in_headers={"Prediction-key": key})
prediction_client = CustomVisionPredictionClient(endpoint=endpoint, credentials=credentials)

image_data = open("fruits.png", mode="rb").read()
project_id = ""
model_name = "FruitModel"

response = prediction_client.classify_image(
    project_id,
    model_name,
    image_data
)

for prediction in response.predictions:
    print(prediction)