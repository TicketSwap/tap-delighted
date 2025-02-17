"""Tests standard tap features using the built-in SDK tests library."""

import os
from datetime import datetime, timedelta

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_delighted.tap import TapDelighted

SAMPLE_CONFIG = {
    "start_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
    "api_key": os.environ["TAP_DELIGHTED_API_KEY_NPS"],
}

TEST_SUITE_CONFIG = SuiteConfig(max_records_limit=100)

# Run standard built-in tap tests from the SDK:
TestTapDelighted = get_tap_test_class(
    tap_class=TapDelighted,
    suite_config=TEST_SUITE_CONFIG,
    config=SAMPLE_CONFIG,
)
