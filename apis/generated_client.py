"""Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT."""

from __future__ import annotations

from typing import Any

from core.requester import UnifiedRequester


class GeneratedWeComClient:
    def __init__(self, requester: UnifiedRequester) -> None:
        self._requester = requester

    def advanced_feature_get_apply_id_list(
        self,
        *,
        business_type: str,
        userid: str,
        limit: int | None = None,
        cursor: str | None = None,
        req_type: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/advanced_feature/get_apply_id_list",
            json_body={
                "business_type": business_type,
                "userid": userid,
                "limit": limit,
                "cursor": cursor,
                "req_type": req_type,
            },
        )

    def advanced_feature_get_approval_info(self, *, apply_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/advanced_feature/get_approval_info",
            json_body={"apply_id": apply_id},
        )

    def advanced_feature_set_approval_detail(
        self,
        *,
        apply_id: str,
        approval_id: str,
        approval_status: str,
        approval_url: str,
        process_list_node_list: str,
        process_list_node_list_node_apv_status: str,
        process_list_node_list_node_apv_rel: str,
        process_list_node_list_current_approvers: str | None = None,
        process_list_node_list_completed_approvers: str | None = None,
        process_list_node_list_apv_update_time: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/advanced_feature/set_approval_detail",
            json_body={
                "apply_id": apply_id,
                "approval_id": approval_id,
                "approval_status": approval_status,
                "approval_url": approval_url,
                "process_list_node_list": process_list_node_list,
                "process_list_node_list_node_apv_status": process_list_node_list_node_apv_status,
                "process_list_node_list_node_apv_rel": process_list_node_list_node_apv_rel,
                "process_list_node_list_current_approvers": process_list_node_list_current_approvers,
                "process_list_node_list_completed_approvers": process_list_node_list_completed_approvers,
                "process_list_node_list_apv_update_time": process_list_node_list_apv_update_time,
            },
        )

    def appchat_get(self, *, chatid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/appchat/get",
            query={"chatid": chatid},
        )

    def appchat_update(
        self,
        *,
        chatid: str,
        name: str | None = None,
        owner: str | None = None,
        add_user_list: str | None = None,
        del_user_list: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/appchat/update",
            json_body={
                "chatid": chatid,
                "name": name,
                "owner": owner,
                "add_user_list": add_user_list,
                "del_user_list": del_user_list,
            },
        )

    def auth_get_token(self, *, corpid: str, corpsecret: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/gettoken",
            query={"corpid": corpid, "corpsecret": corpsecret},
        )

    def auth_getuserdetail(self, *, user_ticket: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/auth/getuserdetail",
            json_body={"user_ticket": user_ticket},
        )

    def auth_getuserinfo(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/auth/getuserinfo",
        )

    def batch_invite(self, *, user: Any | None = None, party: Any | None = None, tag: Any | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/batch/invite",
            json_body={"user": user, "party": party, "tag": tag},
        )

    def batch_replaceparty(self, *, media_id: str, callback: Any | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/batch/replaceparty",
            json_body={"media_id": media_id, "callback": callback},
        )

    def batch_replaceuser(self, *, media_id: str, to_invite: Any | None = None, callback: Any | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/batch/replaceuser",
            json_body={"media_id": media_id, "to_invite": to_invite, "callback": callback},
        )

    def batch_syncuser(self, *, media_id: str, to_invite: Any | None = None, callback: Any | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/batch/syncuser",
            json_body={"media_id": media_id, "to_invite": to_invite, "callback": callback},
        )

    def chatdata_async_program_task(self, *, program_id: str, ability_id: str, request_data: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/async_program_task",
            json_body={"program_id": program_id, "ability_id": ability_id, "request_data": request_data},
        )

    def chatdata_check_debug_mode(self, *, program_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/check_debug_mode",
            json_body={"program_id": program_id},
        )

    def chatdata_close_debug_mode(self, *, program_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/close_debug_mode",
            json_body={"program_id": program_id},
        )

    def chatdata_get_auth_user_list(self, *, cursor: str | None = None, limit: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/get_auth_user_list",
            json_body={"cursor": cursor, "limit": limit},
        )

    def chatdata_open_debug_mode(self, *, program_id: str, debug_token: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/open_debug_mode",
            json_body={"program_id": program_id, "debug_token": debug_token},
        )

    def chatdata_set_hide_sensitiveinfo_config(self, *, userid: str, config: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/set_hide_sensitiveinfo_config",
            json_body={"userid": userid, "config": config},
        )

    def chatdata_set_log_level(self, *, program_id: str, log_level: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/set_log_level",
            json_body={"program_id": program_id, "log_level": log_level},
        )

    def chatdata_set_public_key(self, *, public_key: str, public_key_ver: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/set_public_key",
            json_body={"public_key": public_key, "public_key_ver": public_key_ver},
        )

    def chatdata_set_receive_callback(self, *, program_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/set_receive_callback",
            json_body={"program_id": program_id},
        )

    def chatdata_sync_call_program(
        self, *, program_id: str, ability_id: str, notify_id: str | None = None, request_data: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/sync_call_program",
            json_body={
                "program_id": program_id,
                "ability_id": ability_id,
                "notify_id": notify_id,
                "request_data": request_data,
            },
        )

    def chatdata_upload_media(self, *, type: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/chatdata/upload_media",
            json_body={"type": type},
        )

    def checkin_add_checkin_record(
        self,
        *,
        records: str,
        userid: str,
        checkin_time: str,
        location_title: str,
        location_detail: str,
        notes: str | None = None,
        wifiname: str | None = None,
        wifimac: str | None = None,
        mediaids: str | None = None,
        lat: str | None = None,
        lng: str | None = None,
        device_type: str,
        device_detail: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/checkin/add_checkin_record",
            json_body={
                "records": records,
                "userid": userid,
                "checkin_time": checkin_time,
                "location_title": location_title,
                "location_detail": location_detail,
                "notes": notes,
                "wifiname": wifiname,
                "wifimac": wifimac,
                "mediaids": mediaids,
                "lat": lat,
                "lng": lng,
                "device_type": device_type,
                "device_detail": device_detail,
            },
        )

    def checkin_punch_correction(
        self,
        *,
        userid: str,
        schedule_date_time: str,
        schedule_checkin_time: str | None = None,
        checkin_time: str,
        remark: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/checkin/punch_correction",
            json_body={
                "userid": userid,
                "schedule_date_time": schedule_date_time,
                "schedule_checkin_time": schedule_checkin_time,
                "checkin_time": checkin_time,
                "remark": remark,
            },
        )

    def contacts_list_users(self, *, department_id: int, fetch_child: bool = False) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/simplelist",
            query={"department_id": department_id, "fetch_child": int(fetch_child)},
        )

    def corp_get_join_qrcode(self, *, size_type: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/corp/get_join_qrcode",
            query={"size_type": size_type},
        )

    def corp_opencorpid_to_corpid(self, *, open_userid_list: Any, source_agentid: int) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corp/opencorpid_to_corpid",
            json_body={"open_userid_list": open_userid_list, "source_agentid": source_agentid},
        )

    def corp_getapprovaldata(self, *, starttime: str, endtime: str, next_spnum: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corp/getapprovaldata",
            json_body={"starttime": starttime, "endtime": endtime, "next_spnum": next_spnum},
        )

    def corpgroup_corp_get_chain_list(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/corpgroup/corp/get_chain_list",
        )

    def corpgroup_corp_get_chain_user_custom_id(self, *, chain_id: str, corpid: str, userid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/corp/get_chain_user_custom_id",
            json_body={"chain_id": chain_id, "corpid": corpid, "userid": userid},
        )

    def corpgroup_corp_gettoken(self, *, corpid: str, agentid: str, business_type: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/corp/gettoken",
            json_body={"corpid": corpid, "agentid": agentid, "business_type": business_type},
        )

    def corpgroup_corp_list_app_share_info(
        self,
        *,
        business_type: str | None = None,
        agentid: str,
        corpid: str | None = None,
        limit: str | None = None,
        cursor: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/corp/list_app_share_info",
            json_body={
                "business_type": business_type,
                "agentid": agentid,
                "corpid": corpid,
                "limit": limit,
                "cursor": cursor,
            },
        )

    def corpgroup_corp_remove_corp(
        self, *, chain_id: str, corpid: str | None = None, pending_corpid: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/corp/remove_corp",
            json_body={"chain_id": chain_id, "corpid": corpid, "pending_corpid": pending_corpid},
        )

    def corpgroup_get_corp_shared_chain_list(self, *, corpid: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/get_corp_shared_chain_list",
            json_body={"corpid": corpid},
        )

    def corpgroup_getresult(self, *, jobid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/corpgroup/getresult",
            query={"jobid": jobid},
        )

    def corpgroup_import_chain_contact(
        self,
        *,
        chain_id: str,
        contact_list: str,
        contact_list_corp_name: str,
        contact_list_group_path: str | None = None,
        contact_list_custom_id: str | None = None,
        contact_list_contact_info_list: str,
        contact_list_contact_info_list_name: str,
        contact_list_contact_info_list_identity_type: str,
        contact_list_contact_info_list_mobile: str,
        contact_list_contact_info_list_user_custom_id: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/import_chain_contact",
            json_body={
                "chain_id": chain_id,
                "contact_list": contact_list,
                "contact_list_corp_name": contact_list_corp_name,
                "contact_list_group_path": contact_list_group_path,
                "contact_list_custom_id": contact_list_custom_id,
                "contact_list_contact_info_list": contact_list_contact_info_list,
                "contact_list_contact_info_list_name": contact_list_contact_info_list_name,
                "contact_list_contact_info_list_identity_type": contact_list_contact_info_list_identity_type,
                "contact_list_contact_info_list_mobile": contact_list_contact_info_list_mobile,
                "contact_list_contact_info_list_user_custom_id": contact_list_contact_info_list_user_custom_id,
            },
        )

    def corpgroup_rule_list_ids(self, *, chain_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/rule/list_ids",
            json_body={"chain_id": chain_id},
        )

    def corpgroup_unionid_to_external_userid(
        self, *, unionid: str, openid: str, corpid: str | None = None, mass_call_ticket: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/corpgroup/unionid_to_external_userid",
            json_body={"unionid": unionid, "openid": openid, "corpid": corpid, "mass_call_ticket": mass_call_ticket},
        )

    def customers_add_contact_way(
        self,
        *,
        type: str,
        scene: str,
        style: str | None = None,
        remark: str | None = None,
        skip_verify: bool | None = None,
        state: str | None = None,
        user: str | None = None,
        party: str | None = None,
        is_temp: bool | None = None,
        expires_in: str | None = None,
        chat_expires_in: str | None = None,
        unionid: str | None = None,
        is_exclusive: bool | None = None,
        mark_source: bool | None = None,
        conclusions: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/add_contact_way",
            json_body={
                "type": type,
                "scene": scene,
                "style": style,
                "remark": remark,
                "skip_verify": skip_verify,
                "state": state,
                "user": user,
                "party": party,
                "is_temp": is_temp,
                "expires_in": expires_in,
                "chat_expires_in": chat_expires_in,
                "unionid": unionid,
                "is_exclusive": is_exclusive,
                "mark_source": mark_source,
                "conclusions": conclusions,
            },
        )

    def customers_batch_get_by_user(
        self, *, userid_list: str, cursor: str | None = None, limit: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/batch/get_by_user",
            json_body={"userid_list": userid_list, "cursor": cursor, "limit": limit},
        )

    def customers_cancel_groupmsg_send(self, *, msgid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/cancel_groupmsg_send",
            json_body={"msgid": msgid},
        )

    def customers_cancel_moment_task(self, *, moment_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/cancel_moment_task",
            json_body={"moment_id": moment_id},
        )

    def customers_convert_to_openid(self, *, external_userid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/convert_to_openid",
            json_body={"external_userid": external_userid},
        )

    def customers_customer_acquisition_list_link(self, *, limit: str | None = None, cursor: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/customer_acquisition/list_link",
            json_body={"limit": limit, "cursor": cursor},
        )

    def customers_customer_strategy_list(self, *, cursor: str | None = None, limit: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/customer_strategy/list",
            json_body={"cursor": cursor, "limit": limit},
        )

    def customers_get(self, *, external_userid: str, cursor: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/externalcontact/get",
            query={"external_userid": external_userid, "cursor": cursor},
        )

    def customers_get_follow_user_list(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/externalcontact/get_follow_user_list",
        )

    def customers_get_strategy_tag_list(
        self, *, strategy_id: str | None = None, tag_id: str | None = None, group_id: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/get_strategy_tag_list",
            json_body={"strategy_id": strategy_id, "tag_id": tag_id, "group_id": group_id},
        )

    def customers_get_subscribe_qr_code(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/externalcontact/get_subscribe_qr_code",
        )

    def customers_groupchat_get(self, *, chat_id: str, need_name: bool | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/groupchat/get",
            json_body={"chat_id": chat_id, "need_name": need_name},
        )

    def customers_groupchat_list(
        self,
        *,
        status_filter: str | None = None,
        owner_filter: str | None = None,
        owner_filter_userid_list: str | None = None,
        cursor: str | None = None,
        limit: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/groupchat/list",
            json_body={
                "status_filter": status_filter,
                "owner_filter": owner_filter,
                "owner_filter_userid_list": owner_filter_userid_list,
                "cursor": cursor,
                "limit": limit,
            },
        )

    def customers_groupchat_onjob_transfer(self, *, chat_id_list: str, new_owner: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/groupchat/onjob_transfer",
            json_body={"chat_id_list": chat_id_list, "new_owner": new_owner},
        )

    def customers_list(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/externalcontact/list",
            query={"userid": userid},
        )

    def customers_mark_tag(
        self, *, userid: str, external_userid: str, add_tag: str | None = None, remove_tag: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/mark_tag",
            json_body={
                "userid": userid,
                "external_userid": external_userid,
                "add_tag": add_tag,
                "remove_tag": remove_tag,
            },
        )

    def customers_message_send(
        self,
        *,
        recv_scope: int | None = None,
        to_parent_userid: Any | None = None,
        to_student_userid: Any | None = None,
        to_party: Any | None = None,
        toall: int | None = None,
        msgtype: str | None = None,
        agentid: int | None = None,
        text: Any | None = None,
        enable_id_trans: int | None = None,
        enable_duplicate_check: int | None = None,
        duplicate_check_interval: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/message/send",
            json_body={
                "recv_scope": recv_scope,
                "to_parent_userid": to_parent_userid,
                "to_student_userid": to_student_userid,
                "to_party": to_party,
                "toall": toall,
                "msgtype": msgtype,
                "agentid": agentid,
                "text": text,
                "enable_id_trans": enable_id_trans,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval,
            },
        )

    def customers_opengid_to_chatid(self, *, opengid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/opengid_to_chatid",
            json_body={"opengid": opengid},
        )

    def customers_remark(
        self,
        *,
        userid: str,
        external_userid: str,
        remark: str | None = None,
        description: str | None = None,
        remark_company: str | None = None,
        remark_mobiles: str | None = None,
        remark_pic_mediaid: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/remark",
            json_body={
                "userid": userid,
                "external_userid": external_userid,
                "remark": remark,
                "description": description,
                "remark_company": remark_company,
                "remark_mobiles": remark_mobiles,
                "remark_pic_mediaid": remark_pic_mediaid,
            },
        )

    def customers_remind_groupmsg_send(self, *, msgid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/remind_groupmsg_send",
            json_body={"msgid": msgid},
        )

    def customers_resigned_transfer_customer(
        self, *, handover_userid: str, takeover_userid: str, external_userid: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/resigned/transfer_customer",
            json_body={
                "handover_userid": handover_userid,
                "takeover_userid": takeover_userid,
                "external_userid": external_userid,
            },
        )

    def customers_send_welcome_msg(
        self,
        *,
        welcome_code: str,
        text_content: str | None = None,
        attachments: str | None = None,
        attachments_msgtype: str,
        image_media_id: str | None = None,
        image_pic_url: str | None = None,
        link_title: str,
        link_picurl: str | None = None,
        link_desc: str | None = None,
        link_url: str,
        miniprogram_title: str,
        miniprogram_pic_media_id: str,
        miniprogram_appid: str,
        miniprogram_page: str,
        video_media_id: str,
        file_media_id: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/send_welcome_msg",
            json_body={
                "welcome_code": welcome_code,
                "text_content": text_content,
                "attachments": attachments,
                "attachments_msgtype": attachments_msgtype,
                "image_media_id": image_media_id,
                "image_pic_url": image_pic_url,
                "link_title": link_title,
                "link_picurl": link_picurl,
                "link_desc": link_desc,
                "link_url": link_url,
                "miniprogram_title": miniprogram_title,
                "miniprogram_pic_media_id": miniprogram_pic_media_id,
                "miniprogram_appid": miniprogram_appid,
                "miniprogram_page": miniprogram_page,
                "video_media_id": video_media_id,
                "file_media_id": file_media_id,
            },
        )

    def customers_set_subscribe_mode(self, *, subscribe_mode: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/set_subscribe_mode",
            json_body={"subscribe_mode": subscribe_mode},
        )

    def customers_transfer_customer(
        self,
        *,
        handover_userid: str,
        takeover_userid: str,
        external_userid: str,
        transfer_success_msg: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalcontact/transfer_customer",
            json_body={
                "handover_userid": handover_userid,
                "takeover_userid": takeover_userid,
                "external_userid": external_userid,
                "transfer_success_msg": transfer_success_msg,
            },
        )

    def departments_delete(self, *, id: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/department/delete",
            query={"id": id},
        )

    def departments_get(self, *, id: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/department/get",
            query={"id": id},
        )

    def departments_list(self, *, id: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/department/list",
            query={"id": id},
        )

    def departments_list_ids(self, *, id: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/department/simplelist",
            query={"id": id},
        )

    def departments_create(
        self, *, name: str, name_en: str | None = None, parentid: int, order: int | None = None, id: int | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/department/create",
            json_body={"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": id},
        )

    def departments_update(
        self,
        *,
        id: int,
        name: str | None = None,
        name_en: str | None = None,
        parentid: int | None = None,
        order: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/department/update",
            json_body={"id": id, "name": name, "name_en": name_en, "parentid": parentid, "order": order},
        )

    def dial_get_dial_record(
        self,
        *,
        start_time: str | None = None,
        end_time: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/dial/get_dial_record",
            json_body={"start_time": start_time, "end_time": end_time, "offset": offset, "limit": limit},
        )

    def exmail_app_compose_send(
        self,
        *,
        to: str,
        to_emails: str | None = None,
        to_userids: str | None = None,
        cc: str | None = None,
        cc_emails: str | None = None,
        cc_userids: str | None = None,
        bcc: str | None = None,
        bcc_emails: str | None = None,
        bcc_userids: str | None = None,
        subject: str,
        content: str,
        attachment_list: str | None = None,
        attachment_list_file_name: str,
        attachment_list_content: str,
        content_type: str | None = None,
        schedule: str,
        schedule_schedule_id: str | None = None,
        schedule_method: str | None = None,
        schedule_location: str | None = None,
        schedule_start_time: int,
        schedule_end_time: int,
        schedule_reminders: str | None = None,
        schedule_reminders_is_remind: bool | None = None,
        schedule_reminders_remind_before_event_mins: int | None = None,
        schedule_reminders_timezone: int | None = None,
        schedule_reminders_is_repeat: bool | None = None,
        schedule_reminders_is_custom_repeat: bool | None = None,
        schedule_reminders_repeat_type: int | None = None,
        schedule_reminders_repeat_interval: int | None = None,
        schedule_reminders_repeat_day_of_week: str | None = None,
        schedule_reminders_repeat_day_of_month: str | None = None,
        schedule_reminders_repeat_month_of_year: str | None = None,
        schedule_reminders_repeat_until: int | None = None,
        meeting: str | None = None,
        meeting_hosts: str | None = None,
        meeting_meeting_admins: str,
        meeting_option: str | None = None,
        meeting_option_password: str | None = None,
        meeting_option_auto_record: bool | None = None,
        meeting_option_enable_waiting_room: bool | None = None,
        meeting_option_allow_enter_before_host: bool | None = None,
        meeting_option_enter_restraint: bool | None = None,
        meeting_option_enable_screen_watermark: bool | None = None,
        meeting_option_enable_enter_mute: bool | None = None,
        meeting_option_remind_scope: bool | None = None,
        meeting_option_water_mark_type: int | None = None,
        enable_id_trans: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/app/compose_send",
            json_body={
                "to": to,
                "to_emails": to_emails,
                "to_userids": to_userids,
                "cc": cc,
                "cc_emails": cc_emails,
                "cc_userids": cc_userids,
                "bcc": bcc,
                "bcc_emails": bcc_emails,
                "bcc_userids": bcc_userids,
                "subject": subject,
                "content": content,
                "attachment_list": attachment_list,
                "attachment_list_file_name": attachment_list_file_name,
                "attachment_list_content": attachment_list_content,
                "content_type": content_type,
                "schedule": schedule,
                "schedule_schedule_id": schedule_schedule_id,
                "schedule_method": schedule_method,
                "schedule_location": schedule_location,
                "schedule_start_time": schedule_start_time,
                "schedule_end_time": schedule_end_time,
                "schedule_reminders": schedule_reminders,
                "schedule_reminders_is_remind": schedule_reminders_is_remind,
                "schedule_reminders_remind_before_event_mins": schedule_reminders_remind_before_event_mins,
                "schedule_reminders_timezone": schedule_reminders_timezone,
                "schedule_reminders_is_repeat": schedule_reminders_is_repeat,
                "schedule_reminders_is_custom_repeat": schedule_reminders_is_custom_repeat,
                "schedule_reminders_repeat_type": schedule_reminders_repeat_type,
                "schedule_reminders_repeat_interval": schedule_reminders_repeat_interval,
                "schedule_reminders_repeat_day_of_week": schedule_reminders_repeat_day_of_week,
                "schedule_reminders_repeat_day_of_month": schedule_reminders_repeat_day_of_month,
                "schedule_reminders_repeat_month_of_year": schedule_reminders_repeat_month_of_year,
                "schedule_reminders_repeat_until": schedule_reminders_repeat_until,
                "meeting": meeting,
                "meeting_hosts": meeting_hosts,
                "meeting_meeting_admins": meeting_meeting_admins,
                "meeting_option": meeting_option,
                "meeting_option_password": meeting_option_password,
                "meeting_option_auto_record": meeting_option_auto_record,
                "meeting_option_enable_waiting_room": meeting_option_enable_waiting_room,
                "meeting_option_allow_enter_before_host": meeting_option_allow_enter_before_host,
                "meeting_option_enter_restraint": meeting_option_enter_restraint,
                "meeting_option_enable_screen_watermark": meeting_option_enable_screen_watermark,
                "meeting_option_enable_enter_mute": meeting_option_enable_enter_mute,
                "meeting_option_remind_scope": meeting_option_remind_scope,
                "meeting_option_water_mark_type": meeting_option_water_mark_type,
                "enable_id_trans": enable_id_trans,
            },
        )

    def exmail_app_get_email_alias(self) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/app/get_email_alias",
        )

    def exmail_app_read_mail(self, *, mail_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/app/read_mail",
            json_body={"mail_id": mail_id},
        )

    def exmail_group_create(
        self,
        *,
        groupid: str,
        groupname: str,
        email_list: str | None = None,
        tag_list: str | None = None,
        department_list: str | None = None,
        group_list: str | None = None,
        allow_type: str | None = None,
        allow_emaillist: str | None = None,
        allow_departmentlist: str | None = None,
        allow_taglist: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/group/create",
            json_body={
                "groupid": groupid,
                "groupname": groupname,
                "email_list": email_list,
                "tag_list": tag_list,
                "department_list": department_list,
                "group_list": group_list,
                "allow_type": allow_type,
                "allow_emaillist": allow_emaillist,
                "allow_departmentlist": allow_departmentlist,
                "allow_taglist": allow_taglist,
            },
        )

    def exmail_group_delete(self, *, groupid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/group/delete",
            json_body={"groupid": groupid},
        )

    def exmail_group_get(self, *, groupid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/exmail/group/get",
            query={"groupid": groupid},
        )

    def exmail_group_search(self, *, fuzzy: str, groupid: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/exmail/group/search",
            query={"fuzzy": fuzzy, "groupid": groupid},
        )

    def exmail_group_update(
        self,
        *,
        groupid: str,
        groupname: str | None = None,
        email_list: str | None = None,
        tag_list: str | None = None,
        department_list: str | None = None,
        group_list: str | None = None,
        allow_type: str | None = None,
        allow_emaillist: str | None = None,
        allow_departmentlist: str | None = None,
        allow_taglist: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/group/update",
            json_body={
                "groupid": groupid,
                "groupname": groupname,
                "email_list": email_list,
                "tag_list": tag_list,
                "department_list": department_list,
                "group_list": group_list,
                "allow_type": allow_type,
                "allow_emaillist": allow_emaillist,
                "allow_departmentlist": allow_departmentlist,
                "allow_taglist": allow_taglist,
            },
        )

    def exmail_useroption_update(self, *, userid: str, type: bool, value: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/exmail/useroption/update",
            json_body={"userid": userid, "type": type, "value": value},
        )

    def export_department(self, *, encoding_aeskey: str, block_size: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/export/department",
            json_body={"encoding_aeskey": encoding_aeskey, "block_size": block_size},
        )

    def export_get_result(self, *, jobid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/export/get_result",
            query={"jobid": jobid},
        )

    def export_simple_user(self, *, encoding_aeskey: str, block_size: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/export/simple_user",
            json_body={"encoding_aeskey": encoding_aeskey, "block_size": block_size},
        )

    def export_taguser(self, *, tagid: str, encoding_aeskey: str, block_size: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/export/taguser",
            json_body={"tagid": tagid, "encoding_aeskey": encoding_aeskey, "block_size": block_size},
        )

    def export_user(self, *, encoding_aeskey: str, block_size: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/export/user",
            json_body={"encoding_aeskey": encoding_aeskey, "block_size": block_size},
        )

    def externalpay_get_bill_list(
        self,
        *,
        begin_time: str,
        end_time: str,
        payee_userid: str | None = None,
        cursor: str | None = None,
        limit: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalpay/get_bill_list",
            json_body={
                "begin_time": begin_time,
                "end_time": end_time,
                "payee_userid": payee_userid,
                "cursor": cursor,
                "limit": limit,
            },
        )

    def externalpay_get_fund_flow(
        self,
        *,
        begin_time: str,
        end_time: str,
        mch_id: str | None = None,
        cursor: str | None = None,
        limit: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalpay/get_fund_flow",
            json_body={
                "begin_time": begin_time,
                "end_time": end_time,
                "mch_id": mch_id,
                "cursor": cursor,
                "limit": limit,
            },
        )

    def externalpay_getmerchant(self, *, mch_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/externalpay/getmerchant",
            json_body={"mch_id": mch_id},
        )

    def hardware_get_hardware_checkin_data(
        self, *, filter_type: str | None = None, starttime: str, endtime: str, useridlist: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/hardware/get_hardware_checkin_data",
            json_body={
                "filter_type": filter_type,
                "starttime": starttime,
                "endtime": endtime,
                "useridlist": useridlist,
            },
        )

    def health_get_health_report_stat(self, *, date: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/health/get_health_report_stat",
            json_body={"date": date},
        )

    def health_get_report_answer(
        self, *, jobid: str, date: str, offset: str | None = None, limit: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/health/get_report_answer",
            json_body={"jobid": jobid, "date": date, "offset": offset, "limit": limit},
        )

    def health_get_report_job_info(self, *, jobid: str, date: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/health/get_report_job_info",
            json_body={"jobid": jobid, "date": date},
        )

    def health_get_report_jobids(self, *, offset: str | None = None, limit: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/health/get_report_jobids",
            json_body={"offset": offset, "limit": limit},
        )

    def hr_get_fields(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/hr/get_fields",
        )

    def hr_get_staff_info(
        self,
        *,
        userid: str,
        get_all: bool | None = None,
        fieldids: str | None = None,
        fieldids_fieldid: str,
        fieldids_sub_idx: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/hr/get_staff_info",
            json_body={
                "userid": userid,
                "get_all": get_all,
                "fieldids": fieldids,
                "fieldids_fieldid": fieldids_fieldid,
                "fieldids_sub_idx": fieldids_sub_idx,
            },
        )

    def hr_update_staff_info(
        self,
        *,
        userid: str,
        update_items: str | None = None,
        remove_items: str | None = None,
        insert_items: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/hr/update_staff_info",
            json_body={
                "userid": userid,
                "update_items": update_items,
                "remove_items": remove_items,
                "insert_items": insert_items,
            },
        )

    def idconvert_convert_tmp_external_userid(
        self, *, business_type: int, user_type: int, tmp_external_userid_list: Any
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/idconvert/convert_tmp_external_userid",
            json_body={
                "business_type": business_type,
                "user_type": user_type,
                "tmp_external_userid_list": tmp_external_userid_list,
            },
        )

    def kf_account_add(self, *, name: str, media_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/account/add",
            json_body={"name": name, "media_id": media_id},
        )

    def kf_account_del(self, *, open_kfid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/account/del",
            json_body={"open_kfid": open_kfid},
        )

    def kf_get_corp_statistic(self, *, open_kfid: str, start_time: str, end_time: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/get_corp_statistic",
            json_body={"open_kfid": open_kfid, "start_time": start_time, "end_time": end_time},
        )

    def kf_get_servicer_statistic(
        self, *, open_kfid: str, servicer_userid: str | None = None, start_time: str, end_time: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/get_servicer_statistic",
            json_body={
                "open_kfid": open_kfid,
                "servicer_userid": servicer_userid,
                "start_time": start_time,
                "end_time": end_time,
            },
        )

    def kf_knowledge_add_group(self, *, name: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/knowledge/add_group",
            json_body={"name": name},
        )

    def kf_knowledge_add_intent(
        self,
        *,
        group_id: str,
        question: str,
        question_text: str,
        question_text_content: str,
        similar_questions: str | None = None,
        similar_questions_items: str | None = None,
        similar_questions_items_text: str,
        similar_questions_items_text_content: str,
        answers: str,
        answers_text: str,
        answers_text_content: str,
        answers_attachments: str | None = None,
        answers_attachments_1: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/knowledge/add_intent",
            json_body={
                "group_id": group_id,
                "question": question,
                "question_text": question_text,
                "question_text_content": question_text_content,
                "similar_questions": similar_questions,
                "similar_questions_items": similar_questions_items,
                "similar_questions_items_text": similar_questions_items_text,
                "similar_questions_items_text_content": similar_questions_items_text_content,
                "answers": answers,
                "answers_text": answers_text,
                "answers_text_content": answers_text_content,
                "answers_attachments": answers_attachments,
                "answers_attachments_1": answers_attachments_1,
            },
        )

    def kf_send_msg(
        self,
        *,
        touser: str | None = None,
        open_kfid: str | None = None,
        msgid: str | None = None,
        msgtype: str | None = None,
        text: Any | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/send_msg",
            json_body={"touser": touser, "open_kfid": open_kfid, "msgid": msgid, "msgtype": msgtype, "text": text},
        )

    def kf_send_msg_on_event(self, *, code: str, msgid: str | None = None, msgtype: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/send_msg_on_event",
            json_body={"code": code, "msgid": msgid, "msgtype": msgtype},
        )

    def kf_service_state_get(self, *, open_kfid: str, external_userid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/service_state/get",
            json_body={"open_kfid": open_kfid, "external_userid": external_userid},
        )

    def kf_sync_msg(
        self,
        *,
        cursor: str | None = None,
        token: str | None = None,
        limit: int | None = None,
        voice_format: str | None = None,
        open_kfid: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/kf/sync_msg",
            json_body={
                "cursor": cursor,
                "token": token,
                "limit": limit,
                "voice_format": voice_format,
                "open_kfid": open_kfid,
            },
        )

    def living_delete_replay_data(self, *, livingid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/living/delete_replay_data",
            json_body={"livingid": livingid},
        )

    def living_get_living_info(self, *, livingid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/living/get_living_info",
            query={"livingid": livingid},
        )

    def living_get_user_all_livingid(self, *, userid: str, cursor: str | None = None, limit: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/living/get_user_all_livingid",
            json_body={"userid": userid, "cursor": cursor, "limit": limit},
        )

    def meeting_cancel(self, *, meetingid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/cancel",
            json_body={"meetingid": meetingid},
        )

    def meeting_create(
        self,
        *,
        admin_userid: str,
        title: str,
        meeting_start: str,
        meeting_duration: str,
        description: str | None = None,
        location: str | None = None,
        agentid: str | None = None,
        invitees: str | None = None,
        invitees_userid: str | None = None,
        cal_id: str | None = None,
        settings: str | None = None,
        reminders: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/create",
            json_body={
                "admin_userid": admin_userid,
                "title": title,
                "meeting_start": meeting_start,
                "meeting_duration": meeting_duration,
                "description": description,
                "location": location,
                "agentid": agentid,
                "invitees": invitees,
                "invitees_userid": invitees_userid,
                "cal_id": cal_id,
                "settings": settings,
                "reminders": reminders,
            },
        )

    def meeting_create_customer_short_url(self, *, meetingid: str, customer_data: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/create_customer_short_url",
            json_body={"meetingid": meetingid, "customer_data": customer_data},
        )

    def meeting_enroll_approve(self, *, meetingid: str, action: str, enroll_id_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/enroll/approve",
            json_body={"meetingid": meetingid, "action": action, "enroll_id_list": enroll_id_list},
        )

    def meeting_enroll_delete(self, *, meetingid: str, enroll_id_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/enroll/delete",
            json_body={"meetingid": meetingid, "enroll_id_list": enroll_id_list},
        )

    def meeting_enroll_import(self, *, meetingid: str, enroll_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/enroll/import",
            json_body={"meetingid": meetingid, "enroll_list": enroll_list},
        )

    def meeting_enroll_set_config(
        self,
        *,
        meetingid: str,
        approve_type: str | None = None,
        is_collect_question: bool | None = None,
        question_list: str | None = None,
        no_registration_needed_for_staff: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/enroll/set_config",
            json_body={
                "meetingid": meetingid,
                "approve_type": approve_type,
                "is_collect_question": is_collect_question,
                "question_list": question_list,
                "no_registration_needed_for_staff": no_registration_needed_for_staff,
            },
        )

    def meeting_get_customer_short_url(self, *, meetingid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/get_customer_short_url",
            json_body={"meetingid": meetingid},
        )

    def meeting_get_info(self, *, meetingid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/get_info",
            json_body={"meetingid": meetingid},
        )

    def meeting_get_invitees(self, *, meetingid: str, cursor: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/get_invitees",
            json_body={"meetingid": meetingid, "cursor": cursor},
        )

    def meeting_get_user_meetingid(
        self,
        *,
        userid: str,
        cursor: str | None = None,
        limit: str | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/get_user_meetingid",
            json_body={
                "userid": userid,
                "cursor": cursor,
                "limit": limit,
                "begin_time": begin_time,
                "end_time": end_time,
            },
        )

    def meeting_layout_add_background(
        self, *, meetingid: str, image_list: str, default_image_order: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/layout/add_background",
            json_body={"meetingid": meetingid, "image_list": image_list, "default_image_order": default_image_order},
        )

    def meeting_layout_batch_delete_background(self, *, meetingid: str, background_id_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/layout/batch_delete_background",
            json_body={"meetingid": meetingid, "background_id_list": background_id_list},
        )

    def meeting_layout_delete_background(self, *, meetingid: str, background_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/layout/delete_background",
            json_body={"meetingid": meetingid, "background_id": background_id},
        )

    def meeting_layout_set_default(self, *, meetingid: str, selected_layout_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/layout/set_default",
            json_body={"meetingid": meetingid, "selected_layout_id": selected_layout_id},
        )

    def meeting_layout_set_default_background(self, *, meetingid: str, selected_background_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/layout/set_default_background",
            json_body={"meetingid": meetingid, "selected_background_id": selected_background_id},
        )

    def meeting_mra_set_default_layout(
        self, *, meetingid: str, default_layout: str, default_novideo_user: str, mra_tmp_openid: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/mra/set_default_layout",
            json_body={
                "meetingid": meetingid,
                "default_layout": default_layout,
                "default_novideo_user": default_novideo_user,
                "mra_tmp_openid": mra_tmp_openid,
            },
        )

    def meeting_mra_set_raise_hand(self, *, meetingid: str, raise_hand: bool, mra_tmp_openid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/mra/set_raise_hand",
            json_body={"meetingid": meetingid, "raise_hand": raise_hand, "mra_tmp_openid": mra_tmp_openid},
        )

    def meeting_phone_callout(self, *, meetingid: str, phone_numbers: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/phone/callout",
            json_body={"meetingid": meetingid, "phone_numbers": phone_numbers},
        )

    def meeting_poll_create_theme(
        self,
        *,
        operator_userid: str,
        instance_id: int,
        meetingid: str,
        poll_topic: str,
        poll_desc: str,
        is_anony: bool | None = None,
        poll_questions: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/poll/create_theme",
            json_body={
                "operator_userid": operator_userid,
                "instance_id": instance_id,
                "meetingid": meetingid,
                "poll_topic": poll_topic,
                "poll_desc": poll_desc,
                "is_anony": is_anony,
                "poll_questions": poll_questions,
            },
        )

    def meeting_poll_delete(
        self,
        *,
        operator_userid: str,
        instance_id: int,
        meetingid: str,
        poll_theme_id: str | None = None,
        poll_id: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/poll/delete",
            json_body={
                "operator_userid": operator_userid,
                "instance_id": instance_id,
                "meetingid": meetingid,
                "poll_theme_id": poll_theme_id,
                "poll_id": poll_id,
            },
        )

    def meeting_poll_finish(
        self, *, operator_userid: str, instance_id: int, meetingid: str, poll_theme_id: str, poll_id: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/poll/finish",
            json_body={
                "operator_userid": operator_userid,
                "instance_id": instance_id,
                "meetingid": meetingid,
                "poll_theme_id": poll_theme_id,
                "poll_id": poll_id,
            },
        )

    def meeting_poll_start(self, *, operator_userid: str, instance_id: int, meetingid: str, poll_theme_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/poll/start",
            json_body={
                "operator_userid": operator_userid,
                "instance_id": instance_id,
                "meetingid": meetingid,
                "poll_theme_id": poll_theme_id,
            },
        )

    def meeting_poll_update_theme(
        self,
        *,
        operator_userid: str,
        instance_id: int,
        meetingid: str,
        poll_theme_id: str,
        poll_topic: str,
        poll_desc: str,
        is_anony: bool | None = None,
        poll_questions: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/poll/update_theme",
            json_body={
                "operator_userid": operator_userid,
                "instance_id": instance_id,
                "meetingid": meetingid,
                "poll_theme_id": poll_theme_id,
                "poll_topic": poll_topic,
                "poll_desc": poll_desc,
                "is_anony": is_anony,
                "poll_questions": poll_questions,
            },
        )

    def meeting_realcontrol_dismiss(
        self, *, meetingid: str, force_dismiss: bool | None = None, retrieve_code: bool | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/realcontrol/dismiss",
            json_body={"meetingid": meetingid, "force_dismiss": force_dismiss, "retrieve_code": retrieve_code},
        )

    def meeting_record_delete(self, *, meeting_record_id: str, meetingid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/record/delete",
            json_body={"meeting_record_id": meeting_record_id, "meetingid": meetingid},
        )

    def meeting_record_delete_file(self, *, meetingid: str, record_file_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/record/delete_file",
            json_body={"meetingid": meetingid, "record_file_id": record_file_id},
        )

    def meeting_record_update_sharing_config(
        self, *, meeting_record_id: str, meetingid: str, sharing_config: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/record/update_sharing_config",
            json_body={
                "meeting_record_id": meeting_record_id,
                "meetingid": meetingid,
                "sharing_config": sharing_config,
            },
        )

    def meeting_statistics_get_start_list(
        self, *, type: int, begin_time: int, end_time: int, limit: int | None = None, cursor: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/statistics/get_start_list",
            json_body={"type": type, "begin_time": begin_time, "end_time": end_time, "limit": limit, "cursor": cursor},
        )

    def meeting_update(
        self,
        *,
        meetingid: str,
        title: str | None = None,
        meeting_start: str | None = None,
        meeting_duration: str | None = None,
        description: str | None = None,
        location: str | None = None,
        remind_time: str | None = None,
        agentid: str | None = None,
        invitees: str | None = None,
        invitees_userid: str | None = None,
        cal_id: str | None = None,
        settings: str | None = None,
        reminders: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/update",
            json_body={
                "meetingid": meetingid,
                "title": title,
                "meeting_start": meeting_start,
                "meeting_duration": meeting_duration,
                "description": description,
                "location": location,
                "remind_time": remind_time,
                "agentid": agentid,
                "invitees": invitees,
                "invitees_userid": invitees_userid,
                "cal_id": cal_id,
                "settings": settings,
                "reminders": reminders,
            },
        )

    def meeting_vip_list(self, *, cursor: str | None = None, limit: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/vip/list",
            json_body={"cursor": cursor, "limit": limit},
        )

    def meeting_vip_submit_batch_add_job(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/vip/submit_batch_add_job",
            json_body={"userid_list": userid_list},
        )

    def meeting_vip_submit_batch_del_job(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/vip/submit_batch_del_job",
            json_body={"userid_list": userid_list},
        )

    def meeting_waitingroom_get_current_user_list(
        self, *, meetingid: str, limit: str | None = None, cursor: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/waitingroom/get_current_user_list",
            json_body={"meetingid": meetingid, "limit": limit, "cursor": cursor},
        )

    def meeting_webinar_cancel(self, *, meetingid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/webinar/cancel",
            json_body={"meetingid": meetingid},
        )

    def meeting_webinar_create(
        self,
        *,
        admin_userid: str,
        title: str,
        sponsor: str | None = None,
        start_time: str,
        end_time: str,
        admission_type: str,
        hosts: str | None = None,
        password: str | None = None,
        cover_url: str | None = None,
        description: str | None = None,
        enable_guest_invite_link: bool | None = None,
        media_setting: str | None = None,
        enable_qa: bool | None = None,
        sensitive_words: str | None = None,
        enable_manual_check: bool | None = None,
        activity_page: bool | None = None,
        display_number_of_attendees: str | None = None,
        playback_for_audience: bool,
        preparation_mode: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/webinar/create",
            json_body={
                "admin_userid": admin_userid,
                "title": title,
                "sponsor": sponsor,
                "start_time": start_time,
                "end_time": end_time,
                "admission_type": admission_type,
                "hosts": hosts,
                "password": password,
                "cover_url": cover_url,
                "description": description,
                "enable_guest_invite_link": enable_guest_invite_link,
                "media_setting": media_setting,
                "enable_qa": enable_qa,
                "sensitive_words": sensitive_words,
                "enable_manual_check": enable_manual_check,
                "activity_page": activity_page,
                "display_number_of_attendees": display_number_of_attendees,
                "playback_for_audience": playback_for_audience,
                "preparation_mode": preparation_mode,
            },
        )

    def meeting_webinar_enroll_approve(self, *, meetingid: str, enroll_id_list: str, action: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/webinar/enroll/approve",
            json_body={"meetingid": meetingid, "enroll_id_list": enroll_id_list, "action": action},
        )

    def meeting_webinar_enroll_delete(self, *, meetingid: str, enroll_id_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/webinar/enroll/delete",
            json_body={"meetingid": meetingid, "enroll_id_list": enroll_id_list},
        )

    def meeting_webinar_enroll_import(self, *, meetingid: str, enroll_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/webinar/enroll/import",
            json_body={"meetingid": meetingid, "enroll_list": enroll_list},
        )

    def meeting_webinar_update(
        self,
        *,
        meetingid: str,
        title: str,
        sponsor: str | None = None,
        start_time: str,
        end_time: str,
        admission_type: str,
        hosts: str | None = None,
        password: str | None = None,
        cover_url: str | None = None,
        description: str | None = None,
        enable_guest_invite_link: bool | None = None,
        media_setting: str | None = None,
        enable_qa: bool | None = None,
        sensitive_words: str | None = None,
        enable_manual_check: bool | None = None,
        activity_page: bool | None = None,
        display_number_of_attendees: str | None = None,
        playback_for_audience: bool,
        preparation_mode: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/meeting/webinar/update",
            json_body={
                "meetingid": meetingid,
                "title": title,
                "sponsor": sponsor,
                "start_time": start_time,
                "end_time": end_time,
                "admission_type": admission_type,
                "hosts": hosts,
                "password": password,
                "cover_url": cover_url,
                "description": description,
                "enable_guest_invite_link": enable_guest_invite_link,
                "media_setting": media_setting,
                "enable_qa": enable_qa,
                "sensitive_words": sensitive_words,
                "enable_manual_check": enable_manual_check,
                "activity_page": activity_page,
                "display_number_of_attendees": display_number_of_attendees,
                "playback_for_audience": playback_for_audience,
                "preparation_mode": preparation_mode,
            },
        )

    def messages_send_text(
        self,
        *,
        to_user: str,
        agent_id: int,
        content: str,
        touser: str | None = None,
        toparty: str | None = None,
        totag: str | None = None,
        msgtype: str | None = None,
        agentid: int | None = None,
        text: Any | None = None,
        safe: int | None = None,
        enable_id_trans: int | None = None,
        enable_duplicate_check: int | None = None,
        duplicate_check_interval: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/message/send",
            json_body={
                "touser": to_user,
                "msgtype": "text",
                "agentid": agent_id,
                "text": {"content": content},
                "safe": 0,
                "toparty": toparty,
                "totag": totag,
                "enable_id_trans": enable_id_trans,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval,
            },
        )

    def messages_recall(self, *, msgid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/message/recall",
            json_body={"msgid": msgid},
        )

    def miniapppay_close_order(self, *, 商户号: str, 商户订单号: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/close_order",
            json_body={"商户号": 商户号, "商户订单号": 商户订单号},
        )

    def miniapppay_create_order(
        self,
        *,
        应用ID: str,
        商户号: str,
        商户订单号: str,
        商品描述: str,
        下单场景key: str | None = None,
        订单总金额: int,
        货币类型: str,
        支付者标识: str,
        交易结束时间: str | None = None,
        附加数据: str | None = None,
        订单优惠标记: str | None = None,
        订单原价: int | None = None,
        商品小票ID: str | None = None,
        商户侧商品编码: str,
        微信支付商品编码: str | None = None,
        商品名称: str | None = None,
        商品数量: int,
        商品单价: int,
        用户终端IP: str,
        商户端设备号: str | None = None,
        门店编号: str,
        门店名称: str | None = None,
        地区编码: str | None = None,
        详细地址: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/create_order",
            json_body={
                "应用ID": 应用ID,
                "商户号": 商户号,
                "商户订单号": 商户订单号,
                "商品描述": 商品描述,
                "下单场景key": 下单场景key,
                "订单总金额": 订单总金额,
                "货币类型": 货币类型,
                "支付者标识": 支付者标识,
                "交易结束时间": 交易结束时间,
                "附加数据": 附加数据,
                "订单优惠标记": 订单优惠标记,
                "订单原价": 订单原价,
                "商品小票ID": 商品小票ID,
                "商户侧商品编码": 商户侧商品编码,
                "微信支付商品编码": 微信支付商品编码,
                "商品名称": 商品名称,
                "商品数量": 商品数量,
                "商品单价": 商品单价,
                "用户终端IP": 用户终端IP,
                "商户端设备号": 商户端设备号,
                "门店编号": 门店编号,
                "门店名称": 门店名称,
                "地区编码": 地区编码,
                "详细地址": 详细地址,
            },
        )

    def miniapppay_get_applyment_status(self, *, out_request_no: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/get_applyment_status",
            json_body={"out_request_no": out_request_no},
        )

    def miniapppay_get_order(self, *, 商户号: str, 商户订单号: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/get_order",
            json_body={"商户号": 商户号, "商户订单号": 商户订单号},
        )

    def miniapppay_get_refund_detail(self, *, 商户号: str, 商户退款单号: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/get_refund_detail",
            json_body={"商户号": 商户号, "商户退款单号": 商户退款单号},
        )

    def miniapppay_get_sign(
        self, *, 应用ID: str, 预支付交易会话标识: str, 签名方式: str | None = None, 随机字符串: str, 时间戳: int
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/get_sign",
            json_body={
                "应用ID": 应用ID,
                "预支付交易会话标识": 预支付交易会话标识,
                "签名方式": 签名方式,
                "随机字符串": 随机字符串,
                "时间戳": 时间戳,
            },
        )

    def miniapppay_refund(
        self,
        *,
        商户号: str,
        商户APPID: str,
        商户订单号: str,
        商户退款单号: str,
        退款原因: str | None = None,
        订单金额: str,
        资金账户: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/refund",
            json_body={
                "商户号": 商户号,
                "商户APPID": 商户APPID,
                "商户订单号": 商户订单号,
                "商户退款单号": 商户退款单号,
                "退款原因": 退款原因,
                "订单金额": 订单金额,
                "资金账户": 资金账户,
            },
        )

    def miniapppay_upload_image(self) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniapppay/upload_image",
        )

    def miniprogram_transfer_session(self, *, userid: str, session_key: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/miniprogram/transfer_session",
            json_body={"userid": userid, "session_key": session_key},
        )

    def msgaudit_check_single_agree(self, *, info: str, userid: str, exteranalopenid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/msgaudit/check_single_agree",
            json_body={"info": info, "userid": userid, "exteranalopenid": exteranalopenid},
        )

    def msgaudit_get_permit_user_list(self, *, type: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/msgaudit/get_permit_user_list",
            json_body={"type": type},
        )

    def msgaudit_get_robot_info(
        self,
        *,
        msgid: str | None = None,
        action: str | None = None,
        from_: str | None = None,
        tolist: str | None = None,
        roomid: str | None = None,
        msgtime: str | None = None,
        msgtype: str | None = None,
        content: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/msgaudit/get_robot_info",
            query={
                "msgid": msgid,
                "action": action,
                "from_": from_,
                "tolist": tolist,
                "roomid": roomid,
                "msgtime": msgtime,
                "msgtype": msgtype,
                "content": content,
            },
        )

    def msgaudit_groupchat_get(self, *, roomid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/msgaudit/groupchat/get",
            json_body={"roomid": roomid},
        )

    def network_get_api_domain_ip(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/get_api_domain_ip",
        )

    def network_get_callback_ip(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/getcallbackip",
        )

    def oa_applyevent(
        self,
        *,
        creator_userid: str,
        template_id: str,
        use_template_approver: str,
        choose_department: str | None = None,
        apply_data: str,
        contents: str,
        control: str,
        id: str,
        value: str,
        summary_list: str,
        summary_info: str,
        text: str,
        lang: str,
        process: str | None = None,
        node_list: str,
        type: str,
        apv_rel: str | None = None,
        userid: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/applyevent",
            json_body={
                "creator_userid": creator_userid,
                "template_id": template_id,
                "use_template_approver": use_template_approver,
                "choose_department": choose_department,
                "apply_data": apply_data,
                "contents": contents,
                "control": control,
                "id": id,
                "value": value,
                "summary_list": summary_list,
                "summary_info": summary_info,
                "text": text,
                "lang": lang,
                "process": process,
                "node_list": node_list,
                "type": type,
                "apv_rel": apv_rel,
                "userid": userid,
            },
        )

    def oa_approval_create_template(
        self,
        *,
        template_name: str,
        text: str,
        lang: str,
        template_content: str,
        controls: str,
        property: str,
        control: str,
        id: str,
        title: str,
        text_1: str,
        lang_1: str,
        placeholder: str | None = None,
        text_2: str | None = None,
        lang_2: str | None = None,
        require: bool | None = None,
        un_print: bool | None = None,
        config: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/approval/create_template",
            json_body={
                "template_name": template_name,
                "text": text,
                "lang": lang,
                "template_content": template_content,
                "controls": controls,
                "property": property,
                "control": control,
                "id": id,
                "title": title,
                "text_1": text_1,
                "lang_1": lang_1,
                "placeholder": placeholder,
                "text_2": text_2,
                "lang_2": lang_2,
                "require": require,
                "un_print": un_print,
                "config": config,
            },
        )

    def oa_approval_update_template(
        self, *, template_id: str, template_name: str, text: str, lang: str, template_content: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/approval/update_template",
            json_body={
                "template_id": template_id,
                "template_name": template_name,
                "text": text,
                "lang": lang,
                "template_content": template_content,
            },
        )

    def oa_calendar_del(self, *, cal_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/calendar/del",
            json_body={"cal_id": cal_id},
        )

    def oa_calendar_get(self, *, cal_id_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/calendar/get",
            json_body={"cal_id_list": cal_id_list},
        )

    def oa_calendar_update(
        self,
        *,
        skip_public_range: bool | None = None,
        calendar: str,
        cal_id: str,
        admins: str | None = None,
        summary: str,
        color: str,
        description: str | None = None,
        public_range: str | None = None,
        public_range_userids: str | None = None,
        public_range_partyids: str | None = None,
        shares: str | None = None,
        shares_userid: str,
        shares_permission: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/calendar/update",
            json_body={
                "skip_public_range": skip_public_range,
                "calendar": calendar,
                "cal_id": cal_id,
                "admins": admins,
                "summary": summary,
                "color": color,
                "description": description,
                "public_range": public_range,
                "public_range_userids": public_range_userids,
                "public_range_partyids": public_range_partyids,
                "shares": shares,
                "shares_userid": shares_userid,
                "shares_permission": shares_permission,
            },
        )

    def oa_getapprovaldetail(self, *, sp_no: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/getapprovaldetail",
            json_body={"sp_no": sp_no},
        )

    def oa_getapprovalinfo(
        self,
        *,
        starttime: str,
        endtime: str,
        new_cursor: str,
        size: int,
        filters: str | None = None,
        key: str | None = None,
        value: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/getapprovalinfo",
            json_body={
                "starttime": starttime,
                "endtime": endtime,
                "new_cursor": new_cursor,
                "size": size,
                "filters": filters,
                "key": key,
                "value": value,
            },
        )

    def oa_gettemplatedetail(self, *, template_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/gettemplatedetail",
            json_body={"template_id": template_id},
        )

    def oa_journal_download_wedrive_file(self, *, journaluuid: str, fileid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/journal/download_wedrive_file",
            json_body={"journaluuid": journaluuid, "fileid": fileid},
        )

    def oa_journal_get_record_detail(self, *, journaluuid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/journal/get_record_detail",
            json_body={"journaluuid": journaluuid},
        )

    def oa_meetingroom_add(
        self,
        *,
        name: str,
        capacity: str,
        city: str | None = None,
        building: str | None = None,
        floor: str | None = None,
        equipment: str | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        range_user_list: str | None = None,
        range_department_list: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/meetingroom/add",
            json_body={
                "name": name,
                "capacity": capacity,
                "city": city,
                "building": building,
                "floor": floor,
                "equipment": equipment,
                "coordinate_latitude": coordinate_latitude,
                "coordinate_longitude": coordinate_longitude,
                "range_user_list": range_user_list,
                "range_department_list": range_department_list,
            },
        )

    def oa_meetingroom_get_booking_info(
        self,
        *,
        meetingroom_id: str | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        city: str | None = None,
        building: str | None = None,
        floor: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/meetingroom/get_booking_info",
            json_body={
                "meetingroom_id": meetingroom_id,
                "start_time": start_time,
                "end_time": end_time,
                "city": city,
                "building": building,
                "floor": floor,
            },
        )

    def oa_schedule_add_attendees(
        self, *, schedule_id: str, attendees: str | None = None, attendees_userid: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/schedule/add_attendees",
            json_body={"schedule_id": schedule_id, "attendees": attendees, "attendees_userid": attendees_userid},
        )

    def oa_schedule_del(
        self, *, schedule_id: str, op_mode: str | None = None, op_start_time: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/schedule/del",
            json_body={"schedule_id": schedule_id, "op_mode": op_mode, "op_start_time": op_start_time},
        )

    def oa_schedule_del_attendees(
        self, *, schedule_id: str, attendees: str | None = None, attendees_userid: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/schedule/del_attendees",
            json_body={"schedule_id": schedule_id, "attendees": attendees, "attendees_userid": attendees_userid},
        )

    def oa_schedule_get(self, *, schedule_id_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/schedule/get",
            json_body={"schedule_id_list": schedule_id_list},
        )

    def oa_schedule_get_by_calendar(self, *, cal_id: str, offset: str | None = None, limit: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/schedule/get_by_calendar",
            json_body={"cal_id": cal_id, "offset": offset, "limit": limit},
        )

    def oa_schedule_update(
        self,
        *,
        skip_attendees: bool | None = None,
        op_mode: str | None = None,
        op_start_time: str | None = None,
        schedule: str,
        schedule_schedule_id: str,
        schedule_admins: str | None = None,
        schedule_attendees: str | None = None,
        schedule_attendees_userid: str,
        schedule_summary: str | None = None,
        schedule_description: str | None = None,
        schedule_reminders: str | None = None,
        schedule_reminders_is_remind: bool | None = None,
        schedule_reminders_is_repeat: bool | None = None,
        schedule_reminders_remind_before_event_secs: str | None = None,
        schedule_reminders_remind_time_diffs: str | None = None,
        schedule_reminders_repeat_type: str | None = None,
        schedule_reminders_repeat_until: str | None = None,
        schedule_reminders_is_custom_repeat: bool | None = None,
        schedule_reminders_repeat_interval: str | None = None,
        schedule_reminders_repeat_day_of_week: str | None = None,
        schedule_reminders_repeat_day_of_month: str | None = None,
        schedule_reminders_timezone: str | None = None,
        schedule_location: str | None = None,
        schedule_start_time: str,
        schedule_end_time: str,
        schedule_is_whole_day: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/schedule/update",
            json_body={
                "skip_attendees": skip_attendees,
                "op_mode": op_mode,
                "op_start_time": op_start_time,
                "schedule": schedule,
                "schedule_schedule_id": schedule_schedule_id,
                "schedule_admins": schedule_admins,
                "schedule_attendees": schedule_attendees,
                "schedule_attendees_userid": schedule_attendees_userid,
                "schedule_summary": schedule_summary,
                "schedule_description": schedule_description,
                "schedule_reminders": schedule_reminders,
                "schedule_reminders_is_remind": schedule_reminders_is_remind,
                "schedule_reminders_is_repeat": schedule_reminders_is_repeat,
                "schedule_reminders_remind_before_event_secs": schedule_reminders_remind_before_event_secs,
                "schedule_reminders_remind_time_diffs": schedule_reminders_remind_time_diffs,
                "schedule_reminders_repeat_type": schedule_reminders_repeat_type,
                "schedule_reminders_repeat_until": schedule_reminders_repeat_until,
                "schedule_reminders_is_custom_repeat": schedule_reminders_is_custom_repeat,
                "schedule_reminders_repeat_interval": schedule_reminders_repeat_interval,
                "schedule_reminders_repeat_day_of_week": schedule_reminders_repeat_day_of_week,
                "schedule_reminders_repeat_day_of_month": schedule_reminders_repeat_day_of_month,
                "schedule_reminders_timezone": schedule_reminders_timezone,
                "schedule_location": schedule_location,
                "schedule_start_time": schedule_start_time,
                "schedule_end_time": schedule_end_time,
                "schedule_is_whole_day": schedule_is_whole_day,
            },
        )

    def oa_vacation_getuservacationquota(self, *, userid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/oa/vacation/getuservacationquota",
            json_body={"userid": userid},
        )

    def pstncc_call(self, *, callee_userid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/pstncc/call",
            json_body={"callee_userid": callee_userid},
        )

    def pstncc_getstates(self, *, callee_userid: str, callid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/pstncc/getstates",
            json_body={"callee_userid": callee_userid, "callid": callid},
        )

    def school_agent_get_allow_scope(self, *, agentid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/agent/get_allow_scope",
            query={"agentid": agentid},
        )

    def school_department_create(
        self,
        *,
        name: str | None = None,
        parentid: str,
        id: str | None = None,
        type: str,
        standard_grade: str | None = None,
        register_year: str | None = None,
        order: str | None = None,
        department_admins: str | None = None,
        department_admins_userid: str,
        department_admins_type: str,
        department_admins_subject: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/department/create",
            json_body={
                "name": name,
                "parentid": parentid,
                "id": id,
                "type": type,
                "standard_grade": standard_grade,
                "register_year": register_year,
                "order": order,
                "department_admins": department_admins,
                "department_admins_userid": department_admins_userid,
                "department_admins_type": department_admins_type,
                "department_admins_subject": department_admins_subject,
            },
        )

    def school_department_delete(self, *, id: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/department/delete",
            query={"id": id},
        )

    def school_department_list(self, *, id: str | None = None) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/department/list",
            query={"id": id},
        )

    def school_department_update(
        self,
        *,
        name: str | None = None,
        parentid: str | None = None,
        id: str,
        new_id: str | None = None,
        register_year: str | None = None,
        standard_grade: str | None = None,
        order: str | None = None,
        department_admins: str | None = None,
        department_admins_op: str,
        department_admins_userid: str,
        department_admins_type: str | None = None,
        department_admins_subject: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/department/update",
            json_body={
                "name": name,
                "parentid": parentid,
                "id": id,
                "new_id": new_id,
                "register_year": register_year,
                "standard_grade": standard_grade,
                "order": order,
                "department_admins": department_admins,
                "department_admins_op": department_admins_op,
                "department_admins_userid": department_admins_userid,
                "department_admins_type": department_admins_type,
                "department_admins_subject": department_admins_subject,
            },
        )

    def school_get_chat_create_mode(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/get_chat_create_mode",
        )

    def school_get_payment_result(self, *, payment_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/get_payment_result",
            json_body={"payment_id": payment_id},
        )

    def school_get_trade(self, *, payment_id: str, trade_no: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/get_trade",
            json_body={"payment_id": payment_id, "trade_no": trade_no},
        )

    def school_getuserinfo(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/getuserinfo",
        )

    def school_living_get_living_info(self, *, livingid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/living/get_living_info",
            query={"livingid": livingid},
        )

    def school_living_get_unwatch_stat(self, *, livingid: str, next_key: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/living/get_unwatch_stat",
            json_body={"livingid": livingid, "next_key": next_key},
        )

    def school_living_get_unwatch_stat_v2(self, *, livingid: str, next_cursor: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/living/get_unwatch_stat_v2",
            json_body={"livingid": livingid, "next_cursor": next_cursor},
        )

    def school_living_get_watch_stat(self, *, livingid: str, next_key: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/living/get_watch_stat",
            json_body={"livingid": livingid, "next_key": next_key},
        )

    def school_living_get_watch_stat_v2(self, *, livingid: str, next_cursor: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/living/get_watch_stat_v2",
            json_body={"livingid": livingid, "next_cursor": next_cursor},
        )

    def school_set_arch_sync_mode(self, *, arch_sync_mode: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/set_arch_sync_mode",
            json_body={"arch_sync_mode": arch_sync_mode},
        )

    def school_set_upgrade_info(self, *, upgrade_time: str | None = None, upgrade_switch: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/set_upgrade_info",
            json_body={"upgrade_time": upgrade_time, "upgrade_switch": upgrade_switch},
        )

    def school_user_batch_create_parent(
        self,
        *,
        parents: str,
        parents_parent_userid: str,
        parents_mobile: str,
        parents_to_invite: bool | None = None,
        parents_children: str,
        parents_children_student_userid: str,
        parents_children_relation: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/batch_create_parent",
            json_body={
                "parents": parents,
                "parents_parent_userid": parents_parent_userid,
                "parents_mobile": parents_mobile,
                "parents_to_invite": parents_to_invite,
                "parents_children": parents_children,
                "parents_children_student_userid": parents_children_student_userid,
                "parents_children_relation": parents_children_relation,
            },
        )

    def school_user_batch_create_student(
        self,
        *,
        students: str,
        students_student_userid: str,
        students_mobile: str | None = None,
        students_to_invite: bool | None = None,
        students_name: str,
        students_department: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/batch_create_student",
            json_body={
                "students": students,
                "students_student_userid": students_student_userid,
                "students_mobile": students_mobile,
                "students_to_invite": students_to_invite,
                "students_name": students_name,
                "students_department": students_department,
            },
        )

    def school_user_batch_delete_parent(self, *, useridlist: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/batch_delete_parent",
            json_body={"useridlist": useridlist},
        )

    def school_user_batch_delete_student(self, *, useridlist: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/batch_delete_student",
            json_body={"useridlist": useridlist},
        )

    def school_user_batch_update_parent(
        self,
        *,
        parents: str | None = None,
        parents_parent_userid: str,
        parents_new_parent_userid: str | None = None,
        parents_mobile: str | None = None,
        parents_children: str | None = None,
        parents_children_student_userid: str,
        parents_children_relation: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/batch_update_parent",
            json_body={
                "parents": parents,
                "parents_parent_userid": parents_parent_userid,
                "parents_new_parent_userid": parents_new_parent_userid,
                "parents_mobile": parents_mobile,
                "parents_children": parents_children,
                "parents_children_student_userid": parents_children_student_userid,
                "parents_children_relation": parents_children_relation,
            },
        )

    def school_user_batch_update_student(
        self,
        *,
        students: str | None = None,
        students_student_userid: str,
        students_mobile: str | None = None,
        students_new_student_userid: str | None = None,
        students_name: str | None = None,
        students_department: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/batch_update_student",
            json_body={
                "students": students,
                "students_student_userid": students_student_userid,
                "students_mobile": students_mobile,
                "students_new_student_userid": students_new_student_userid,
                "students_name": students_name,
                "students_department": students_department,
            },
        )

    def school_user_create_parent(
        self,
        *,
        parent_userid: str,
        mobile: str,
        to_invite: bool | None = None,
        children: str,
        children_student_userid: str,
        children_relation: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/create_parent",
            json_body={
                "parent_userid": parent_userid,
                "mobile": mobile,
                "to_invite": to_invite,
                "children": children,
                "children_student_userid": children_student_userid,
                "children_relation": children_relation,
            },
        )

    def school_user_create_student(
        self,
        *,
        student_userid: str,
        mobile: str | None = None,
        to_invite: bool | None = None,
        name: str,
        department: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/create_student",
            json_body={
                "student_userid": student_userid,
                "mobile": mobile,
                "to_invite": to_invite,
                "name": name,
                "department": department,
            },
        )

    def school_user_delete_parent(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/user/delete_parent",
            query={"userid": userid},
        )

    def school_user_delete_student(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/user/delete_student",
            query={"userid": userid},
        )

    def school_user_get(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/user/get",
            query={"userid": userid},
        )

    def school_user_list_parent(self, *, department_id: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/school/user/list_parent",
            query={"department_id": department_id},
        )

    def school_user_update_parent(
        self,
        *,
        parent_userid: str,
        new_parent_userid: str | None = None,
        mobile: str | None = None,
        children: str | None = None,
        children_student_userid: str,
        children_relation: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/update_parent",
            json_body={
                "parent_userid": parent_userid,
                "new_parent_userid": new_parent_userid,
                "mobile": mobile,
                "children": children,
                "children_student_userid": children_student_userid,
                "children_relation": children_relation,
            },
        )

    def school_user_update_student(
        self,
        *,
        student_userid: str,
        mobile: str | None = None,
        new_student_userid: str | None = None,
        name: str | None = None,
        department: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/school/user/update_student",
            json_body={
                "student_userid": student_userid,
                "mobile": mobile,
                "new_student_userid": new_student_userid,
                "name": name,
                "department": department,
            },
        )

    def security_admin_oper_log_list(
        self,
        *,
        start_time: str,
        end_time: str,
        oper_type: str | None = None,
        userid: str | None = None,
        cusor: str | None = None,
        limit: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/admin_oper_log/list",
            json_body={
                "start_time": start_time,
                "end_time": end_time,
                "oper_type": oper_type,
                "userid": userid,
                "cusor": cusor,
                "limit": limit,
            },
        )

    def security_get_screen_oper_record(
        self,
        *,
        start_time: int,
        end_time: int,
        userid_list: str | None = None,
        department_id_list: str | None = None,
        screen_shot_type: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/get_screen_oper_record",
            json_body={
                "start_time": start_time,
                "end_time": end_time,
                "userid_list": userid_list,
                "department_id_list": department_id_list,
                "screen_shot_type": screen_shot_type,
                "cursor": cursor,
                "limit": limit,
            },
        )

    def security_get_server_domain_ip(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/security/get_server_domain_ip",
        )

    def security_member_oper_log_list(
        self,
        *,
        start_time: str,
        end_time: str,
        oper_type: str | None = None,
        userid: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/member_oper_log/list",
            json_body={
                "start_time": start_time,
                "end_time": end_time,
                "oper_type": oper_type,
                "userid": userid,
                "cursor": cursor,
                "limit": limit,
            },
        )

    def security_trustdevice_import(
        self,
        *,
        device_list_system: str,
        device_list_mac_addr: str,
        device_list_motherboard_uuid: str | None = None,
        device_list_harddisk_uuid: str | None = None,
        device_list_domain: str | None = None,
        device_list_pc_name: str | None = None,
        device_list_seq_no: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/trustdevice/import",
            json_body={
                "device_list_system": device_list_system,
                "device_list_mac_addr": device_list_mac_addr,
                "device_list_motherboard_uuid": device_list_motherboard_uuid,
                "device_list_harddisk_uuid": device_list_harddisk_uuid,
                "device_list_domain": device_list_domain,
                "device_list_pc_name": device_list_pc_name,
                "device_list_seq_no": device_list_seq_no,
            },
        )

    def security_vip_list(self, *, cursor: str | None = None, limit: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/vip/list",
            json_body={"cursor": cursor, "limit": limit},
        )

    def security_vip_submit_batch_add_job(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/vip/submit_batch_add_job",
            json_body={"userid_list": userid_list},
        )

    def security_vip_submit_batch_del_job(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/security/vip/submit_batch_del_job",
            json_body={"userid_list": userid_list},
        )

    def tags_delete(self, *, tagid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/tag/delete",
            query={"tagid": tagid},
        )

    def tags_get(self, *, tagid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/tag/get",
            query={"tagid": tagid},
        )

    def tags_list(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/tag/list",
        )

    def tags_create(self, *, tagname: str, tagid: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/tag/create",
            json_body={"tagname": tagname, "tagid": tagid},
        )

    def tags_update(self, *, tagid: int, tagname: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/tag/update",
            json_body={"tagid": tagid, "tagname": tagname},
        )

    def tags_addtagusers(self, *, tagid: int, userlist: Any | None = None, partylist: Any | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/tag/addtagusers",
            json_body={"tagid": tagid, "userlist": userlist, "partylist": partylist},
        )

    def tags_deltagusers(self, *, tagid: int, userlist: Any | None = None, partylist: Any | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/tag/deltagusers",
            json_body={"tagid": tagid, "userlist": userlist, "partylist": partylist},
        )

    def ticket_get(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/ticket/get",
        )

    def unknown_cgi_bin_get_jsapi_ticket(self) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/get_jsapi_ticket",
        )

    def unknown_cgi_bin_get_launch_code(self, *, launch_code: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/get_launch_code",
            json_body={"launch_code": launch_code},
        )

    def users_authsucc(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/authsucc",
            query={"userid": userid},
        )

    def users_delete(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/delete",
            query={"userid": userid},
        )

    def users_get(self, *, userid: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/get",
            query={"userid": userid},
        )

    def users_list(self, *, department_id: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/list",
            query={"department_id": department_id},
        )

    def users_batchdelete(self, *, useridlist: Any) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/batchdelete",
            json_body={"useridlist": useridlist},
        )

    def users_convert_to_openid(self, *, userid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/convert_to_openid",
            json_body={"userid": userid},
        )

    def users_get_userid_by_email(self, *, email: str, email_type: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/get_userid_by_email",
            json_body={"email": email, "email_type": email_type},
        )

    def users_getuserid(self, *, mobile: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/getuserid",
            json_body={"mobile": mobile},
        )

    def users_list_id(self, *, cursor: str | None = None, limit: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/list_id",
            json_body={"cursor": cursor, "limit": limit},
        )

    def users_create(
        self,
        *,
        userid: str,
        name: str,
        alias: str | None = None,
        mobile: str | None = None,
        department: Any | None = None,
        order: Any | None = None,
        position: str | None = None,
        gender: str | None = None,
        email: str | None = None,
        biz_mail: str | None = None,
        telephone: str | None = None,
        is_leader_in_dept: Any | None = None,
        direct_leader: Any | None = None,
        avatar_mediaid: str | None = None,
        enable: int | None = None,
        extattr: Any | None = None,
        to_invite: Any | None = None,
        external_profile: Any | None = None,
        external_position: str | None = None,
        nickname: str | None = None,
        address: str | None = None,
        main_department: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/create",
            json_body={
                "userid": userid,
                "name": name,
                "alias": alias,
                "mobile": mobile,
                "department": department,
                "order": order,
                "position": position,
                "gender": gender,
                "email": email,
                "biz_mail": biz_mail,
                "telephone": telephone,
                "is_leader_in_dept": is_leader_in_dept,
                "direct_leader": direct_leader,
                "avatar_mediaid": avatar_mediaid,
                "enable": enable,
                "extattr": extattr,
                "to_invite": to_invite,
                "external_profile": external_profile,
                "external_position": external_position,
                "nickname": nickname,
                "address": address,
                "main_department": main_department,
            },
        )

    def users_update(
        self,
        *,
        userid: str,
        name: str | None = None,
        alias: str | None = None,
        mobile: str | None = None,
        department: Any | None = None,
        order: Any | None = None,
        position: str | None = None,
        gender: str | None = None,
        email: str | None = None,
        biz_mail: str | None = None,
        biz_mail_alias: Any | None = None,
        telephone: str | None = None,
        is_leader_in_dept: Any | None = None,
        direct_leader: Any | None = None,
        avatar_mediaid: str | None = None,
        enable: int | None = None,
        extattr: Any | None = None,
        external_profile: Any | None = None,
        external_position: str | None = None,
        nickname: str | None = None,
        address: str | None = None,
        main_department: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/user/update",
            json_body={
                "userid": userid,
                "name": name,
                "alias": alias,
                "mobile": mobile,
                "department": department,
                "order": order,
                "position": position,
                "gender": gender,
                "email": email,
                "biz_mail": biz_mail,
                "biz_mail_alias": biz_mail_alias,
                "telephone": telephone,
                "is_leader_in_dept": is_leader_in_dept,
                "direct_leader": direct_leader,
                "avatar_mediaid": avatar_mediaid,
                "enable": enable,
                "extattr": extattr,
                "external_profile": external_profile,
                "external_position": external_position,
                "nickname": nickname,
                "address": address,
                "main_department": main_department,
            },
        )

    def users_getuserinfo(self, *, appId: str, agentId: str, scopes: str) -> dict:
        return self._requester.request(
            method="GET",
            endpoint="/cgi-bin/user/getuserinfo",
            query={"appId": appId, "agentId": agentId, "scopes": scopes},
        )

    def wedoc_doc_share(self, *, docid: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/doc_share",
            json_body={"docid": docid},
        )

    def wedoc_document_batch_update(self, *, docid: str, version: str | None = None, requests: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/document/batch_update",
            json_body={"docid": docid, "version": version, "requests": requests},
        )

    def wedoc_document_get(self, *, docid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/document/get",
            json_body={"docid": docid},
        )

    def wedoc_get_doc_base_info(self, *, docid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/get_doc_base_info",
            json_body={"docid": docid},
        )

    def wedoc_get_form_answer(self, *, repeated_id: str, answer_ids: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/get_form_answer",
            json_body={"repeated_id": repeated_id, "answer_ids": answer_ids},
        )

    def wedoc_get_form_info(self, *, formid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/get_form_info",
            json_body={"formid": formid},
        )

    def wedoc_get_form_statistic(
        self,
        *,
        repeated_id: str,
        req_type: str,
        start_time: str | None = None,
        end_time: str | None = None,
        limit: str | None = None,
        cursor: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/get_form_statistic",
            json_body={
                "repeated_id": repeated_id,
                "req_type": req_type,
                "start_time": start_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
            },
        )

    def wedoc_image_upload(self, *, docid: str, base64_content: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/image_upload",
            json_body={"docid": docid, "base64_content": base64_content},
        )

    def wedoc_mod_doc_safty_setting(
        self,
        *,
        docid: str,
        enable_readonly_copy: bool | None = None,
        watermark: str | None = None,
        margin_type: str | None = None,
        show_visitor_name: bool | None = None,
        show_text: bool | None = None,
        text: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/mod_doc_safty_setting",
            json_body={
                "docid": docid,
                "enable_readonly_copy": enable_readonly_copy,
                "watermark": watermark,
                "margin_type": margin_type,
                "show_visitor_name": show_visitor_name,
                "show_text": show_text,
                "text": text,
            },
        )

    def wedoc_modify_form(
        self,
        *,
        oper: str,
        formid: str,
        form_title: str | None = None,
        form_desc: str | None = None,
        form_header: str | None = None,
        form_question: str | None = None,
        items: str,
        question_id: str,
        title: str,
        pos: str,
        status: str,
        reply_type: str,
        must_reply: bool,
        note: str | None = None,
        placeholder: str | None = None,
        question_extend_setting: str | None = None,
        option_item: str,
        key: str,
        value: str,
        status_1: str,
        form_setting: str | None = None,
        fill_out_auth: str,
        fill_in_range: str | None = None,
        userids: str | None = None,
        departmentids: str | None = None,
        setting_manager_range: str | None = None,
        timed_repeat_info: str | None = None,
        timed_repeat_info_enable: bool | None = None,
        timed_repeat_info_remind_time: str | None = None,
        timed_repeat_info_repeat_type: str | None = None,
        timed_repeat_info_week_flag: str | None = None,
        timed_repeat_info_skip_holiday: bool | None = None,
        timed_repeat_info_day_of_month: str | None = None,
        timed_repeat_info_fork_finish_type: bool | None = None,
        allow_multi_fill: bool | None = None,
        timed_finish: str | None = None,
        can_anonymous: bool | None = None,
        can_notify_submit: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/modify_form",
            json_body={
                "oper": oper,
                "formid": formid,
                "form_title": form_title,
                "form_desc": form_desc,
                "form_header": form_header,
                "form_question": form_question,
                "items": items,
                "question_id": question_id,
                "title": title,
                "pos": pos,
                "status": status,
                "reply_type": reply_type,
                "must_reply": must_reply,
                "note": note,
                "placeholder": placeholder,
                "question_extend_setting": question_extend_setting,
                "option_item": option_item,
                "key": key,
                "value": value,
                "status_1": status_1,
                "form_setting": form_setting,
                "fill_out_auth": fill_out_auth,
                "fill_in_range": fill_in_range,
                "userids": userids,
                "departmentids": departmentids,
                "setting_manager_range": setting_manager_range,
                "timed_repeat_info": timed_repeat_info,
                "timed_repeat_info_enable": timed_repeat_info_enable,
                "timed_repeat_info_remind_time": timed_repeat_info_remind_time,
                "timed_repeat_info_repeat_type": timed_repeat_info_repeat_type,
                "timed_repeat_info_week_flag": timed_repeat_info_week_flag,
                "timed_repeat_info_skip_holiday": timed_repeat_info_skip_holiday,
                "timed_repeat_info_day_of_month": timed_repeat_info_day_of_month,
                "timed_repeat_info_fork_finish_type": timed_repeat_info_fork_finish_type,
                "allow_multi_fill": allow_multi_fill,
                "timed_finish": timed_finish,
                "can_anonymous": can_anonymous,
                "can_notify_submit": can_notify_submit,
            },
        )

    def wedoc_smartsheet_add_field_group(
        self, *, docid: str, sheet_id: str, name: str, children: str | None = None, children_field_id: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/add_field_group",
            json_body={
                "docid": docid,
                "sheet_id": sheet_id,
                "name": name,
                "children": children,
                "children_field_id": children_field_id,
            },
        )

    def wedoc_smartsheet_add_fields(self, *, docid: str, sheet_id: str, fields: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/add_fields",
            json_body={"docid": docid, "sheet_id": sheet_id, "fields": fields},
        )

    def wedoc_smartsheet_add_records(
        self, *, docid: str, sheet_id: str, key_type: str | None = None, records: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/add_records",
            json_body={"docid": docid, "sheet_id": sheet_id, "key_type": key_type, "records": records},
        )

    def wedoc_smartsheet_add_sheet(
        self,
        *,
        docid: str,
        properties: str | None = None,
        properties_title: str | None = None,
        properties_index: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/add_sheet",
            json_body={
                "docid": docid,
                "properties": properties,
                "properties_title": properties_title,
                "properties_index": properties_index,
            },
        )

    def wedoc_smartsheet_add_view(
        self,
        *,
        docid: str,
        sheet_id: str,
        view_title: str,
        view_type: str,
        property_gantt: str | None = None,
        property_calendar: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/add_view",
            json_body={
                "docid": docid,
                "sheet_id": sheet_id,
                "view_title": view_title,
                "view_type": view_type,
                "property_gantt": property_gantt,
                "property_calendar": property_calendar,
            },
        )

    def wedoc_smartsheet_content_priv_get_sheet_priv(
        self, *, docid: str, type: str, rule_id_list: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/content_priv/get_sheet_priv",
            json_body={"docid": docid, "type": type, "rule_id_list": rule_id_list},
        )

    def wedoc_smartsheet_delete_field_groups(self, *, docid: str, sheet_id: str, field_group_ids: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/delete_field_groups",
            json_body={"docid": docid, "sheet_id": sheet_id, "field_group_ids": field_group_ids},
        )

    def wedoc_smartsheet_delete_fields(self, *, docid: str, sheet_id: str, field_ids: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/delete_fields",
            json_body={"docid": docid, "sheet_id": sheet_id, "field_ids": field_ids},
        )

    def wedoc_smartsheet_delete_records(self, *, docid: str, sheet_id: str, record_ids: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/delete_records",
            json_body={"docid": docid, "sheet_id": sheet_id, "record_ids": record_ids},
        )

    def wedoc_smartsheet_delete_sheet(self, *, docid: str, sheet_id: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/delete_sheet",
            json_body={"docid": docid, "sheet_id": sheet_id},
        )

    def wedoc_smartsheet_delete_views(self, *, docid: str, sheet_id: str, view_ids: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/delete_views",
            json_body={"docid": docid, "sheet_id": sheet_id, "view_ids": view_ids},
        )

    def wedoc_smartsheet_get_field_groups(
        self, *, docid: str, sheet_id: str, offset: str | None = None, limit: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/get_field_groups",
            json_body={"docid": docid, "sheet_id": sheet_id, "offset": offset, "limit": limit},
        )

    def wedoc_smartsheet_get_fields(
        self,
        *,
        docid: str,
        sheet_id: str,
        view_id: str | None = None,
        field_ids: str | None = None,
        field_titles: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/get_fields",
            json_body={
                "docid": docid,
                "sheet_id": sheet_id,
                "view_id": view_id,
                "field_ids": field_ids,
                "field_titles": field_titles,
                "offset": offset,
                "limit": limit,
            },
        )

    def wedoc_smartsheet_get_records(
        self,
        *,
        docid: str,
        sheet_id: str,
        view_id: str | None = None,
        record_ids: str | None = None,
        key_type: str | None = None,
        field_titles: str | None = None,
        field_ids: str | None = None,
        sort: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
        ver: str | None = None,
        filter_spec: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/get_records",
            json_body={
                "docid": docid,
                "sheet_id": sheet_id,
                "view_id": view_id,
                "record_ids": record_ids,
                "key_type": key_type,
                "field_titles": field_titles,
                "field_ids": field_ids,
                "sort": sort,
                "offset": offset,
                "limit": limit,
                "ver": ver,
                "filter_spec": filter_spec,
            },
        )

    def wedoc_smartsheet_get_sheet(
        self, *, docid: str, sheet_id: str | None = None, need_all_type_sheet: bool | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/get_sheet",
            json_body={"docid": docid, "sheet_id": sheet_id, "need_all_type_sheet": need_all_type_sheet},
        )

    def wedoc_smartsheet_get_views(
        self,
        *,
        docid: str,
        sheet_id: str,
        view_ids: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/get_views",
            json_body={"docid": docid, "sheet_id": sheet_id, "view_ids": view_ids, "offset": offset, "limit": limit},
        )

    def wedoc_smartsheet_update_field_group(
        self,
        *,
        docid: str,
        sheet_id: str,
        field_group_id: str,
        name: str | None = None,
        children: str | None = None,
        children_field_id: str | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/update_field_group",
            json_body={
                "docid": docid,
                "sheet_id": sheet_id,
                "field_group_id": field_group_id,
                "name": name,
                "children": children,
                "children_field_id": children_field_id,
            },
        )

    def wedoc_smartsheet_update_fields(self, *, docid: str, sheet_id: str, fields: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/update_fields",
            json_body={"docid": docid, "sheet_id": sheet_id, "fields": fields},
        )

    def wedoc_smartsheet_update_records(
        self, *, docid: str, sheet_id: str, key_type: str | None = None, records: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/update_records",
            json_body={"docid": docid, "sheet_id": sheet_id, "key_type": key_type, "records": records},
        )

    def wedoc_smartsheet_update_sheet(
        self, *, docid: str, properties_sheet_id: str, properties_title: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/update_sheet",
            json_body={
                "docid": docid,
                "properties_sheet_id": properties_sheet_id,
                "properties_title": properties_title,
            },
        )

    def wedoc_smartsheet_update_view(
        self, *, docid: str, sheet_id: str, view_id: str, view_title: str | None = None, property: str | None = None
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/smartsheet/update_view",
            json_body={
                "docid": docid,
                "sheet_id": sheet_id,
                "view_id": view_id,
                "view_title": view_title,
                "property": property,
            },
        )

    def wedoc_spreadsheet_batch_update(self, *, docid: str, requests: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/spreadsheet/batch_update",
            json_body={"docid": docid, "requests": requests},
        )

    def wedoc_spreadsheet_get_sheet_properties(self, *, docid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/spreadsheet/get_sheet_properties",
            json_body={"docid": docid},
        )

    def wedoc_spreadsheet_get_sheet_range_data(self, *, docid: str, sheet_id: str, range: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/spreadsheet/get_sheet_range_data",
            json_body={"docid": docid, "sheet_id": sheet_id, "range": range},
        )

    def wedoc_vip_batch_add(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/vip/batch_add",
            json_body={"userid_list": userid_list},
        )

    def wedoc_vip_batch_del(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/vip/batch_del",
            json_body={"userid_list": userid_list},
        )

    def wedoc_vip_list(self, *, cursor: str | None = None, limit: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedoc/vip/list",
            json_body={"cursor": cursor, "limit": limit},
        )

    def wedrive_file_acl_del(
        self, *, fileid: str, auth_info: str, type_后续将废弃: str, userid: str, departmentid_后续将废弃: str
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_acl_del",
            json_body={
                "fileid": fileid,
                "auth_info": auth_info,
                "type_后续将废弃": type_后续将废弃,
                "userid": userid,
                "departmentid_后续将废弃": departmentid_后续将废弃,
            },
        )

    def wedrive_file_create(self, *, spaceid: str, fatherid: str, file_type: str, file_name: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_create",
            json_body={"spaceid": spaceid, "fatherid": fatherid, "file_type": file_type, "file_name": file_name},
        )

    def wedrive_file_delete(self, *, fileid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_delete",
            json_body={"fileid": fileid},
        )

    def wedrive_file_download(self, *, fileid: str | None = None, selected_ticket: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_download",
            json_body={"fileid": fileid, "selected_ticket": selected_ticket},
        )

    def wedrive_file_info(self, *, fileid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_info",
            json_body={"fileid": fileid},
        )

    def wedrive_file_move(self, *, fatherid: str, replace: bool | None = None, fileid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_move",
            json_body={"fatherid": fatherid, "replace": replace, "fileid": fileid},
        )

    def wedrive_file_rename(self, *, fileid: str, new_name: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_rename",
            json_body={"fileid": fileid, "new_name": new_name},
        )

    def wedrive_file_secure_setting(
        self,
        *,
        fileid: str,
        text: str | None = None,
        margin_type: str | None = None,
        show_visitor_name: bool | None = None,
        show_text: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_secure_setting",
            json_body={
                "fileid": fileid,
                "text": text,
                "margin_type": margin_type,
                "show_visitor_name": show_visitor_name,
                "show_text": show_text,
            },
        )

    def wedrive_file_setting(self, *, fileid: str, auth_scope: str, auth: str | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_setting",
            json_body={"fileid": fileid, "auth_scope": auth_scope, "auth": auth},
        )

    def wedrive_file_share(self, *, fileid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_share",
            json_body={"fileid": fileid},
        )

    def wedrive_file_upload(
        self,
        *,
        spaceid: str | None = None,
        fatherid: str | None = None,
        selected_ticket: str | None = None,
        file_name: str,
        file_base64_content: str,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_upload",
            json_body={
                "spaceid": spaceid,
                "fatherid": fatherid,
                "selected_ticket": selected_ticket,
                "file_name": file_name,
                "file_base64_content": file_base64_content,
            },
        )

    def wedrive_file_upload_init(
        self,
        *,
        spaceid: str | None = None,
        fatherid: str | None = None,
        selected_ticket: str | None = None,
        file_name: str,
        size: str,
        block_sha: str,
        skip_push_card: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/file_upload_init",
            json_body={
                "spaceid": spaceid,
                "fatherid": fatherid,
                "selected_ticket": selected_ticket,
                "file_name": file_name,
                "size": size,
                "block_sha": block_sha,
                "skip_push_card": skip_push_card,
            },
        )

    def wedrive_get_file_permission(self, *, fileid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/get_file_permission",
            json_body={"fileid": fileid},
        )

    def wedrive_mng_pro_info(self) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/mng_pro_info",
        )

    def wedrive_new_space_info(self, *, spaceid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/new_space_info",
            json_body={"spaceid": spaceid},
        )

    def wedrive_space_acl_del(self, *, spaceid: str, auth_info: str, type: str, userid: str, departmentid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/space_acl_del",
            json_body={
                "spaceid": spaceid,
                "auth_info": auth_info,
                "type": type,
                "userid": userid,
                "departmentid": departmentid,
            },
        )

    def wedrive_space_dismiss(self, *, spaceid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/space_dismiss",
            json_body={"spaceid": spaceid},
        )

    def wedrive_space_info(self, *, spaceid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/space_info",
            json_body={"spaceid": spaceid},
        )

    def wedrive_space_rename(self, *, spaceid: str, space_name: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/space_rename",
            json_body={"spaceid": spaceid, "space_name": space_name},
        )

    def wedrive_space_setting(
        self,
        *,
        spaceid: str,
        enable_watermark: bool | None = None,
        enable_confidential_mode: bool | None = None,
        share_url_no_approve: bool | None = None,
        share_url_no_approve_default_auth: str | None = None,
        default_file_scope: str | None = None,
        ban_share_external: bool | None = None,
    ) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/space_setting",
            json_body={
                "spaceid": spaceid,
                "enable_watermark": enable_watermark,
                "enable_confidential_mode": enable_confidential_mode,
                "share_url_no_approve": share_url_no_approve,
                "share_url_no_approve_default_auth": share_url_no_approve_default_auth,
                "default_file_scope": default_file_scope,
                "ban_share_external": ban_share_external,
            },
        )

    def wedrive_space_share(self, *, spaceid: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/space_share",
            json_body={"spaceid": spaceid},
        )

    def wedrive_vip_batch_add(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/vip/batch_add",
            json_body={"userid_list": userid_list},
        )

    def wedrive_vip_batch_del(self, *, userid_list: str) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/vip/batch_del",
            json_body={"userid_list": userid_list},
        )

    def wedrive_vip_list(self, *, cursor: str | None = None, limit: int | None = None) -> dict:
        return self._requester.request(
            method="POST",
            endpoint="/cgi-bin/wedrive/vip/list",
            json_body={"cursor": cursor, "limit": limit},
        )
