from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

endpoint = ""
key = ""

document_url = "https://viststracc1ai15jun2026.blob.core.windows.net/docuements/invoice_2.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-invoice", AnalyzeDocumentRequest(url_source=document_url))

result = response.result()

for index,invoice in enumerate(result.documents):
    print(f"Customer Name: {invoice.fields.get('CustomerName').get('valueString')}")
    print(f"Invoice ID: {invoice.fields.get('InvoiceId').get('valueString')}")
    print(f"Total Amount: {invoice.fields.get('InvoiceTotal').get('valueNumber')}")