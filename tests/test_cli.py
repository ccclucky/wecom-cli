from __future__ import annotations

from argparse import Namespace

from cli.main import route


class DummyContacts:
    def list_users(self, department_id, fetch_child):
        return {"department_id": department_id, "fetch_child": fetch_child}


class DummyMessages:
    def send_text(self, *, to_user, agent_id, content):
        return {"to_user": to_user, "agent_id": agent_id, "content": content}


class DummyCustomers:
    def list_follow_users(self):
        return {"user": ["zhangsan"]}


def test_route_contacts():
    args = Namespace(domain="contacts", action="list", department_id=2, fetch_child=True)
    result = route(args, DummyContacts(), DummyMessages(), DummyCustomers())
    assert result["department_id"] == 2


def test_route_messages():
    args = Namespace(
        domain="messages",
        action="send-text",
        to_user="zhangsan",
        agent_id=1,
        content="hello",
    )
    result = route(args, DummyContacts(), DummyMessages(), DummyCustomers())
    assert result["to_user"] == "zhangsan"


def test_route_customers():
    args = Namespace(domain="customers", action="list-follow-users")
    result = route(args, DummyContacts(), DummyMessages(), DummyCustomers())
    assert result["user"] == ["zhangsan"]
