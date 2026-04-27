"""Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT."""

from __future__ import annotations

from typing import Any

from core.requester import UnifiedRequester


class GeneratedWeComClient:
    def __init__(self, requester: UnifiedRequester) -> None:
        self._requester = requester

    def auth_get_token(self, *, corpid: str, corpsecret: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/gettoken',
            query={
                'corpid': corpid,
                'corpsecret': corpsecret
                },
        )

    def batch_invite(self, *, user: Any | None = None, party: Any | None = None, tag: Any | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/batch/invite',
            json_body={
                'user': user,
                'party': party,
                'tag': tag
                },
        )

    def batch_replaceparty(self, *, media_id: str, callback: Any | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/batch/replaceparty',
            json_body={
                'media_id': media_id,
                'callback': callback
                },
        )

    def batch_replaceuser(self, *, media_id: str, to_invite: Any | None = None, callback: Any | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/batch/replaceuser',
            json_body={
                'media_id': media_id,
                'to_invite': to_invite,
                'callback': callback
                },
        )

    def batch_syncuser(self, *, media_id: str, to_invite: Any | None = None, callback: Any | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/batch/syncuser',
            json_body={
                'media_id': media_id,
                'to_invite': to_invite,
                'callback': callback
                },
        )

    def contacts_list_users(self, *, department_id: int = 1, fetch_child: bool = False) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/user/simplelist',
            query={
                'department_id': department_id,
                'fetch_child': int(fetch_child)
                },
        )

    def corp_get_join_qrcode(self, *, size_type: str | None = None) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/corp/get_join_qrcode',
            query={
                'size_type': size_type
                },
        )

    def corp_opencorpid_to_corpid(self, *, open_userid_list: Any, source_agentid: int) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/corp/opencorpid_to_corpid',
            json_body={
                'open_userid_list': open_userid_list,
                'source_agentid': source_agentid
                },
        )

    def departments_delete(self, *, id: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/department/delete',
            query={
                'id': id
                },
        )

    def departments_get(self, *, id: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/department/get',
            query={
                'id': id
                },
        )

    def departments_list(self, *, id: str | None = None) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/department/list',
            query={
                'id': id
                },
        )

    def departments_list_ids(self, *, id: str | None = None) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/department/simplelist',
            query={
                'id': id
                },
        )

    def departments_create(self, *, name: str, name_en: str | None = None, parentid: int, order: int | None = None, id: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/department/create',
            json_body={
                'name': name,
                'name_en': name_en,
                'parentid': parentid,
                'order': order,
                'id': id
                },
        )

    def departments_update(self, *, id: int, name: str | None = None, name_en: str | None = None, parentid: int | None = None, order: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/department/update',
            json_body={
                'id': id,
                'name': name,
                'name_en': name_en,
                'parentid': parentid,
                'order': order
                },
        )

    def idconvert_convert_tmp_external_userid(self, *, business_type: int, user_type: int, tmp_external_userid_list: Any) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/idconvert/convert_tmp_external_userid',
            json_body={
                'business_type': business_type,
                'user_type': user_type,
                'tmp_external_userid_list': tmp_external_userid_list
                },
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

    def network_get_api_domain_ip(self) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/get_api_domain_ip',
        )

    def network_get_callback_ip(self) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/getcallbackip',
        )

    def tags_delete(self, *, tagid: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/tag/delete',
            query={
                'tagid': tagid
                },
        )

    def tags_get(self, *, tagid: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/tag/get',
            query={
                'tagid': tagid
                },
        )

    def tags_list(self) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/tag/list',
        )

    def tags_create(self, *, tagname: str, tagid: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/tag/create',
            json_body={
                'tagname': tagname,
                'tagid': tagid
                },
        )

    def tags_update(self, *, tagid: int, tagname: str) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/tag/update',
            json_body={
                'tagid': tagid,
                'tagname': tagname
                },
        )

    def tags_addtagusers(self, *, tagid: int, userlist: Any | None = None, partylist: Any | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/tag/addtagusers',
            json_body={
                'tagid': tagid,
                'userlist': userlist,
                'partylist': partylist
                },
        )

    def tags_deltagusers(self, *, tagid: int, userlist: Any | None = None, partylist: Any | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/tag/deltagusers',
            json_body={
                'tagid': tagid,
                'userlist': userlist,
                'partylist': partylist
                },
        )

    def users_authsucc(self, *, userid: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/user/authsucc',
            query={
                'userid': userid
                },
        )

    def users_delete(self, *, userid: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/user/delete',
            query={
                'userid': userid
                },
        )

    def users_get(self, *, userid: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/user/get',
            query={
                'userid': userid
                },
        )

    def users_list(self, *, department_id: str) -> dict:
        return self._requester.request(
            method='GET',
            endpoint='/cgi-bin/user/list',
            query={
                'department_id': department_id
                },
        )

    def users_batchdelete(self, *, useridlist: Any) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/batchdelete',
            json_body={
                'useridlist': useridlist
                },
        )

    def users_convert_to_openid(self, *, userid: str) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/convert_to_openid',
            json_body={
                'userid': userid
                },
        )

    def users_get_userid_by_email(self, *, email: str, email_type: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/get_userid_by_email',
            json_body={
                'email': email,
                'email_type': email_type
                },
        )

    def users_getuserid(self, *, mobile: str) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/getuserid',
            json_body={
                'mobile': mobile
                },
        )

    def users_list_id(self, *, cursor: str | None = None, limit: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/list_id',
            json_body={
                'cursor': cursor,
                'limit': limit
                },
        )

    def users_create(self, *, userid: str, name: str, alias: str | None = None, mobile: str | None = None, department: Any | None = None, order: Any | None = None, position: str | None = None, gender: str | None = None, email: str | None = None, biz_mail: str | None = None, telephone: str | None = None, is_leader_in_dept: Any | None = None, direct_leader: Any | None = None, avatar_mediaid: str | None = None, enable: int | None = None, extattr: Any | None = None, to_invite: Any | None = None, external_profile: Any | None = None, external_position: str | None = None, nickname: str | None = None, address: str | None = None, main_department: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/create',
            json_body={
                'userid': userid,
                'name': name,
                'alias': alias,
                'mobile': mobile,
                'department': department,
                'order': order,
                'position': position,
                'gender': gender,
                'email': email,
                'biz_mail': biz_mail,
                'telephone': telephone,
                'is_leader_in_dept': is_leader_in_dept,
                'direct_leader': direct_leader,
                'avatar_mediaid': avatar_mediaid,
                'enable': enable,
                'extattr': extattr,
                'to_invite': to_invite,
                'external_profile': external_profile,
                'external_position': external_position,
                'nickname': nickname,
                'address': address,
                'main_department': main_department
                },
        )

    def users_update(self, *, userid: str, name: str | None = None, alias: str | None = None, mobile: str | None = None, department: Any | None = None, order: Any | None = None, position: str | None = None, gender: str | None = None, email: str | None = None, biz_mail: str | None = None, biz_mail_alias: Any | None = None, telephone: str | None = None, is_leader_in_dept: Any | None = None, direct_leader: Any | None = None, avatar_mediaid: str | None = None, enable: int | None = None, extattr: Any | None = None, external_profile: Any | None = None, external_position: str | None = None, nickname: str | None = None, address: str | None = None, main_department: int | None = None) -> dict:
        return self._requester.request(
            method='POST',
            endpoint='/cgi-bin/user/update',
            json_body={
                'userid': userid,
                'name': name,
                'alias': alias,
                'mobile': mobile,
                'department': department,
                'order': order,
                'position': position,
                'gender': gender,
                'email': email,
                'biz_mail': biz_mail,
                'biz_mail_alias': biz_mail_alias,
                'telephone': telephone,
                'is_leader_in_dept': is_leader_in_dept,
                'direct_leader': direct_leader,
                'avatar_mediaid': avatar_mediaid,
                'enable': enable,
                'extattr': extattr,
                'external_profile': external_profile,
                'external_position': external_position,
                'nickname': nickname,
                'address': address,
                'main_department': main_department
                },
        )
