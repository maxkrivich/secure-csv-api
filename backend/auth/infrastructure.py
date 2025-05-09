# generate stack with cognito auth
import aws_cdk as cdk
import aws_cdk.aws_cognito as cognito
from constructs import Construct


class Auth(Construct):
    """Auth construct for managing Cognito User Pool and Identity Pool resources."""

    def __init__(
        self,
        scope: Construct,
        id_: str,
        **kwargs: dict,
    ) -> None:
        super().__init__(scope, id_, **kwargs)

        # TODO: add user pool client with auth flow
