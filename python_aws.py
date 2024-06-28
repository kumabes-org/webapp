import boto3
# configure your ssm client here, such as AWS key or region
ssm_client = boto3.client('ssm',
    region_name="us-east-1",
    aws_access_key_id="AKIEXAMPLEEQPQR12345",
    aws_secret_access_key="EXAMPLEFgSm0xPRIvaTeKB8Nt5LX97EAnEKa12345"
)
# then pass to the store
store = SSMParameterStore(ssm_client=ssm_client)