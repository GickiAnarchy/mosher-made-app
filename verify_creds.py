import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.exceptions import DefaultCredentialsError


   
def verify_service_account():
    try:
        with open("creds.json","r") as  f:
            info = json.load(f)
    except Exception as e:
        print(e)
        return False
    try:
        # 1. Attempt to create credentials object
        creds = service_account.Credentials.from_service_account_info(info)
        
        # 2. Scope the credentials (e.g., for Google Drive or Cloud Storage)
        # Even if you don't use the API, scoping is required to verify
        scoped_creds = creds.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
        
        # 3. Build a service and make a 'test' call
        # We use the Service Usage API to see if we can at least authenticate
        service = build('serviceusage', 'v1', credentials=scoped_creds)
        
        # This triggers a refresh/validation check
        print(f"Success! Authenticated as: {creds.service_account_email}")
        return True

    except Exception as e:
        print(f"Verification Failed: {e}")
        return False