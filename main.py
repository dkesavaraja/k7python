from s3file.s3upload import *
from s3file.s3download import *
from s3file.s3delete import *
from s3file.config import *


#s3 upload function
if __name__ == "__main__":
    upload(BUCKET,AWS_BUCKET_KEY,AWS_BUCKET_SECRET_KEY,'1595430043.png','1595430043.png',REGION,'public-read')
    print ("File Upload Successfully");
# bucketname, aws_key, aws_secret, source_path, keyname, region=None,acl='private', headers={}, guess_mimetype=True, parallel_processes=4

#s3 download function
dl(BUCKET,'1595430043.png','1595430043.png',AWS_BUCKET_SECRET_KEY,AWS_BUCKET_KEY);
print ("File Downloaded Successfully");
#bucket, key, model_path, aws_secret, aws_key


#s3 delete file function
delete_from_s3(BUCKET,'1595430043.png',AWS_BUCKET_SECRET_KEY,AWS_BUCKET_KEY);
print ("File Deleted Successfully");
#delete_from_s3(bucket, model, aws_secret, aws_key):
		   
