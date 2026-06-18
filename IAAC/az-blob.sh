# ============================================
# Azure Storage Account Practical using Azure CLI
# ============================================

# Variables
RG="vit-ai-storage-rg"
LOCATION="eastus"
STORAGE="vitstorage$(date +%s)"
CONTAINER="vitcontainer"

# Create Resource Group
az group create \
    --name $RG \
    --location $LOCATION

# Create Storage Account
az storage account create \
    --name $STORAGE \
    --resource-group $RG \
    --location $LOCATION \
    --sku Standard_LRS \
    --kind StorageV2

# Get Storage Account Key
ACCOUNT_KEY=$(az storage account keys list \
    --resource-group $RG \
    --account-name $STORAGE \
    --query "[0].value" \
    --output tsv)

# Create Blob Container
az storage container create \
    --name $CONTAINER \
    --account-name $STORAGE \
    --account-key $ACCOUNT_KEY

# Create Sample Files
echo "Welcome to Azure Storage Practical using Azure CLI" > sample1.txt
echo "This file is uploaded to Azure Blob Storage" > sample2.txt

# Upload First File
az storage blob upload \
    --account-name $STORAGE \
    --account-key $ACCOUNT_KEY \
    --container-name $CONTAINER \
    --name sample1.txt \
    --file sample1.txt

# Upload Second File
az storage blob upload \
    --account-name $STORAGE \
    --account-key $ACCOUNT_KEY \
    --container-name $CONTAINER \
    --name sample2.txt \
    --file sample2.txt

# List Uploaded Blobs
az storage blob list \
    --account-name $STORAGE \
    --account-key $ACCOUNT_KEY \
    --container-name $CONTAINER \
    --output table

# Display Storage Account Name
echo "Storage Account Created: $STORAGE"