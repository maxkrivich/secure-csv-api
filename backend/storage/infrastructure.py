import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_ssm as ssm
from constructs import Construct


class Storage(Construct):
    """Storage construct for managing S3 bucket resources."""

    def __init__(
        self, scope: Construct, id_: str, bucket_name: str, **kwargs: dict
    ) -> None:
        super().__init__(scope, id_, **kwargs)
        region = cdk.Stack.of(self).region

        self.s3_bucket = s3.Bucket(
            scope=self,
            id=f"Storage{region}Bucket",
            bucket_name=f"{bucket_name}-{region}",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.RETAIN,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            lifecycle_rules=[
                s3.LifecycleRule(
                    id="DeleteOldVersions",
                    abort_incomplete_multipart_upload_after=cdk.Duration.days(7),
                )
            ],
            encryption=s3.BucketEncryption.S3_MANAGED,
        )
        # Outputs
        _ = ssm.StringParameter(
            scope=self,
            id=f"{region}S3BucketNameParameter",
            parameter_name=f"/secure_csv/{region}/s3_bucket_name",
            description="S3 bucket name for secure CSV storage",
            string_value=self.s3_bucket.bucket_name,
        )
