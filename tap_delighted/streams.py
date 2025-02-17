"""Stream type classes for tap-delighted."""

from __future__ import annotations

import typing as t
from datetime import datetime
from typing import Iterable

import delighted
import pytz
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_delighted.client import DelightedStream


class SurveyResponsesStream(DelightedStream):
    """Define custom stream."""

    name = "survey_responses"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("person", th.StringType),
        th.Property(
            "score",
            th.IntegerType,
            description="The survey response score",
        ),
        th.Property("created_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property(
            "person_properties",
            th.ObjectType(
                th.Property("CaseId", th.StringType),
                th.Property("UserId", th.StringType),
                th.Property("UserCountry", th.StringType),
                th.Property("ClosedByEmployee", th.StringType),
                th.Property("Delighted Source", th.StringType),
                th.Property("Delighted Link Name", th.StringType),
                th.Property("Delighted Device Type", th.StringType),
                th.Property("Delighted Operating System", th.StringType),
                th.Property("Delighted Browser", th.StringType),
                th.Property("ts_user_id", th.StringType),
                th.Property("event_id", th.StringType),
                th.Property("case_id", th.StringType),
                th.Property("solved_reason", th.StringType),
                th.Property("touchpoint", th.StringType),
            ),
        ),
    ).to_dict()

    def get_records(self, context: dict | None) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        starting_date = self.get_starting_replication_key_value(context)
        if type(starting_date) is str:
            since = datetime.strptime(starting_date, "%Y-%m-%d")  # noqa: DTZ007
        else:
            since = datetime.fromtimestamp(starting_date)  # noqa: DTZ006
        since = since.replace(tzinfo=pytz.UTC)
        response = True
        page = 1
        survey_responses = []

        while response:
            self.logger.info(f"retrieving page {page} of survey responses")  # noqa: G004
            response = delighted.SurveyResponse.all(page=page, per_page=100, since=since)
            survey_responses.extend(response)
            page += 1

        yield from survey_responses
