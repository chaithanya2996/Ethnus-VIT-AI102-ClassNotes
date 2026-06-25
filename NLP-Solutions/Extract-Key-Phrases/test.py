from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://language4000.cognitiveservices.azure.com/"
key=""

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Machine learning and artificial intelligence are transforming industries such as healthcare, "
    "finance, and education by automating tasks and providing insights"
]

response=client.extract_key_phrases(documents=documents)[0]

for key_phrase in response.key_phrases:
    print(key_phrase)