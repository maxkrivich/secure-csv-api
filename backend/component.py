import aws_cdk as cdk
from constructs import Construct

from backend.api.infrastructure import API
from backend.storage.infrastructure import Storage


class Backend(cdk.Stack):
    """Backend stack for managing API and storage resources."""

    def __init__(
        self,
        scope: Construct,
        id_: str,
        **kwargs: dict,
    ):
        super().__init__(scope, id_, **kwargs)

        Storage(
            self,
            "Storage",
            bucket_name="secure-csv-bucket",
        )

        API(
            self,
            "API",
        )

        # self.api_endpoint = cdk.CfnOutput(
        #     self,
        #     "APIEndpoint",
        #     value=api.api_gateway_http_api.url,
        # )
