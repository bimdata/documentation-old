=====================================
# Authentication by client_credential
=====================================


---
[block:callout]
{
  "type": "warning",
  "title": "Pre-requisite: having created an application",
  "body": "Look [at the procedure to create an application](https://documentation.bimdata.io/v1.0/docs/create-your-application), then come back here.\nAfter the application is created, you can retrieve it on the BIMData.io account manager, in the \"Manage your application\" screen."
}
[/block]

[block:api-header]
{
  "title": "Get your access token"
}
[/block]
The Client ID and the Client Secret are the 2 elements that you need to get the Access Token of your application from the Authentication Server. You will need this Access Token for every call of the bimdata's API.


[block:code]
{
  "codes": [
    {
      "code": "import requests\npayload = {\n    \"client_id\": CLIENT_ID,\n    \"client_secret\": CLIENT_SECRET,\n    \"grant_type\": \"client_credentials\",\n}\n    \n# Get the token\nresponse = requests.post(\"https://login-staging.bimdata.io/token\", data=payload)\naccess_token = response.json().get(\"access_token\")",
      "language": "python"
    }
  ]
}
[/block]
