"""Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT."""

from __future__ import annotations

import argparse
import json
from collections.abc import Callable

from apis.generated_client import GeneratedWeComClient

CommandHandler = Callable[[argparse.Namespace], dict]


def register_generated_commands(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    client: GeneratedWeComClient,
) -> dict[tuple[str, str], CommandHandler]:
    table: dict[tuple[str, str], CommandHandler] = {}

    auth_parser = subparsers.add_parser(
        'auth',
        help='auth 域命令',
    )
    auth_sub = auth_parser.add_subparsers(dest='action', required=True)

    auth_get_token_parser = auth_sub.add_parser(
        'get-token',
        help='获取access_token',
    )
    auth_get_token_parser.add_argument(
        '--corpid',
        type=str,
        required=True,
        help='企业ID，获取方式参考：术语说明-corpid',
    )
    auth_get_token_parser.add_argument(
        '--corpsecret',
        type=str,
        required=True,
        help='应用的凭证密钥，注意应用需要是启用状态，获取方式参考：术语说明-secret',
    )

    def _handle_auth_get_token(a: argparse.Namespace) -> dict:
        return client.auth_get_token(
            corpid=a.corpid,
            corpsecret=a.corpsecret,
        )
    table[('auth', 'get-token')] = _handle_auth_get_token

    batch_parser = subparsers.add_parser(
        'batch',
        help='batch 域命令',
    )
    batch_sub = batch_parser.add_subparsers(dest='action', required=True)

    batch_invite_parser = batch_sub.add_parser(
        'invite',
        help='邀请成员',
    )
    batch_invite_parser.add_argument(
        '--user',
        type=json.loads,
        help='成员ID列表, 最多支持1000个。',
    )
    batch_invite_parser.add_argument(
        '--party',
        type=json.loads,
        help='部门ID列表，最多支持100个。',
    )
    batch_invite_parser.add_argument(
        '--tag',
        type=json.loads,
        help='标签ID列表，最多支持100个。',
    )

    def _handle_batch_invite(a: argparse.Namespace) -> dict:
        return client.batch_invite(
            user=a.user,
            party=a.party,
            tag=a.tag,
        )
    table[('batch', 'invite')] = _handle_batch_invite

    batch_replaceparty_parser = batch_sub.add_parser(
        'replaceparty',
        help='全量覆盖部门',
    )
    batch_replaceparty_parser.add_argument(
        '--media-id',
        type=str,
        required=True,
        help='上传的csv文件的media_id',
    )
    batch_replaceparty_parser.add_argument(
        '--callback',
        type=json.loads,
        help='回调信息。如填写该项则任务完成后，通过callback推送事件给企业。具体请参考应用回调模式中的相应选项',
    )

    def _handle_batch_replaceparty(a: argparse.Namespace) -> dict:
        return client.batch_replaceparty(
            media_id=a.media_id,
            callback=a.callback,
        )
    table[('batch', 'replaceparty')] = _handle_batch_replaceparty

    batch_replaceuser_parser = batch_sub.add_parser(
        'replaceuser',
        help='全量覆盖成员',
    )
    batch_replaceuser_parser.add_argument(
        '--media-id',
        type=str,
        required=True,
        help='上传的csv文件的media_id',
    )
    batch_replaceuser_parser.add_argument(
        '--to-invite',
        type=json.loads,
        help='是否邀请新建的成员使用企业微信（将通过微信服务通知或短信或邮件下发邀请，每天自动下发一次，最多持续3个工作日），默认值为true。',
    )
    batch_replaceuser_parser.add_argument(
        '--callback',
        type=json.loads,
        help='回调信息。如填写该项则任务完成后，通过callback推送事件给企业。具体请参考应用回调模式中的相应选项',
    )

    def _handle_batch_replaceuser(a: argparse.Namespace) -> dict:
        return client.batch_replaceuser(
            media_id=a.media_id,
            to_invite=a.to_invite,
            callback=a.callback,
        )
    table[('batch', 'replaceuser')] = _handle_batch_replaceuser

    batch_syncuser_parser = batch_sub.add_parser(
        'syncuser',
        help='增量更新成员',
    )
    batch_syncuser_parser.add_argument(
        '--media-id',
        type=str,
        required=True,
        help='上传的csv文件的media_id',
    )
    batch_syncuser_parser.add_argument(
        '--to-invite',
        type=json.loads,
        help='是否邀请新建的成员使用企业微信（将通过微信服务通知或短信或邮件下发邀请，每天自动下发一次，最多持续3个工作日），默认值为true。',
    )
    batch_syncuser_parser.add_argument(
        '--callback',
        type=json.loads,
        help='回调信息。如填写该项则任务完成后，通过callback推送事件给企业。具体请参考应用回调模式中的相应选项',
    )

    def _handle_batch_syncuser(a: argparse.Namespace) -> dict:
        return client.batch_syncuser(
            media_id=a.media_id,
            to_invite=a.to_invite,
            callback=a.callback,
        )
    table[('batch', 'syncuser')] = _handle_batch_syncuser

    contacts_parser = subparsers.add_parser(
        'contacts',
        help='contacts 域命令',
    )
    contacts_sub = contacts_parser.add_subparsers(dest='action', required=True)

    contacts_list_users_parser = contacts_sub.add_parser(
        'list',
        help='列出成员',
    )
    contacts_list_users_parser.add_argument(
        '--department-id',
        type=int,
        default=1,
        help='部门 ID',
    )
    contacts_list_users_parser.add_argument(
        '--fetch-child',
        action='store_true',
        help='是否递归拉取子部门',
    )

    def _handle_contacts_list_users(a: argparse.Namespace) -> dict:
        return client.contacts_list_users(
            department_id=a.department_id,
            fetch_child=a.fetch_child,
        )
    table[('contacts', 'list')] = _handle_contacts_list_users

    corp_parser = subparsers.add_parser(
        'corp',
        help='corp 域命令',
    )
    corp_sub = corp_parser.add_subparsers(dest='action', required=True)

    corp_get_join_qrcode_parser = corp_sub.add_parser(
        'get-join-qrcode',
        help='获取加入企业二维码',
    )
    corp_get_join_qrcode_parser.add_argument(
        '--size-type',
        type=str,
        help='qrcode尺寸类型，1: 171 x 171; 2: 399 x 399; 3: 741 x 741; 4: 2052 x 2052',
    )

    def _handle_corp_get_join_qrcode(a: argparse.Namespace) -> dict:
        return client.corp_get_join_qrcode(
            size_type=a.size_type,
        )
    table[('corp', 'get-join-qrcode')] = _handle_corp_get_join_qrcode

    corp_opencorpid_to_corpid_parser = corp_sub.add_parser(
        'opencorpid-to-corpid',
        help='自建应用与第三方应用的对接',
    )
    corp_opencorpid_to_corpid_parser.add_argument(
        '--open-userid-list',
        type=json.loads,
        required=True,
        help='open_userid列表，最多不超过1000个。必须是source_agentid对应的应用所获取',
    )
    corp_opencorpid_to_corpid_parser.add_argument(
        '--source-agentid',
        type=int,
        required=True,
        help='企业授权的代开发自建应用或第三方应用的agentid',
    )

    def _handle_corp_opencorpid_to_corpid(a: argparse.Namespace) -> dict:
        return client.corp_opencorpid_to_corpid(
            open_userid_list=a.open_userid_list,
            source_agentid=a.source_agentid,
        )
    table[('corp', 'opencorpid-to-corpid')] = _handle_corp_opencorpid_to_corpid

    departments_parser = subparsers.add_parser(
        'departments',
        help='departments 域命令',
    )
    departments_sub = departments_parser.add_subparsers(dest='action', required=True)

    departments_delete_parser = departments_sub.add_parser(
        'delete',
        help='删除部门',
    )
    departments_delete_parser.add_argument(
        '--id',
        type=str,
        required=True,
        help='部门id。（注：不能删除根部门；不能删除含有子部门、成员的部门）',
    )

    def _handle_departments_delete(a: argparse.Namespace) -> dict:
        return client.departments_delete(
            id=a.id,
        )
    table[('departments', 'delete')] = _handle_departments_delete

    departments_get_parser = departments_sub.add_parser(
        'get',
        help='获取单个部门详情',
    )
    departments_get_parser.add_argument(
        '--id',
        type=str,
        required=True,
        help='部门id。',
    )

    def _handle_departments_get(a: argparse.Namespace) -> dict:
        return client.departments_get(
            id=a.id,
        )
    table[('departments', 'get')] = _handle_departments_get

    departments_list_parser = departments_sub.add_parser(
        'list',
        help='获取部门列表',
    )
    departments_list_parser.add_argument(
        '--id',
        type=str,
        help='部门id。获取指定部门及其下的子部门（以及子部门的子部门等等，递归）。 如果不填，默认获取全量组织架构',
    )

    def _handle_departments_list(a: argparse.Namespace) -> dict:
        return client.departments_list(
            id=a.id,
        )
    table[('departments', 'list')] = _handle_departments_list

    departments_list_ids_parser = departments_sub.add_parser(
        'list-ids',
        help='获取子部门ID列表',
    )
    departments_list_ids_parser.add_argument(
        '--id',
        type=str,
        help='部门id。获取指定部门及其下的子部门（以及子部门的子部门等等，递归）。 如果不填，默认获取全量组织架构',
    )

    def _handle_departments_list_ids(a: argparse.Namespace) -> dict:
        return client.departments_list_ids(
            id=a.id,
        )
    table[('departments', 'list-ids')] = _handle_departments_list_ids

    departments_create_parser = departments_sub.add_parser(
        'create',
        help='创建部门',
    )
    departments_create_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='部门名称。同一个层级的部门名称不能重复。长度限制为1~64个UTF-8字符，字符不能包括\\:*?"<>｜',
    )
    departments_create_parser.add_argument(
        '--name-en',
        type=str,
        help='英文名称。同一个层级的部门名称不能重复。需要在管理后台开启多语言支持才能生效。长度限制为1~64个字符，字符不能包括\\:*?"<>｜',
    )
    departments_create_parser.add_argument(
        '--parentid',
        type=int,
        required=True,
        help='父部门id，32位整型',
    )
    departments_create_parser.add_argument(
        '--order',
        type=int,
        help='在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)',
    )
    departments_create_parser.add_argument(
        '--id',
        type=int,
        help='部门id，32位整型，指定时必须大于1。若不填该参数，将自动生成id',
    )

    def _handle_departments_create(a: argparse.Namespace) -> dict:
        return client.departments_create(
            name=a.name,
            name_en=a.name_en,
            parentid=a.parentid,
            order=a.order,
            id=a.id,
        )
    table[('departments', 'create')] = _handle_departments_create

    departments_update_parser = departments_sub.add_parser(
        'update',
        help='更新部门',
    )
    departments_update_parser.add_argument(
        '--id',
        type=int,
        required=True,
        help='部门id',
    )
    departments_update_parser.add_argument(
        '--name',
        type=str,
        help='部门名称。长度限制为1~64个UTF-8字符，字符不能包括\\:*?"<>｜',
    )
    departments_update_parser.add_argument(
        '--name-en',
        type=str,
        help='英文名称，需要在管理后台开启多语言支持才能生效。长度限制为1~64个字符，字符不能包括\\:*?"<>｜',
    )
    departments_update_parser.add_argument(
        '--parentid',
        type=int,
        help='父部门id',
    )
    departments_update_parser.add_argument(
        '--order',
        type=int,
        help='在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)',
    )

    def _handle_departments_update(a: argparse.Namespace) -> dict:
        return client.departments_update(
            id=a.id,
            name=a.name,
            name_en=a.name_en,
            parentid=a.parentid,
            order=a.order,
        )
    table[('departments', 'update')] = _handle_departments_update

    idconvert_parser = subparsers.add_parser(
        'idconvert',
        help='idconvert 域命令',
    )
    idconvert_sub = idconvert_parser.add_subparsers(dest='action', required=True)

    idconvert_convert_tmp_external_userid_parser = idconvert_sub.add_parser(
        'convert-tmp-external-userid',
        help='tmp_external_userid的转换',
    )
    idconvert_convert_tmp_external_userid_parser.add_argument(
        '--business-type',
        type=int,
        required=True,
        help='业务类型。1-会议 2-收集表 3-智能表',
    )
    idconvert_convert_tmp_external_userid_parser.add_argument(
        '--user-type',
        type=int,
        required=True,
        help='转换的目标用户类型。1-客户 2-企业互联 3-上下游 4-互联企业（圈子） 详见上面关于user_type的说明',
    )
    idconvert_convert_tmp_external_userid_parser.add_argument(
        '--tmp-external-userid-list',
        type=json.loads,
        required=True,
        help='外部用户临时id，最多不超过100个',
    )

    def _handle_idconvert_convert_tmp_external_userid(a: argparse.Namespace) -> dict:
        return client.idconvert_convert_tmp_external_userid(
            business_type=a.business_type,
            user_type=a.user_type,
            tmp_external_userid_list=a.tmp_external_userid_list,
        )
    table[('idconvert', 'convert-tmp-external-userid')] = _handle_idconvert_convert_tmp_external_userid

    messages_parser = subparsers.add_parser(
        'messages',
        help='messages 域命令',
    )
    messages_sub = messages_parser.add_subparsers(dest='action', required=True)

    messages_send_text_parser = messages_sub.add_parser(
        'send-text',
        help='发送文本消息',
    )
    messages_send_text_parser.add_argument(
        '--to-user',
        type=str,
        required=True,
        help='接收者用户 ID',
    )
    messages_send_text_parser.add_argument(
        '--agent-id',
        type=int,
        required=True,
        help='应用 agent id',
    )
    messages_send_text_parser.add_argument(
        '--content',
        type=str,
        required=True,
        help='文本内容',
    )

    def _handle_messages_send_text(a: argparse.Namespace) -> dict:
        return client.messages_send_text(
            to_user=a.to_user,
            agent_id=a.agent_id,
            content=a.content,
        )
    table[('messages', 'send-text')] = _handle_messages_send_text

    network_parser = subparsers.add_parser(
        'network',
        help='network 域命令',
    )
    network_sub = network_parser.add_subparsers(dest='action', required=True)

    network_sub.add_parser(
        'get-api-domain-ip',
        help='获取企业微信接口IP段',
    )

    def _handle_network_get_api_domain_ip(a: argparse.Namespace) -> dict:
        return client.network_get_api_domain_ip()
    table[('network', 'get-api-domain-ip')] = _handle_network_get_api_domain_ip

    network_sub.add_parser(
        'get-callback-ip',
        help='获取企业微信回调IP段',
    )

    def _handle_network_get_callback_ip(a: argparse.Namespace) -> dict:
        return client.network_get_callback_ip()
    table[('network', 'get-callback-ip')] = _handle_network_get_callback_ip

    tags_parser = subparsers.add_parser(
        'tags',
        help='tags 域命令',
    )
    tags_sub = tags_parser.add_subparsers(dest='action', required=True)

    tags_delete_parser = tags_sub.add_parser(
        'delete',
        help='删除标签',
    )
    tags_delete_parser.add_argument(
        '--tagid',
        type=str,
        required=True,
        help='标签ID',
    )

    def _handle_tags_delete(a: argparse.Namespace) -> dict:
        return client.tags_delete(
            tagid=a.tagid,
        )
    table[('tags', 'delete')] = _handle_tags_delete

    tags_get_parser = tags_sub.add_parser(
        'get',
        help='获取标签成员',
    )
    tags_get_parser.add_argument(
        '--tagid',
        type=str,
        required=True,
        help='标签ID',
    )

    def _handle_tags_get(a: argparse.Namespace) -> dict:
        return client.tags_get(
            tagid=a.tagid,
        )
    table[('tags', 'get')] = _handle_tags_get

    tags_sub.add_parser(
        'list',
        help='获取标签列表',
    )

    def _handle_tags_list(a: argparse.Namespace) -> dict:
        return client.tags_list()
    table[('tags', 'list')] = _handle_tags_list

    tags_create_parser = tags_sub.add_parser(
        'create',
        help='创建标签',
    )
    tags_create_parser.add_argument(
        '--tagname',
        type=str,
        required=True,
        help='标签名称，长度限制为32个字以内（汉字或英文字母），标签名不可与其他标签重名。',
    )
    tags_create_parser.add_argument(
        '--tagid',
        type=int,
        help='标签id，非负整型，指定此参数时新增的标签会生成对应的标签id，不指定时则以目前最大的id自增。',
    )

    def _handle_tags_create(a: argparse.Namespace) -> dict:
        return client.tags_create(
            tagname=a.tagname,
            tagid=a.tagid,
        )
    table[('tags', 'create')] = _handle_tags_create

    tags_update_parser = tags_sub.add_parser(
        'update',
        help='更新标签名字',
    )
    tags_update_parser.add_argument(
        '--tagid',
        type=int,
        required=True,
        help='标签ID',
    )
    tags_update_parser.add_argument(
        '--tagname',
        type=str,
        required=True,
        help='标签名称，长度限制为32个字（汉字或英文字母），标签不可与其他标签重名。',
    )

    def _handle_tags_update(a: argparse.Namespace) -> dict:
        return client.tags_update(
            tagid=a.tagid,
            tagname=a.tagname,
        )
    table[('tags', 'update')] = _handle_tags_update

    tags_addtagusers_parser = tags_sub.add_parser(
        'addtagusers',
        help='增加标签成员',
    )
    tags_addtagusers_parser.add_argument(
        '--tagid',
        type=int,
        required=True,
        help='标签ID',
    )
    tags_addtagusers_parser.add_argument(
        '--userlist',
        type=json.loads,
        help='企业成员ID列表，注意：userlist、partylist不能同时为空，单次请求个数不超过1000',
    )
    tags_addtagusers_parser.add_argument(
        '--partylist',
        type=json.loads,
        help='企业部门ID列表，注意：userlist、partylist不能同时为空，单次请求个数不超过100',
    )

    def _handle_tags_addtagusers(a: argparse.Namespace) -> dict:
        return client.tags_addtagusers(
            tagid=a.tagid,
            userlist=a.userlist,
            partylist=a.partylist,
        )
    table[('tags', 'addtagusers')] = _handle_tags_addtagusers

    tags_deltagusers_parser = tags_sub.add_parser(
        'deltagusers',
        help='删除标签成员',
    )
    tags_deltagusers_parser.add_argument(
        '--tagid',
        type=int,
        required=True,
        help='标签ID',
    )
    tags_deltagusers_parser.add_argument(
        '--userlist',
        type=json.loads,
        help='企业成员ID列表，注意：userlist、partylist不能同时为空，单次请求长度不超过1000',
    )
    tags_deltagusers_parser.add_argument(
        '--partylist',
        type=json.loads,
        help='企业部门ID列表，注意：userlist、partylist不能同时为空，单次请求长度不超过100',
    )

    def _handle_tags_deltagusers(a: argparse.Namespace) -> dict:
        return client.tags_deltagusers(
            tagid=a.tagid,
            userlist=a.userlist,
            partylist=a.partylist,
        )
    table[('tags', 'deltagusers')] = _handle_tags_deltagusers

    users_parser = subparsers.add_parser(
        'users',
        help='users 域命令',
    )
    users_sub = users_parser.add_subparsers(dest='action', required=True)

    users_authsucc_parser = users_sub.add_parser(
        'authsucc',
        help='登录二次验证',
    )
    users_authsucc_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员UserID。对应管理端的账号',
    )

    def _handle_users_authsucc(a: argparse.Namespace) -> dict:
        return client.users_authsucc(
            userid=a.userid,
        )
    table[('users', 'authsucc')] = _handle_users_authsucc

    users_delete_parser = users_sub.add_parser(
        'delete',
        help='删除成员',
    )
    users_delete_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员UserID。对应管理端的账号',
    )

    def _handle_users_delete(a: argparse.Namespace) -> dict:
        return client.users_delete(
            userid=a.userid,
        )
    table[('users', 'delete')] = _handle_users_delete

    users_get_parser = users_sub.add_parser(
        'get',
        help='读取成员',
    )
    users_get_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员UserID。对应管理端的账号，企业内必须唯一。不区分大小写，长度为1~64个字节',
    )

    def _handle_users_get(a: argparse.Namespace) -> dict:
        return client.users_get(
            userid=a.userid,
        )
    table[('users', 'get')] = _handle_users_get

    users_list_parser = users_sub.add_parser(
        'list',
        help='获取部门成员详情',
    )
    users_list_parser.add_argument(
        '--department-id',
        type=str,
        required=True,
        help='获取的部门id',
    )

    def _handle_users_list(a: argparse.Namespace) -> dict:
        return client.users_list(
            department_id=a.department_id,
        )
    table[('users', 'list')] = _handle_users_list

    users_batchdelete_parser = users_sub.add_parser(
        'batchdelete',
        help='批量删除成员',
    )
    users_batchdelete_parser.add_argument(
        '--useridlist',
        type=json.loads,
        required=True,
        help='成员UserID列表。对应管理端的账号。最多支持200个。若存在无效UserID，直接返回错误',
    )

    def _handle_users_batchdelete(a: argparse.Namespace) -> dict:
        return client.users_batchdelete(
            useridlist=a.useridlist,
        )
    table[('users', 'batchdelete')] = _handle_users_batchdelete

    users_convert_to_openid_parser = users_sub.add_parser(
        'convert-to-openid',
        help='userid与openid互换',
    )
    users_convert_to_openid_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='企业内的成员id',
    )

    def _handle_users_convert_to_openid(a: argparse.Namespace) -> dict:
        return client.users_convert_to_openid(
            userid=a.userid,
        )
    table[('users', 'convert-to-openid')] = _handle_users_convert_to_openid

    users_get_userid_by_email_parser = users_sub.add_parser(
        'get-userid-by-email',
        help='邮箱获取userid',
    )
    users_get_userid_by_email_parser.add_argument(
        '--email',
        type=str,
        required=True,
        help='邮箱',
    )
    users_get_userid_by_email_parser.add_argument(
        '--email-type',
        type=int,
        help='邮箱类型：1-企业邮箱（默认）；2-个人邮箱',
    )

    def _handle_users_get_userid_by_email(a: argparse.Namespace) -> dict:
        return client.users_get_userid_by_email(
            email=a.email,
            email_type=a.email_type,
        )
    table[('users', 'get-userid-by-email')] = _handle_users_get_userid_by_email

    users_getuserid_parser = users_sub.add_parser(
        'getuserid',
        help='手机号获取userid',
    )
    users_getuserid_parser.add_argument(
        '--mobile',
        type=str,
        required=True,
        help='用户在企业微信通讯录中的手机号码。长度为5~32个字节',
    )

    def _handle_users_getuserid(a: argparse.Namespace) -> dict:
        return client.users_getuserid(
            mobile=a.mobile,
        )
    table[('users', 'getuserid')] = _handle_users_getuserid

    users_list_id_parser = users_sub.add_parser(
        'list-id',
        help='获取成员ID列表',
    )
    users_list_id_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用不填',
    )
    users_list_id_parser.add_argument(
        '--limit',
        type=int,
        help='分页，预期请求的数据量，取值范围 1 ~ 10000',
    )

    def _handle_users_list_id(a: argparse.Namespace) -> dict:
        return client.users_list_id(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('users', 'list-id')] = _handle_users_list_id

    users_create_parser = users_sub.add_parser(
        'create',
        help='创建成员',
    )
    users_create_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员UserID。对应管理端的账号，企业内必须唯一。长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。系统进行唯一性检查时会忽略大小写。',
    )
    users_create_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='成员名称。长度为1~64个utf8字符',
    )
    users_create_parser.add_argument(
        '--alias',
        type=str,
        help='成员别名。长度1~64个utf8字符',
    )
    users_create_parser.add_argument(
        '--mobile',
        type=str,
        help='手机号码。企业内必须唯一，mobile/email二者不能同时为空 ，中国大陆手机号码可省略“+86”，其他国家或地区必须要带上国际码。',
    )
    users_create_parser.add_argument(
        '--department',
        type=json.loads,
        help='成员所属部门id列表，不超过100个。当不填写department或id为0时，成员会放在其他（待设置部门）下，当填写的部门不存在时，会在在其他（待设置部门）下新建对应部门',
    )
    users_create_parser.add_argument(
        '--order',
        type=json.loads,
        help='部门内的排序值，默认为0，成员次序以创建时间从小到大排列。个数必须和参数department的个数一致，数值越大排序越前面。有效的值范围是[0, 2^32)',
    )
    users_create_parser.add_argument(
        '--position',
        type=str,
        help='职务信息。长度为0~128个字符',
    )
    users_create_parser.add_argument(
        '--gender',
        type=str,
        help='性别。1表示男性，2表示女性',
    )
    users_create_parser.add_argument(
        '--email',
        type=str,
        help='邮箱。可填写企业已有的邮箱账号，方便同事获取成员的邮箱账号以发邮件。长度6~64个字节，且为有效的email格式。企业内必须唯一，mobile/email二者不能同时为空。境外成员可用此邮箱登录企业微信。',
    )
    users_create_parser.add_argument(
        '--biz-mail',
        type=str,
        help='如果企业已开通腾讯企业邮（企业微信邮箱），设置该值可创建企业邮箱账号。长度6~64个字节，且为有效的企业邮箱格式。企业内必须唯一。未填写则系统会为用户生成默认企业邮箱（由系统生成的邮箱可修改一次）',
    )
    users_create_parser.add_argument(
        '--telephone',
        type=str,
        help='座机。32字节以内，由纯数字、“-”、“+”或“,”组成。',
    )
    users_create_parser.add_argument(
        '--is-leader-in-dept',
        type=json.loads,
        help='个数必须和参数department的个数一致，表示在所在的部门内是否为部门负责人。1表示为部门负责人，0表示非部门负责人。在审批(自建、第三方)等应用里可以用来标识上级审批人',
    )
    users_create_parser.add_argument(
        '--direct-leader',
        type=json.loads,
        help='直属上级UserID，设置范围为企业内成员，可以设置最多1个上级',
    )
    users_create_parser.add_argument(
        '--avatar-mediaid',
        type=str,
        help='成员头像的mediaid，通过素材管理接口上传图片获得的mediaid',
    )
    users_create_parser.add_argument(
        '--enable',
        type=int,
        help='启用/禁用成员。1表示启用成员，0表示禁用成员',
    )
    users_create_parser.add_argument(
        '--extattr',
        type=json.loads,
        help='扩展属性。扩展属性字段需要先在WEB管理端添加，见扩展属性添加方法，否则忽略未知属性的赋值。字段详情见成员扩展属性',
    )
    users_create_parser.add_argument(
        '--to-invite',
        type=json.loads,
        help='是否邀请该成员使用企业微信（将通过微信服务通知或短信或邮件下发邀请，每天自动下发一次，最多持续3个工作日），默认值为true。',
    )
    users_create_parser.add_argument(
        '--external-profile',
        type=json.loads,
        help='成员对外属性，字段详情见对外属性',
    )
    users_create_parser.add_argument(
        '--external-position',
        type=str,
        help='对外职务，如果设置了该值，则以此作为对外展示的职务，否则以position来展示。长度12个汉字内',
    )
    users_create_parser.add_argument(
        '--nickname',
        type=str,
        help='视频号名字（设置后，成员将对外展示该视频号）。须从企业绑定到企业微信的视频号中选择，可在“我的企业”页中查看绑定的视频号',
    )
    users_create_parser.add_argument(
        '--address',
        type=str,
        help='地址。长度最大128个字符',
    )
    users_create_parser.add_argument(
        '--main-department',
        type=int,
        help='主部门',
    )

    def _handle_users_create(a: argparse.Namespace) -> dict:
        return client.users_create(
            userid=a.userid,
            name=a.name,
            alias=a.alias,
            mobile=a.mobile,
            department=a.department,
            order=a.order,
            position=a.position,
            gender=a.gender,
            email=a.email,
            biz_mail=a.biz_mail,
            telephone=a.telephone,
            is_leader_in_dept=a.is_leader_in_dept,
            direct_leader=a.direct_leader,
            avatar_mediaid=a.avatar_mediaid,
            enable=a.enable,
            extattr=a.extattr,
            to_invite=a.to_invite,
            external_profile=a.external_profile,
            external_position=a.external_position,
            nickname=a.nickname,
            address=a.address,
            main_department=a.main_department,
        )
    table[('users', 'create')] = _handle_users_create

    users_update_parser = users_sub.add_parser(
        'update',
        help='更新成员',
    )
    users_update_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员UserID。对应管理端的账号，企业内必须唯一。不区分大小写，长度为1~64个字节',
    )
    users_update_parser.add_argument(
        '--name',
        type=str,
        help='成员名称。长度为1~64个utf8字符',
    )
    users_update_parser.add_argument(
        '--alias',
        type=str,
        help='别名。长度为1-64个utf8字符',
    )
    users_update_parser.add_argument(
        '--mobile',
        type=str,
        help='手机号码。企业内必须唯一。若成员已激活企业微信，则需成员自行修改（此情况下该参数被忽略，但不会报错） ，中国大陆手机号码可省略“+86”，其他国家或地区必须要带上国际码。',
    )
    users_update_parser.add_argument(
        '--department',
        type=json.loads,
        help='成员所属部门id列表，不超过100个',
    )
    users_update_parser.add_argument(
        '--order',
        type=json.loads,
        help='部门内的排序值，默认为0。当有传入department时有效。数量必须和department一致，数值越大排序越前面。有效的值范围是[0, 2^32)',
    )
    users_update_parser.add_argument(
        '--position',
        type=str,
        help='职务信息。长度为0~128个utf8字符',
    )
    users_update_parser.add_argument(
        '--gender',
        type=str,
        help='性别。1表示男性，2表示女性',
    )
    users_update_parser.add_argument(
        '--email',
        type=str,
        help='邮箱。可填写企业已有的邮箱账号，方便同事获取成员的邮箱账号以发邮件。长度6~64个字节，且为有效的email格式。企业内必须唯一。境外成员可用此邮箱登录企业微信。',
    )
    users_update_parser.add_argument(
        '--biz-mail',
        type=str,
        help='如果企业已开通腾讯企业邮（企业微信邮箱），设置该值可创建企业邮箱账号。长度6~63个字节，且为有效的企业邮箱格式。企业内必须唯一。未填写则系统会为用户生成默认企业邮箱（由系统生成的邮箱可修改一次）。',
    )
    users_update_parser.add_argument(
        '--biz-mail-alias',
        type=json.loads,
        help='企业邮箱别名。长度6~63个字节，且为有效的企业邮箱格式。企业内必须唯一，最多可设置5个别名。更新时为覆盖式更新。传空结构或传空数组会清空当前企业邮箱别名。',
    )
    users_update_parser.add_argument(
        '--telephone',
        type=str,
        help='座机。由1-32位的纯数字、“-”、“+”或“,”组成',
    )
    users_update_parser.add_argument(
        '--is-leader-in-dept',
        type=json.loads,
        help='部门负责人字段，个数必须和department一致，表示在所在的部门内是否为负责人。0-否，1-是',
    )
    users_update_parser.add_argument(
        '--direct-leader',
        type=json.loads,
        help='直属上级，可以设置企业范围内成员为直属上级，最多设置1个',
    )
    users_update_parser.add_argument(
        '--avatar-mediaid',
        type=str,
        help='成员头像的mediaid，通过素材管理接口上传图片获得的mediaid',
    )
    users_update_parser.add_argument(
        '--enable',
        type=int,
        help='启用/禁用成员。1表示启用成员，0表示禁用成员',
    )
    users_update_parser.add_argument(
        '--extattr',
        type=json.loads,
        help='扩展属性。扩展属性字段需要先在WEB管理端添加，见扩展属性添加方法，否则忽略未知属性的赋值。字段详情见成员扩展属性',
    )
    users_update_parser.add_argument(
        '--external-profile',
        type=json.loads,
        help='成员对外属性，字段详情见对外属性',
    )
    users_update_parser.add_argument(
        '--external-position',
        type=str,
        help='对外职务，如果设置了该值，则以此作为对外展示的职务，否则以position来展示。不超过12个汉字',
    )
    users_update_parser.add_argument(
        '--nickname',
        type=str,
        help='视频号名字（设置后，成员将对外展示该视频号）。须从企业绑定到企业微信的视频号中选择，可在“我的企业”页中查看绑定的视频号',
    )
    users_update_parser.add_argument(
        '--address',
        type=str,
        help='地址。长度最大128个字符',
    )
    users_update_parser.add_argument(
        '--main-department',
        type=int,
        help='主部门',
    )

    def _handle_users_update(a: argparse.Namespace) -> dict:
        return client.users_update(
            userid=a.userid,
            name=a.name,
            alias=a.alias,
            mobile=a.mobile,
            department=a.department,
            order=a.order,
            position=a.position,
            gender=a.gender,
            email=a.email,
            biz_mail=a.biz_mail,
            biz_mail_alias=a.biz_mail_alias,
            telephone=a.telephone,
            is_leader_in_dept=a.is_leader_in_dept,
            direct_leader=a.direct_leader,
            avatar_mediaid=a.avatar_mediaid,
            enable=a.enable,
            extattr=a.extattr,
            external_profile=a.external_profile,
            external_position=a.external_position,
            nickname=a.nickname,
            address=a.address,
            main_department=a.main_department,
        )
    table[('users', 'update')] = _handle_users_update

    return table
