import os
from google.cloud import storage

def upload_file_to_folder(bucket_name, source_file_name, folder_name, destination_blob_name):
    """Uploads a file to a specific folder in the GCS bucket."""
    try:
        # Initialize a GCS client
        storage_client = storage.Client(project='krishnaproject-435718')


        # Get the bucket
        bucket = storage_client.bucket(bucket_name)

        # Append the folder name to the destination blob name
        destination_path = f"{folder_name}/{destination_blob_name}"

        # Get the blob (file in the folder)
        blob = bucket.blob(destination_path)

        # Upload the file to the folder in the bucket
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {bucket_name}/{destination_path} successfully uploaded.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    try:
        # Configuration
        bucket_name = "p2projectkc"  # Replace with your desired bucket name
        source_file_name = r"C:\Users\krishna chaithanya\OneDrive\Desktop\Rev_Project2\GCS\uploading files to gcs\ecommerce_raw_data.csv" # Replace with the file path you want to upload
        folder_name = "raw_folder"  # Folder in the GCS bucket
        destination_blob_name = "ecommerce_raw_data.csv"  # The desired file name in the bucket

        # Upload the file to the folder in the bucket
        upload_file_to_folder(bucket_name, source_file_name, folder_name, destination_blob_name)

        # Configuration
        bucket_name = "p2projectkc"  # Replace with your desired bucket name
        source_file_name = r"C:\Users\krishna chaithanya\OneDrive\Desktop\Rev_Project2\GCS\uploading files to gcs\ecommerce_cleansed_data.csv" # Replace with the file path you want to upload
        folder_name = "cleaned_folder"  # Folder in the GCS bucket
        destination_blob_name = "ecommerce_cleansed_data.csv"  # The desired file name in the bucket

        # Upload the file to the folder in the bucket
        upload_file_to_folder(bucket_name, source_file_name, folder_name, destination_blob_name)

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
