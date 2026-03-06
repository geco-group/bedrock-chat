"""
Custom model configurations for AWS Bedrock models.

This module contains model configurations that extend the upstream bedrock-chat
to support additional models available in AWS Bedrock before they are added
to the upstream repository.

NOTE: This is a custom extension maintained separately from upstream bedrock-chat.

To add a new model:
1. Add the model ID to CUSTOM_MODEL_IDS
2. Add global inference profile to CUSTOM_GLOBAL_INFERENCE_PROFILES (if supported)
3. Add regional inference profile to CUSTOM_REGIONAL_INFERENCE_PROFILES (if supported)
4. Add pricing to CUSTOM_PRICING
5. Update backend/app/routes/schemas/conversation.py - add to type_model_name
6. Update backend/app/bedrock.py - add to feature support functions if needed
7. Update frontend/src/constants/index.ts - add to AVAILABLE_MODEL_KEYS
8. Update frontend/src/hooks/useModel.ts - add model details
9. Update frontend/src/i18n/en/index.ts - add translations
"""

# Model name to AWS Bedrock model ID mapping
CUSTOM_MODEL_IDS = {
    "claude-v4.6-opus": "anthropic.claude-opus-4-6-v1",
    "claude-v4.6-sonnet": "anthropic.claude-sonnet-4-6",
}

# Global inference profiles for cross-region inference
# Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html
CUSTOM_GLOBAL_INFERENCE_PROFILES = {
    "claude-v4.6-opus": {
        "supported_regions": [
            "ap-northeast-1"
        ]
    },
    "claude-v4.6-sonnet": {
        "supported_regions": [
            "ap-northeast-1"
        ]
    },
}

# Regional inference profiles
# Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html
# Note: ap-northeast-1 (Japan) supports jp. prefix for Sonnet 4.6 (March 2026), but not Opus 4.6
CUSTOM_REGIONAL_INFERENCE_PROFILES = {
    "claude-v4.6-opus": {
        "supported_regions": {} # 03/2026, does not support regional inference in bedrock for region ap-northeast-1 (tokyo).
    },
    "claude-v4.6-sonnet": {
        "supported_regions": {
            # Support jp only for now
            # Japan region (jp.) - Added March 2026
            "ap-northeast-1": "jp",
        }
    },
}

# Pricing configuration (per 1K tokens)
# Reference: https://aws.amazon.com/bedrock/pricing/
CUSTOM_PRICING = {
    "claude-v4.6-opus": {
        "input": 0.015,
        "output": 0.075,
        "cache_write_input": 0.01875,
        "cache_read_input": 0.0015,
    },
    "claude-v4.6-sonnet": {
        "input": 0.003,
        "output": 0.015,
        "cache_write_input": 0.00375,
        "cache_read_input": 0.0003,
    },
}

def get_custom_model_ids():
    """Return custom model IDs to merge with BASE_MODEL_IDS."""
    return CUSTOM_MODEL_IDS.copy()


def get_custom_global_inference_profiles():
    """Return custom global inference profiles."""
    return CUSTOM_GLOBAL_INFERENCE_PROFILES.copy()


def get_custom_regional_inference_profiles():
    """Return custom regional inference profiles."""
    return CUSTOM_REGIONAL_INFERENCE_PROFILES.copy()


def get_custom_pricing():
    """Return custom pricing configuration."""
    return CUSTOM_PRICING.copy()
