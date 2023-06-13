from attr import define, field
from griptape.artifacts import BaseArtifact
from griptape.core import BaseTool
from griptape.core.decorators import activity
from schema import Schema


@define
class AwsPricing(BaseTool):
    aws_access_key_id: str = field(default=None, kw_only=True, metadata={"env": "AWS_ACCESS_KEY_ID"})
    aws_secret_access_key: str = field(default=None, kw_only=True, metadata={"env": "AWS_SECRET_ACCESS_KEY"})

    @activity(config={
        "description": "can be used to get the account or IAM principal of the caller",
        "schema": Schema(
            str,
            description="context of this activity"
        )
    })
    def get_caller_identity(self, params: dict) -> BaseArtifact:
        return BaseArtifact("not implemented")
