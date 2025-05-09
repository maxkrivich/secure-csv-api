#!/usr/bin/env python3
import os

import aws_cdk as cdk

from backend.component import Backend

app = cdk.App()

regions = ["us-east-1", "eu-west-1", "ap-southeast-1"]
environments = [
    cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=region,
    )
    for region in regions
]

for environment in environments:
    stack = Backend(
        app,
        f"SecureCSVBackend-{environment.region}",
        env=environment,
        stack_name=f"SecureCSVBackend-{environment.region}",
        description="Backend stack for Secure CSV processing",
    )
    cdk.Tags.of(stack).add("CostCenter", "YourCostCenter")

app.synth()
