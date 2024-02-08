from llama_index import download_loader

S3Reader = download_loader("S3Reader")
loader = S3Reader(
    bucket='<BUCKET_NAME>', 
    key='<FILE_NAME>', 
    aws_access_id='[ACCESS_KEY_ID]', 
    aws_access_secret='[ACCESS_KEY_SECRET]'
)
documents = loader.load_data()
