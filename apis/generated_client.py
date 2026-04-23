"""Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT."""

from __future__ import annotations

from core.requester import UnifiedRequester


class GeneratedWeComClient:
    def __init__(self, requester: UnifiedRequester) -> None:
        self._requester = requester

    def contacts_list_users(self, *, department_id: int = 1, fetch_child: bool = False) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/user/simplelist',
            query={
                'department_id': department_id,
                'fetch_child': int(fetch_child)
                },
        )

    def customers_list_follow_users(self) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/externalcontact/get_follow_user_list',
        )

    def messages_send_text(self, *, to_user: str, agent_id: int, content: str) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/message/send',
            json_body={
                'touser': to_user,
                'msgtype': 'text',
                'agentid': agent_id,
                'text': {
                'content': content
                },
                'safe': 0
                },
        )
