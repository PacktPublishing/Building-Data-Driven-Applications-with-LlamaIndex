from llama_index.readers.s3 import S3Reader

loader = S3Reader(
    bucket='<BUCKET_NAME>', 
    key='<FILE_NAME>', 
    aws_access_id='[ACCESS_KEY_ID]', 
    aws_access_secret='[ACCESS_KEY_SECRET]'
)
documents = loader.load_data()
print(documents)


