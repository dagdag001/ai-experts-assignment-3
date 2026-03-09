from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from dateutil.parser import isoparse


@dataclass
class OAuth2Token:
    access_token: str
    expires_at: int  

    @property
    def expired(self) -> bool:
        return int(datetime.now(tz=timezone.utc).timestamp()) >= self.expires_at

    def as_header(self) -> str:
        return f"Bearer {self.access_token}"


def token_from_iso(access_token: str, expires_at_iso: str) -> OAuth2Token:
    dt = isoparse(expires_at_iso)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    expires_at = int(dt.timestamp())
    return OAuth2Token(access_token=access_token, expires_at=expires_at)