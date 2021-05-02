import boto3
def delete_from_s3(bucket, model, aws_secret, aws_key):
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=aws_key, aws_secret_access_key=aws_secret
        )
        s3.delete_object(Bucket=bucket, Key=model)
        return True
    except Exception as ex:
        print(str(ex))
        return False