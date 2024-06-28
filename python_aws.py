import boto3
# configure your ssm client here, such as AWS key or region
ssm_client = boto3.client('ssm',
    region_name="us-east-1",
    aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
    aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
)
# then pass to the store
store = SSMParameterStore(ssm_client=ssm_client)