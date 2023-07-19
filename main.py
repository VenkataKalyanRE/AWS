# Replace these with your AWS credentials or configure them using environment variables
AWS_ACCESS_KEY = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
REGION_NAME = 'us-east-1'  # Replace with your desired region

def create_s3_bucket(bucket_name):
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)
    
    # Create an S3 bucket
    s3_client.create_bucket(Bucket=bucket_name)

def upload_file_to_s3(bucket_name, file_path, object_name):
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)
    
    # Upload a file to the specified bucket
    s3_client.upload_file(file_path, bucket_name, object_name)

def list_objects_in_bucket(bucket_name):
    s3_resource = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)
