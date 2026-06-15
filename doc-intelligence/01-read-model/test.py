from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest


endpoint = ""
key = ""

document_url = "https://viststracc1ai15jun2026.blob.core.windows.net/docuements/Chapter2.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-read", AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}: {para.content}")   