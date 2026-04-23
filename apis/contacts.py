"""Contacts domain APIs."""

from __future__ import annotations

from core.requester import UnifiedRequester


class ContactsAPI:
    def __init__(self, requester: UnifiedRequester) -> None:
        self._requester = requester

    def list_users(self, department_id: int = 1, fetch_child: bool = True) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/simplelist",
            query={"department_id": department_id, "fetch_child": int(fetch_child)},
        )
