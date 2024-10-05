import os
from google.cloud import storage

def set_google_application_credentials(json_key_path):
    """Sets the environment variable for Google Application Credentials."""
    if not os.path.exists(json_key_path):
        raise FileNotFoundError(f"Service account key file '{json_key_path}' not found.")
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_path
    print(f"Google application credentials set to: {json_key_path}")

def create_bucket_and_folders(bucket_name, folders):
    """Creates a GCS bucket and multiple folders."""
    try:
        # Initialize a GCS client
        storage_client = storage.Client()  # Will use the credentials set in the environment variable
    except Exception as e:
        print(f"Error initializing GCS client: {e}")
        return

    # Create the bucket
    try:
        bucket = storage_client.create_bucket(bucket_name)  # Creates the bucket
        print(f"Bucket '{bucket.name}' created.")
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return

    # Create folders
    for folder in folders:
        blob = bucket.blob(f"{folder}/")  # Append a slash to create a "folder"
        try:
            blob.upload_from_string('')  # Upload an empty string to create the folder
            print(f"Folder '{folder}' created in bucket '{bucket.name}'.")
        except Exception as e:
            print(f"Error creating folder '{folder}': {e}")

if __name__ == "__main__":
    try:
        # Set the path to your service account key JSON
        json_key_path = r"C:\serviceaccounts\krishnaproject-435718-48fcd5fe61a3.json"
        set_google_application_credentials(json_key_path)

        # Configuration
        bucket_name = "p2projectkc"  # Replace with your desired bucket name
        folders_to_create = ["raw_folder", "cleaned_folder"]

        # Create the bucket and folders
        create_bucket_and_folders(bucket_name, folders_to_create)

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
