"""External contact domain APIs."""

from __future__ import annotations

from core.requester import UnifiedRequester


class CustomersAPI:
    def __init__(self, requester: UnifiedRequester) -> None:
        self._requester = requester

    def list_follow_users(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/externalcontact/get_follow_user_list",
        )
