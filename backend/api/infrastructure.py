import pathlib

import aws_cdk as cdk
import aws_cdk.aws_lambda_python_alpha as lambda_python_alpha
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_ssm as ssm
from constructs import Construct


class API(Construct):
    """API construct for managing API Gateway and Lambda resources."""

    def __init__(
        self,
        scope: Construct,
        id_: str,
        **kwargs: dict,
    ) -> None:
        super().__init__(scope, id_, **kwargs)
        region = cdk.Stack.of(self).region

        bucket_name = ssm.StringParameter.value_for_string_parameter(
            scope=self, parameter_name=f"/secure_csv/{region}/s3_bucket_name"
        )

        self.lambda_function = lambda_python_alpha.PythonFunction(
            scope=self,
            id=f"APILambdaFunction-{region}",
            entry=str(pathlib.Path(__file__).parent.joinpath("runtime").resolve()),
            function_name="secure-csv-api-lambda-function",
            description="Lambda function for generating pre signed URLs for CSV upload",
            index="lambda_function.py",
            handler="lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_12,
            environment={
                "BUCKET_NAME": bucket_name,
            },
        )

        # self.api_gateway_http_api = apigatewayv2_alpha.HttpApi(
        #     scope=self,
        #     id="APIHttpApi",
        #     api_name="SecureCSVAPI",
        #     description="API for Secure CSV processing",
        # )

        # self.api_gateway_http_api.add_routes(
        #     path="/process-csv",
        #     methods=[apigatewayv2_alpha.HttpMethod.POST],
        #     integration=apigatewayv2_integrations_alpha.LambdaProxyIntegration(
        #         handler=self.lambda_function
        #     ),
        # )
