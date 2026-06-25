from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint=""
key=""

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Me gusta aprender nuevos idiomas.",
    "Comment allez-vous ce matin ?"
]

response=client.detect_language(documents=documents)

print(response)