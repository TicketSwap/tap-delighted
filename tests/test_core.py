"""Tests standard tap features using the built-in SDK tests library."""

import datetime
import os

from singer_sdk.testing import get_tap_test_class

from tap_delighted.tap import TapDelighted

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "auth_token": os.getenv('TAP_DELIGHTED_AUTH_TOKEN')
}


# Run standard built-in tap tests from the SDK:
TestTapDelighted = get_tap_test_class(
    tap_class=TapDelighted,
    config=SAMPLE_CONFIG,
)