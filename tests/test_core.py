"""Tests standard tap features using the built-in SDK tests library."""

from datetime import datetime, timedelta
import os

from singer_sdk.testing import get_tap_test_class

from tap_delighted.tap import TapDelighted

SAMPLE_CONFIG = {
    "start_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
    "api_key": os.getenv("TAP_DELIGHTED_API_KEY_NPS"),
}


# Run standard built-in tap tests from the SDK:
TestTapDelighted = get_tap_test_class(
    tap_class=TapDelighted,
    config=SAMPLE_CONFIG,
)
