from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import json

resource_endpoint="https://language200023.cognitiveservices.azure.com/"
resource_key=""

resource_credential = AzureKeyCredential(resource_key)
client = TextAnalyticsClient(
            endpoint=resource_endpoint, 
            credential=resource_credential)

documents=["Satya Nadella announced at Microsoft’s headquarters in Redmond that the company’s revenue for the fourth quarter was $46 billion."]

response = client.recognize_entities(documents = documents)[0]

for entity in response.entities:
    print(f"Entity Text: {entity.text} - Entity Category: {entity.category}")