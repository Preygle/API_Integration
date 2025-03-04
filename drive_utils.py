import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from io import BytesIO

# Load credentials
SERVICE_ACCOUNT_FILE = "service_account.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=credentials)

# Your shared Google Drive folder ID
FOLDER_ID = "drive_folder_id"


def upload_note(note_content, note_title):
    try:
        file_metadata = {
            "name": f"{note_title}.txt",
            "parents": [FOLDER_ID]
        }
        media = MediaFileUpload(io.BytesIO(
            note_content.encode()), mimetype="text/plain")
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()
        return file.get("id")
    except Exception as e:
        print(f"An error occurred during upload: {e}")
        return None



    media = MediaIoBaseUpload(io.BytesIO(
        note_content.encode()), mimetype="text/plain")

        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()
        return file.get("id")
    except Exception as e:
        print(f"An error occurred during upload: {e}")
        return None


    return file.get("id")

def list_notes():
    try:
        query = f"'{FOLDER_ID}' in parents and mimeType='text/plain'"
        results = drive_service.files().list(q=query, fields="files(id, name)").execute()
        return results.get("files", [])
    except Exception as e:
        print(f"An error occurred while listing notes: {e}")
        return []

    except Exception as e:
        print(f"An error occurred while listing notes: {e}")
        return []


def get_note_content(file_id):
    try:
        request = drive_service.files().get_media(fileId=file_id)
        content = BytesIO()
        downloader = MediaIoBaseDownload(content, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        return content.getvalue().decode("utf-8")
    except Exception as e:
        print(f"An error occurred while retrieving the note content: {e}")
        return None

    except Exception as e:
        print(f"An error occurred while retrieving the note content: {e}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
