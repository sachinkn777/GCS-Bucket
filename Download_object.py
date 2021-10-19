from google.cloud import storage
# Setting credentials using the downloaded JSON file
client = storage.Client.from_service_account_json(json_credentials_path='C:\Terraform\dev-sa.json')

bucket = client.bucket("dcmbucket")

blob = bucket.blob("sample.dcm")
blob.download_to_filename("C:/Terraform/first_download_file.dcm")