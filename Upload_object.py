from google.cloud import storage

# Setting credentials using the downloaded JSON file

client = storage.Client.from_service_account_json(json_credentials_path='C:\Terraform\dev-sa.json')



bucket = client.bucket("dcmbucket")

# Name of the object to be stored in the bucket

object_name_in_gcs_bucket = bucket.blob('my_first_gcs_upload.txt')

# Name of the object in local file system

object_name_in_gcs_bucket.upload_from_filename('C:/Terraform/testblob.txt')

blobs = client.list_blobs("dcmbucket")
for blob in blobs:
    #if str(blob) == "my_first_gcs_upload.txt":
        print(blob)
