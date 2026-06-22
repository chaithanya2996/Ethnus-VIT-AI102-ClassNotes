targetScope = 'resourceGroup'

@description('Development Environment')
@allowed(['dev','stage','prod'])
param environment string = 'dev'

@description('Azure Region')
param location string = resourceGroup().location

var prefix = 'vitai${environment}'
var storageName = '${prefix}22june2026'

// storage account creation

resource docStorage 'Microsoft.Storage/storageAccounts@2026-04-01' = {
  name: storageName
  location: location
  sku: { name: 'Standard_LRS'}
  kind: 'StorageV2'
  properties: {
    allowBlobPublicAccess: false
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
  }
}

resource blobContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2026-04-01' = {
  name: '${docStorage.name}/default/ai-documents'
  properties: {publicAccess:'None'}
}

output storageId string = docStorage.id

