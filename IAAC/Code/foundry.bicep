@description('AI Foundry resource name')
param foundryName string

@description('Deployment location')
param location string = resourceGroup().location

resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: foundryName
  location: location
  kind: 'AIServices'

  sku: {
    name: 'S0'
  }

  identity: {
    type: 'SystemAssigned'
  }

  properties: {
    allowProjectManagement: true
    customSubDomainName: foundryName
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: false
    dynamicThrottlingEnabled: false
    restrictOutboundNetworkAccess: false
  }
}

output foundryId string = foundry.id
output endpoint string = foundry.properties.endpoint
