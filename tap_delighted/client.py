"""REST client handling, including DelightedStream base class."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import delighted
from singer_sdk.streams import Stream

if TYPE_CHECKING:
    from singer_sdk.tap_base import Tap

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class DelightedStream(Stream):
    """Delighted stream class."""

    def __init__(self, tap: Tap) -> None:
        """Initialize the DelightedStream with the given Tap instance.

        Args:
            tap (Tap): The Tap instance.
        """
        super().__init__(tap)
        delighted.api_key = self.config.get("api_key")
