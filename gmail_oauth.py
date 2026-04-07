from google_auth_oauthlib.flow import InstalledAppFlow
import os

# Where your client JSON is
CLIENT_SECRETS_FILE = os.path.expanduser("~/.openclaw/identity/googleproject.json")

# Where the token will be saved
TOKEN_FILE = os.path.expanduser("~/.openclaw/identity/google-token.json")

# Gmail scopes
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    SCOPES
)

# IMPORTANT: match what you added in Google Cloud
creds = flow.run_local_server(
    host="localhost",
    port=8765,
    open_browser=False
)

# Save token
with open(TOKEN_FILE, "w") as token:
    token.write(creds.to_json())

print("\n✅ OAuth complete. Token saved to:")
print(TOKEN_FILE)
