import boto3
def dl(bucket, key, model_path, aws_secret, aws_key):
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=aws_key, aws_secret_access_key=aws_secret
        )
        s3.download_file(bucket,key,model_path)
    except Exception as ex:
        print(str(ex))
        return False
    return True