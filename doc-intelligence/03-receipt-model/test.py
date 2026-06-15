from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

endpoint = ""
key = ""

document_url = "https://viststracc1ai15jun2026.blob.core.windows.net/docuements/Sample Receipt.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-receipt", AnalyzeDocumentRequest(url_source=document_url))

result = response.result()

for index,receipt in enumerate(result.documents):
    print(f"Merchant Name: {receipt.fields.get('MerchantName').get('valueString')}")
    print(f"Transaction Date: {receipt.fields.get('TransactionDate').get('valueDate')}")
    print(f"Total Amount: {receipt.fields.get('Total').get("content")}")