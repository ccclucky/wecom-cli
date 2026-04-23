"""Messages domain APIs."""

from __future__ import annotations

from core.requester import UnifiedRequester


class MessagesAPI:
    def __init__(self, requester: UnifiedRequester) -> None:
        self._requester = requester

    def send_text(self, *, to_user: str, agent_id: int, content: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/message/send",
            json_body={
                "touser": to_user,
                "msgtype": "text",
                "agentid": agent_id,
                "text": {"content": content},
                "safe": 0,
            },
        )
