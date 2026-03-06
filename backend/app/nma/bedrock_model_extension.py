"""
Bedrock model extension for request logging.

This module extends the Strands BedrockModel to log Bedrock request IDs
for improved observability.

NOTE: This is a custom extension maintained separately from upstream bedrock-chat.
"""

import logging
from typing import Any

from strands.models import BedrockModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BedrockClientWrapper:
    """Wrapper around boto3 Bedrock client that logs request IDs."""

    def __init__(self, client: Any):
        self._client = client

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self._client, name)
        if name in ("converse", "converse_stream"):
            return self._wrap_method(attr)
        return attr

    def _wrap_method(self, method: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            response = method(*args, **kwargs)
            bedrock_request_id = response.get("ResponseMetadata", {}).get(
                "RequestId", ""
            )
            if bedrock_request_id:
                logger.info(f"Bedrock API response received: bedrock_request_id={bedrock_request_id}")
            return response

        return wrapper


class BedrockModelWithLogging(BedrockModel):
    """Extended BedrockModel that logs Bedrock Request IDs."""

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.client = BedrockClientWrapper(self.client)
