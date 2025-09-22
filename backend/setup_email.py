#!/usr/bin/env python3
"""
Email Setup Script for TraceQ
This script helps configure Gmail API credentials for email functionality.
"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def setup_email_credentials():
    """Setup Gmail API credentials"""
    
    # Your Google OAuth credentials - Replace with your actual credentials
    # Get these from: https://console.cloud.google.com/
    credentials_info = {
        "web": {
            "client_id": "YOUR_GOOGLE_CLIENT_ID_HERE",
            "project_id": "YOUR_PROJECT_ID_HERE",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_GOOGLE_CLIENT_SECRET_HERE",
            "redirect_uris": [
                "http://localhost:8000/",
                "http://localhost:8080",
                "http://localhost:8080/",
                "http://localhost:8082/",
                "http://localhost:3000/"
            ],
            "javascript_origins": [
                "http://localhost:3000",
                "http://localhost:8000",
                "http://localhost:8001",
                "http://localhost:8002",
                "http://localhost:8003",
                "http://localhost:8004",
                "http://localhost:8005",
                "http://localhost:8080",
                "http://localhost:8082"
            ]
        }
    }
    
    # Save credentials to file
    with open('credentials.json', 'w') as f:
        json.dump(credentials_info, f, indent=2)
    
    print("✅ Credentials file created: credentials.json")
    print("⚠️  Please replace YOUR_GOOGLE_CLIENT_ID_HERE and YOUR_GOOGLE_CLIENT_SECRET_HERE with actual values")
    
    # Authenticate and get token
    creds = None
    token_path = 'token.json'
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ credentials.json not found. Please create it first with your actual OAuth credentials.")
                return
            
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8082)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    print("✅ Gmail API authentication successful")
    print("✅ Token saved to: token.json")

if __name__ == "__main__":
    print("🔧 Setting up Gmail API credentials for TraceQ...")
    print()
    print("Before running this script, make sure you have:")
    print("1. Created a project in Google Cloud Console")
    print("2. Enabled the Gmail API")
    print("3. Created OAuth 2.0 credentials")
    print("4. Updated the client_id and client_secret in this script")
    print()
    
    setup_email_credentials()