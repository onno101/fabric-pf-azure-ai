from promptflow import tool
import requests
import json
import pprint
import msal
from promptflow.connections import CustomConnection





@tool
def my_python_tool(input1: str, conn:CustomConnection) -> str:
    
    # Your Azure Active Directory tenant ID
    TENANT_ID = conn.tenant_id
    # Your Azure AD registered application's client ID
    CLIENT_ID = conn.client_id

    # The UPN and password of the user
    USERNAME = conn.username
    PASSWORD = conn.password
    
    # The authority URL
    AUTHORITY_URL = f'https://login.microsoftonline.com/{TENANT_ID}'
    # The scope for the token
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # Create a public client application
    app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY_URL, client_credential=None)
    
    # Acquire token by username and password
    result = app.acquire_token_by_username_password(USERNAME, PASSWORD, scopes=SCOPE)

    # Check if the token was acquired successfully
    access_token = result['access_token']
    
    url = conn.ai_skill_url

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    
    question = "{\"UserQuestion\": \""+ input1 + "\"}"

    response = requests.post(url, headers=headers, data = question)

    response = json.loads(response.content)

    
    return response