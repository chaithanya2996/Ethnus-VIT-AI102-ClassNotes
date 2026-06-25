from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://language4000.cognitiveservices.azure.com/"
key=""

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "The restaurant had amazing food and the staff were incredibly friendly. I can’t wait to go back!",
    "The product arrived broken and customer service was unhelpful when I tried to get a replacement.",
    "The report produced around 1000 data points."
]

response=client.analyze_sentiment(documents=documents)

for result in response:
    print(f"Sentiment: {result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}")
    