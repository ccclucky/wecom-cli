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

    advanced_feature_parser = subparsers.add_parser(
        'advanced_feature',
        help='advanced_feature',
    )
    advanced_feature_sub = advanced_feature_parser.add_subparsers(dest='__action', required=True)

    advanced_feature_get_apply_id_list_parser = advanced_feature_sub.add_parser(
        'get-apply-id-list',
        help='批量获取申请单ID',
    )
    advanced_feature_get_apply_id_list_parser.add_argument(
        '--business-type',
        type=str,
        required=True,
        help='申请的高级账号类型 1-邮件 2-文档 3-微盘 4-会议',
    )
    advanced_feature_get_apply_id_list_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='申请的userid',
    )
    advanced_feature_get_apply_id_list_parser.add_argument(
        '--limit',
        type=int,
        help='分页查询的数据上限。默认100，最大200 注意：不保证每次返回的数据刚好为指定limit，须用返回的has_more判断是否继续请求',
    )
    advanced_feature_get_apply_id_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    advanced_feature_get_apply_id_list_parser.add_argument(
        '--req-type',
        type=str,
        help='0-所有 1-仅api单 2-非api 申请单， 默认为0',
    )

    def _handle_advanced_feature_get_apply_id_list(a: argparse.Namespace) -> dict:
        return client.advanced_feature_get_apply_id_list(
            business_type=a.business_type,
            userid=a.userid,
            limit=a.limit,
            cursor=a.cursor,
            req_type=a.req_type,
        )
    table[('advanced_feature', 'get-apply-id-list')] = _handle_advanced_feature_get_apply_id_list

    advanced_feature_get_approval_info_parser = advanced_feature_sub.add_parser(
        'get-approval-info',
        help='获取申请单详细信息',
    )
    advanced_feature_get_approval_info_parser.add_argument(
        '--apply-id',
        type=str,
        required=True,
        help='申请id',
    )

    def _handle_advanced_feature_get_approval_info(a: argparse.Namespace) -> dict:
        return client.advanced_feature_get_approval_info(
            apply_id=a.apply_id,
        )
    table[('advanced_feature', 'get-approval-info')] = _handle_advanced_feature_get_approval_info

    advanced_feature_set_approval_detail_parser = advanced_feature_sub.add_parser(
        'set-approval-detail',
        help='设置审批单审批信息',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--apply-id',
        type=str,
        required=True,
        help='申请id',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--approval-id',
        type=str,
        required=True,
        help='审批id，注意：应用生成审批id后，审批id和申请id是一一对应的，不可改变',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--approval-status',
        type=str,
        required=True,
        help='审批单状态：1-审批中; 2-已驳回; 3-已同意; 101-已撤销',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--approval-url',
        type=str,
        required=True,
        help='审批单跳转链接，须已"http://"或"https://"开头',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--process-list-node-list',
        type=str,
        required=True,
        help='审批单审批节点，注意：如果需要变更审批节点信息，需要全量节点都传入',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--process-list-node-list-node-apv-status',
        type=str,
        required=True,
        help='审批节点状态：1-审批中; 2-已驳回; 3-已同意; 101-已撤销; 102-未到流程',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--process-list-node-list-node-apv-rel',
        type=str,
        required=True,
        help='审批节点多人审批方式：1-会签；2-或签；3-依次审批',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--process-list-node-list-current-approvers',
        type=str,
        help='当前审批节点待处理人列表，最多100个，待处理人列表和已处理人列表不可同时为空',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--process-list-node-list-completed-approvers',
        type=str,
        help='当前审批节点已处理人列表，做多100个，待处理人列表和已处理人列表不可同时为空',
    )
    advanced_feature_set_approval_detail_parser.add_argument(
        '--process-list-node-list-apv-update-time',
        type=str,
        help='审批节点更新时间',
    )

    def _handle_advanced_feature_set_approval_detail(a: argparse.Namespace) -> dict:
        return client.advanced_feature_set_approval_detail(
            apply_id=a.apply_id,
            approval_id=a.approval_id,
            approval_status=a.approval_status,
            approval_url=a.approval_url,
            process_list_node_list=a.process_list_node_list,
            process_list_node_list_node_apv_status=a.process_list_node_list_node_apv_status,
            process_list_node_list_node_apv_rel=a.process_list_node_list_node_apv_rel,
            process_list_node_list_current_approvers=a.process_list_node_list_current_approvers,
            process_list_node_list_completed_approvers=a.process_list_node_list_completed_approvers,
            process_list_node_list_apv_update_time=a.process_list_node_list_apv_update_time,
        )
    table[('advanced_feature', 'set-approval-detail')] = _handle_advanced_feature_set_approval_detail

    appchat_parser = subparsers.add_parser(
        'appchat',
        help='appchat',
    )
    appchat_sub = appchat_parser.add_subparsers(dest='__action', required=True)

    appchat_get_parser = appchat_sub.add_parser(
        'get',
        help='获取群聊会话',
    )
    appchat_get_parser.add_argument(
        '--chatid',
        type=str,
        required=True,
        help='群聊id',
    )

    def _handle_appchat_get(a: argparse.Namespace) -> dict:
        return client.appchat_get(
            chatid=a.chatid,
        )
    table[('appchat', 'get')] = _handle_appchat_get

    appchat_update_parser = appchat_sub.add_parser(
        'update',
        help='修改群聊会话',
    )
    appchat_update_parser.add_argument(
        '--chatid',
        type=str,
        required=True,
        help='群聊id',
    )
    appchat_update_parser.add_argument(
        '--name',
        type=str,
        help='新的群聊名。若不需更新，请忽略此参数。最多50个utf8字符，超过将截断',
    )
    appchat_update_parser.add_argument(
        '--owner',
        type=str,
        help='新群主的id。若不需更新，请忽略此参数。课程群聊群主必须拥有课程群创建权限，del_user_list包含群主时本字段必填',
    )
    appchat_update_parser.add_argument(
        '--add-user-list',
        type=str,
        help='添加成员的id列表',
    )
    appchat_update_parser.add_argument(
        '--del-user-list',
        type=str,
        help='踢出成员的id列表',
    )

    def _handle_appchat_update(a: argparse.Namespace) -> dict:
        return client.appchat_update(
            chatid=a.chatid,
            name=a.name,
            owner=a.owner,
            add_user_list=a.add_user_list,
            del_user_list=a.del_user_list,
        )
    table[('appchat', 'update')] = _handle_appchat_update

    auth_parser = subparsers.add_parser(
        'auth',
        help='auth',
    )
    auth_sub = auth_parser.add_subparsers(dest='__action', required=True)

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

    auth_getuserdetail_parser = auth_sub.add_parser(
        'getuserdetail',
        help='获取访问用户敏感信息',
    )
    auth_getuserdetail_parser.add_argument(
        '--user-ticket',
        type=str,
        required=True,
        help='成员票据',
    )

    def _handle_auth_getuserdetail(a: argparse.Namespace) -> dict:
        return client.auth_getuserdetail(
            user_ticket=a.user_ticket,
        )
    table[('auth', 'getuserdetail')] = _handle_auth_getuserdetail

    auth_sub.add_parser(
        'getuserinfo',
        help='获取用户登录身份',
    )

    def _handle_auth_getuserinfo(a: argparse.Namespace) -> dict:
        return client.auth_getuserinfo()
    table[('auth', 'getuserinfo')] = _handle_auth_getuserinfo

    batch_parser = subparsers.add_parser(
        'batch',
        help='batch',
    )
    batch_sub = batch_parser.add_subparsers(dest='__action', required=True)

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

    chatdata_parser = subparsers.add_parser(
        'chatdata',
        help='chatdata',
    )
    chatdata_sub = chatdata_parser.add_subparsers(dest='__action', required=True)

    chatdata_async_program_task_parser = chatdata_sub.add_parser(
        'async-program-task',
        help='应用异步调用专区程序',
    )
    chatdata_async_program_task_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id',
    )
    chatdata_async_program_task_parser.add_argument(
        '--ability-id',
        type=str,
        required=True,
        help='程序关联的能力id',
    )
    chatdata_async_program_task_parser.add_argument(
        '--request-data',
        type=str,
        required=True,
        help='请求的输入JSON，要求与配置的格式匹配',
    )

    def _handle_chatdata_async_program_task(a: argparse.Namespace) -> dict:
        return client.chatdata_async_program_task(
            program_id=a.program_id,
            ability_id=a.ability_id,
            request_data=a.request_data,
        )
    table[('chatdata', 'async-program-task')] = _handle_chatdata_async_program_task

    chatdata_check_debug_mode_parser = chatdata_sub.add_parser(
        'check-debug-mode',
        help='获取专区调试模式状态',
    )
    chatdata_check_debug_mode_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id',
    )

    def _handle_chatdata_check_debug_mode(a: argparse.Namespace) -> dict:
        return client.chatdata_check_debug_mode(
            program_id=a.program_id,
        )
    table[('chatdata', 'check-debug-mode')] = _handle_chatdata_check_debug_mode

    chatdata_close_debug_mode_parser = chatdata_sub.add_parser(
        'close-debug-mode',
        help='关闭专区调试模式',
    )
    chatdata_close_debug_mode_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id',
    )

    def _handle_chatdata_close_debug_mode(a: argparse.Namespace) -> dict:
        return client.chatdata_close_debug_mode(
            program_id=a.program_id,
        )
    table[('chatdata', 'close-debug-mode')] = _handle_chatdata_close_debug_mode

    chatdata_get_auth_user_list_parser = chatdata_sub.add_parser(
        'get-auth-user-list',
        help='获取授权存档的成员列表',
    )
    chatdata_get_auth_user_list_parser.add_argument(
        '--cursor',
        type=str,
        help='上一次调用时返回的next_cursor，第一次拉取可以不填',
    )
    chatdata_get_auth_user_list_parser.add_argument(
        '--limit',
        type=str,
        help='本次查询返回的最大条数。不超过1000，默认200条',
    )

    def _handle_chatdata_get_auth_user_list(a: argparse.Namespace) -> dict:
        return client.chatdata_get_auth_user_list(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('chatdata', 'get-auth-user-list')] = _handle_chatdata_get_auth_user_list

    chatdata_open_debug_mode_parser = chatdata_sub.add_parser(
        'open-debug-mode',
        help='开启专区调试模式',
    )
    chatdata_open_debug_mode_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id',
    )
    chatdata_open_debug_mode_parser.add_argument(
        '--debug-token',
        type=str,
        required=True,
        help='程序的调试凭证',
    )

    def _handle_chatdata_open_debug_mode(a: argparse.Namespace) -> dict:
        return client.chatdata_open_debug_mode(
            program_id=a.program_id,
            debug_token=a.debug_token,
        )
    table[('chatdata', 'open-debug-mode')] = _handle_chatdata_open_debug_mode

    chatdata_set_hide_sensitiveinfo_config_parser = chatdata_sub.add_parser(
        'set-hide-sensitiveinfo-config',
        help='会话组件敏感信息隐藏设置',
    )
    chatdata_set_hide_sensitiveinfo_config_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员的userid',
    )
    chatdata_set_hide_sensitiveinfo_config_parser.add_argument(
        '--config',
        type=str,
        required=True,
        help='敏感信息隐藏配置，详见Config结构说明',
    )

    def _handle_chatdata_set_hide_sensitiveinfo_config(a: argparse.Namespace) -> dict:
        return client.chatdata_set_hide_sensitiveinfo_config(
            userid=a.userid,
            config=a.config,
        )
    table[('chatdata', 'set-hide-sensitiveinfo-config')] = _handle_chatdata_set_hide_sensitiveinfo_config

    chatdata_set_log_level_parser = chatdata_sub.add_parser(
        'set-log-level',
        help='设置日志打印级别',
    )
    chatdata_set_log_level_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id',
    )
    chatdata_set_log_level_parser.add_argument(
        '--log-level',
        type=str,
        required=True,
        help='日志级别 指定后，仅会存储不高于改级别的日志。例如指定级别为2，那么只会存储级别为1或2的日志 默认级别为2 取值范围： 1 - ERR 2 - INFO 3 - DBG',
    )

    def _handle_chatdata_set_log_level(a: argparse.Namespace) -> dict:
        return client.chatdata_set_log_level(
            program_id=a.program_id,
            log_level=a.log_level,
        )
    table[('chatdata', 'set-log-level')] = _handle_chatdata_set_log_level

    chatdata_set_public_key_parser = chatdata_sub.add_parser(
        'set-public-key',
        help='设置公钥',
    )
    chatdata_set_public_key_parser.add_argument(
        '--public-key',
        type=str,
        required=True,
        help='开发者为该企业生成的公钥，可以参考下方使用openssl命令生成',
    )
    chatdata_set_public_key_parser.add_argument(
        '--public-key-ver',
        type=str,
        required=True,
        help='公钥对应的版本号，当重复调用该接口更换公钥时要求比旧公钥版本号大',
    )

    def _handle_chatdata_set_public_key(a: argparse.Namespace) -> dict:
        return client.chatdata_set_public_key(
            public_key=a.public_key,
            public_key_ver=a.public_key_ver,
        )
    table[('chatdata', 'set-public-key')] = _handle_chatdata_set_public_key

    chatdata_set_receive_callback_parser = chatdata_sub.add_parser(
        'set-receive-callback',
        help='设置专区接收回调事件',
    )
    chatdata_set_receive_callback_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id，同一个应用只能设置一个程序接收。若先设置了程序A接收，再调用该接口设置程序B时，会更改为程序B接收',
    )

    def _handle_chatdata_set_receive_callback(a: argparse.Namespace) -> dict:
        return client.chatdata_set_receive_callback(
            program_id=a.program_id,
        )
    table[('chatdata', 'set-receive-callback')] = _handle_chatdata_set_receive_callback

    chatdata_sync_call_program_parser = chatdata_sub.add_parser(
        'sync-call-program',
        help='应用同步调用专区程序',
    )
    chatdata_sync_call_program_parser.add_argument(
        '--program-id',
        type=str,
        required=True,
        help='应用关联的程序id',
    )
    chatdata_sync_call_program_parser.add_argument(
        '--ability-id',
        type=str,
        required=True,
        help='程序关联的能力id',
    )
    chatdata_sync_call_program_parser.add_argument(
        '--notify-id',
        type=str,
        help='通知id。由专区通知应用返回',
    )
    chatdata_sync_call_program_parser.add_argument(
        '--request-data',
        type=str,
        required=True,
        help='请求的输入JSON，要求与配置的输入协议格式匹配，如需使用专区程序示例，请留意Java版本demo的输入无需在request_data内包裹一层input对象',
    )

    def _handle_chatdata_sync_call_program(a: argparse.Namespace) -> dict:
        return client.chatdata_sync_call_program(
            program_id=a.program_id,
            ability_id=a.ability_id,
            notify_id=a.notify_id,
            request_data=a.request_data,
        )
    table[('chatdata', 'sync-call-program')] = _handle_chatdata_sync_call_program

    chatdata_upload_media_parser = chatdata_sub.add_parser(
        'upload-media',
        help='上传临时文件到专区',
    )
    chatdata_upload_media_parser.add_argument(
        '--type',
        type=str,
        required=True,
        help='文件类型，目前仅支持普通文件：file',
    )

    def _handle_chatdata_upload_media(a: argparse.Namespace) -> dict:
        return client.chatdata_upload_media(
            type=a.type,
        )
    table[('chatdata', 'upload-media')] = _handle_chatdata_upload_media

    checkin_parser = subparsers.add_parser(
        'checkin',
        help='checkin',
    )
    checkin_sub = checkin_parser.add_subparsers(dest='__action', required=True)

    checkin_add_checkin_record_parser = checkin_sub.add_parser(
        'add-checkin-record',
        help='添加打卡记录',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--records',
        type=str,
        required=True,
        help='打卡记录，一批最多200个',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='用户id',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--checkin-time',
        type=str,
        required=True,
        help='打卡时间。Unix时间戳',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--location-title',
        type=str,
        required=True,
        help='打卡地点title，限制1024字符',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--location-detail',
        type=str,
        required=True,
        help='打卡地点详情限制1024字符',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--notes',
        type=str,
        help='打卡备注限制1024字符',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--wifiname',
        type=str,
        help='打卡wifi名称限制1024字符',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--wifimac',
        type=str,
        help='打卡的MAC地址/bssid 满足正则表达式^[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}$。传入wifiname时必填',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--mediaids',
        type=str,
        help='打卡的附件media_id，可使用media/upload上传附件。当前最多只允许传1个',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--lat',
        type=str,
        help='位置打卡地点纬度，是实际纬度的1000000倍，与腾讯地图一致采用GCJ-02坐标系统标准 范围 -90000000,90000000',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--lng',
        type=str,
        help='位置打卡地点经度，是实际经度的1000000倍，与腾讯地图一致采用GCJ-02坐标系统标准 范围-180000000,180000000',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--device-type',
        type=str,
        required=True,
        help='打卡设备类型：1、门禁 2、考勤机（人脸识别、指纹识别） 3、其他；',
    )
    checkin_add_checkin_record_parser.add_argument(
        '--device-detail',
        type=str,
        required=True,
        help='打卡设备品牌：字符串写入（限制40个字符内）',
    )

    def _handle_checkin_add_checkin_record(a: argparse.Namespace) -> dict:
        return client.checkin_add_checkin_record(
            records=a.records,
            userid=a.userid,
            checkin_time=a.checkin_time,
            location_title=a.location_title,
            location_detail=a.location_detail,
            notes=a.notes,
            wifiname=a.wifiname,
            wifimac=a.wifimac,
            mediaids=a.mediaids,
            lat=a.lat,
            lng=a.lng,
            device_type=a.device_type,
            device_detail=a.device_detail,
        )
    table[('checkin', 'add-checkin-record')] = _handle_checkin_add_checkin_record

    checkin_punch_correction_parser = checkin_sub.add_parser(
        'punch-correction',
        help='为打卡人员补卡',
    )
    checkin_punch_correction_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='需要补卡的成员userid',
    )
    checkin_punch_correction_parser.add_argument(
        '--schedule-date-time',
        type=str,
        required=True,
        help='应打卡日期，为当天0点的Unix时间戳。',
    )
    checkin_punch_correction_parser.add_argument(
        '--schedule-checkin-time',
        type=str,
        help='应打卡时间点，相对应打卡日期0点的偏移秒数，如9点整则为32400。可通过获取员工打卡规则获取对应的规则打卡时间点，如work_sec/off_work_sec。 对于没有规则对应的打卡时间点，如休息日打卡、无规则打卡、自由上下班，该参数不用填。',
    )
    checkin_punch_correction_parser.add_argument(
        '--checkin-time',
        type=str,
        required=True,
        help='实际打卡时间，Unix时间戳。相对于schedule_checkin_time的实际打卡时间，具体可以表现为正常/迟到/早退',
    )
    checkin_punch_correction_parser.add_argument(
        '--remark',
        type=str,
        help='备注信息 不超过512字节',
    )

    def _handle_checkin_punch_correction(a: argparse.Namespace) -> dict:
        return client.checkin_punch_correction(
            userid=a.userid,
            schedule_date_time=a.schedule_date_time,
            schedule_checkin_time=a.schedule_checkin_time,
            checkin_time=a.checkin_time,
            remark=a.remark,
        )
    table[('checkin', 'punch-correction')] = _handle_checkin_punch_correction

    contacts_parser = subparsers.add_parser(
        'contacts',
        help='contacts',
    )
    contacts_sub = contacts_parser.add_subparsers(dest='__action', required=True)

    contacts_list_users_parser = contacts_sub.add_parser(
        'list',
        help='列出成员',
    )
    contacts_list_users_parser.add_argument(
        '--department-id',
        type=int,
        required=True,
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
        help='corp',
    )
    corp_sub = corp_parser.add_subparsers(dest='__action', required=True)

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

    corp_getapprovaldata_parser = corp_sub.add_parser(
        'getapprovaldata',
        help='获取审批数据（旧）',
    )
    corp_getapprovaldata_parser.add_argument(
        '--starttime',
        type=str,
        required=True,
        help='获取审批记录的开始时间。Unix时间戳',
    )
    corp_getapprovaldata_parser.add_argument(
        '--endtime',
        type=str,
        required=True,
        help='获取审批记录的结束时间。Unix时间戳',
    )
    corp_getapprovaldata_parser.add_argument(
        '--next-spnum',
        type=str,
        help='第一个拉取的审批单号，不填从该时间段的第一个审批单拉取',
    )

    def _handle_corp_getapprovaldata(a: argparse.Namespace) -> dict:
        return client.corp_getapprovaldata(
            starttime=a.starttime,
            endtime=a.endtime,
            next_spnum=a.next_spnum,
        )
    table[('corp', 'getapprovaldata')] = _handle_corp_getapprovaldata

    corpgroup_parser = subparsers.add_parser(
        'corpgroup',
        help='corpgroup',
    )
    corpgroup_sub = corpgroup_parser.add_subparsers(dest='__action', required=True)

    corpgroup_sub.add_parser(
        'corp-get-chain-list',
        help='获取上下游信息',
    )

    def _handle_corpgroup_corp_get_chain_list(a: argparse.Namespace) -> dict:
        return client.corpgroup_corp_get_chain_list()
    table[('corpgroup', 'corp-get-chain-list')] = _handle_corpgroup_corp_get_chain_list

    corpgroup_corp_get_chain_user_custom_id_parser = corpgroup_sub.add_parser(
        'corp-get-chain-user-custom-id',
        help='查询成员自定义id',
    )
    corpgroup_corp_get_chain_user_custom_id_parser.add_argument(
        '--chain-id',
        type=str,
        required=True,
        help='上下游id',
    )
    corpgroup_corp_get_chain_user_custom_id_parser.add_argument(
        '--corpid',
        type=str,
        required=True,
        help='已加入企业id',
    )
    corpgroup_corp_get_chain_user_custom_id_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='企业内的成员',
    )

    def _handle_corpgroup_corp_get_chain_user_custom_id(a: argparse.Namespace) -> dict:
        return client.corpgroup_corp_get_chain_user_custom_id(
            chain_id=a.chain_id,
            corpid=a.corpid,
            userid=a.userid,
        )
    table[('corpgroup', 'corp-get-chain-user-custom-id')] = _handle_corpgroup_corp_get_chain_user_custom_id

    corpgroup_corp_gettoken_parser = corpgroup_sub.add_parser(
        'corp-gettoken',
        help='获取下级/下游企业的access_token',
    )
    corpgroup_corp_gettoken_parser.add_argument(
        '--corpid',
        type=str,
        required=True,
        help='已授权的下级/下游企业corpid',
    )
    corpgroup_corp_gettoken_parser.add_argument(
        '--agentid',
        type=str,
        required=True,
        help='已授权的下级/下游企业应用ID',
    )
    corpgroup_corp_gettoken_parser.add_argument(
        '--business-type',
        type=str,
        help='填0则为企业互联/局校互联，填1则表示上下游企业，默认0',
    )

    def _handle_corpgroup_corp_gettoken(a: argparse.Namespace) -> dict:
        return client.corpgroup_corp_gettoken(
            corpid=a.corpid,
            agentid=a.agentid,
            business_type=a.business_type,
        )
    table[('corpgroup', 'corp-gettoken')] = _handle_corpgroup_corp_gettoken

    corpgroup_corp_list_app_share_info_parser = corpgroup_sub.add_parser(
        'corp-list-app-share-info',
        help='获取应用共享信息',
    )
    corpgroup_corp_list_app_share_info_parser.add_argument(
        '--business-type',
        type=str,
        help='填0则为企业互联/局校互联，填1则表示上下游企业',
    )
    corpgroup_corp_list_app_share_info_parser.add_argument(
        '--agentid',
        type=str,
        required=True,
        help='上级/上游企业应用agentid',
    )
    corpgroup_corp_list_app_share_info_parser.add_argument(
        '--corpid',
        type=str,
        help='下级/下游企业corpid，若指定该参数则表示拉取该下级/下游企业的应用共享信息',
    )
    corpgroup_corp_list_app_share_info_parser.add_argument(
        '--limit',
        type=str,
        help='返回的最大记录数，整型，最大值100，默认情况或者值为0表示下拉取全量数据，建议分页拉取或者通过指定corpid参数拉取。',
    )
    corpgroup_corp_list_app_share_info_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )

    def _handle_corpgroup_corp_list_app_share_info(a: argparse.Namespace) -> dict:
        return client.corpgroup_corp_list_app_share_info(
            business_type=a.business_type,
            agentid=a.agentid,
            corpid=a.corpid,
            limit=a.limit,
            cursor=a.cursor,
        )
    table[('corpgroup', 'corp-list-app-share-info')] = _handle_corpgroup_corp_list_app_share_info

    corpgroup_corp_remove_corp_parser = corpgroup_sub.add_parser(
        'corp-remove-corp',
        help='移除企业',
    )
    corpgroup_corp_remove_corp_parser.add_argument(
        '--chain-id',
        type=str,
        required=True,
        help='上下游id',
    )
    corpgroup_corp_remove_corp_parser.add_argument(
        '--corpid',
        type=str,
        help='需要移除的下游企业corpid',
    )
    corpgroup_corp_remove_corp_parser.add_argument(
        '--pending-corpid',
        type=str,
        help='需要移除的未加入下游企业corpid，corpid和pending_corpid至少填一个，都填corpid生效',
    )

    def _handle_corpgroup_corp_remove_corp(a: argparse.Namespace) -> dict:
        return client.corpgroup_corp_remove_corp(
            chain_id=a.chain_id,
            corpid=a.corpid,
            pending_corpid=a.pending_corpid,
        )
    table[('corpgroup', 'corp-remove-corp')] = _handle_corpgroup_corp_remove_corp

    corpgroup_get_corp_shared_chain_list_parser = corpgroup_sub.add_parser(
        'get-corp-shared-chain-list',
        help='获取下级企业加入的上下游',
    )
    corpgroup_get_corp_shared_chain_list_parser.add_argument(
        '--corpid',
        type=str,
        help='已加入企业id',
    )

    def _handle_corpgroup_get_corp_shared_chain_list(a: argparse.Namespace) -> dict:
        return client.corpgroup_get_corp_shared_chain_list(
            corpid=a.corpid,
        )
    table[('corpgroup', 'get-corp-shared-chain-list')] = _handle_corpgroup_get_corp_shared_chain_list

    corpgroup_getresult_parser = corpgroup_sub.add_parser(
        'getresult',
        help='获取异步任务结果',
    )
    corpgroup_getresult_parser.add_argument(
        '--jobid',
        type=str,
        required=True,
        help='异步任务id，最大长度为64字节',
    )

    def _handle_corpgroup_getresult(a: argparse.Namespace) -> dict:
        return client.corpgroup_getresult(
            jobid=a.jobid,
        )
    table[('corpgroup', 'getresult')] = _handle_corpgroup_getresult

    corpgroup_import_chain_contact_parser = corpgroup_sub.add_parser(
        'import-chain-contact',
        help='批量导入上下游联系人',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--chain-id',
        type=str,
        required=True,
        help='上下游id。文件中的联系人将会被导入此上下游中',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list',
        type=str,
        required=True,
        help='上下游联系人列表。这些联系人将会被导入此上下游中',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-corp-name',
        type=str,
        required=True,
        help='上下游企业名称。长度为1-32个utf8字符。只能由中文、字母、数字和“ -_()（）”六种字符组成',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-group-path',
        type=str,
        help='导入后企业所在分组。分组为空的企业会放在根分组下。仅针对新导入企业生效，不会修改已导入企业的分组。',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-custom-id',
        type=str,
        help='上下游企业自定义 id。长度为0～64 个字节，只能由数字和字母组成',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-contact-info-list',
        type=str,
        required=True,
        help='上下游联系人信息列表',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-contact-info-list-name',
        type=str,
        required=True,
        help='上下游联系人姓名。长度为1～32个utf8字符',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-contact-info-list-identity-type',
        type=str,
        required=True,
        help='联系人身份类型。1:成员，2:负责人。',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-contact-info-list-mobile',
        type=str,
        required=True,
        help='手机号。支持国内、国际手机号（国内手机号直接输入手机号即可，格式示例：“138****0001”；国际手机号必须包含加号以及国家地区码，格式示例：“+85259****45”',
    )
    corpgroup_import_chain_contact_parser.add_argument(
        '--contact-list-contact-info-list-user-custom-id',
        type=str,
        help='上下游用户自定义 id。类型为字符串，暂时只支持传入64比特无符号整型，取值范围1到2^64-2，必须是全数字，不得传入前置0，且不能为11位或13位数字。',
    )

    def _handle_corpgroup_import_chain_contact(a: argparse.Namespace) -> dict:
        return client.corpgroup_import_chain_contact(
            chain_id=a.chain_id,
            contact_list=a.contact_list,
            contact_list_corp_name=a.contact_list_corp_name,
            contact_list_group_path=a.contact_list_group_path,
            contact_list_custom_id=a.contact_list_custom_id,
            contact_list_contact_info_list=a.contact_list_contact_info_list,
            contact_list_contact_info_list_name=a.contact_list_contact_info_list_name,
            contact_list_contact_info_list_identity_type=a.contact_list_contact_info_list_identity_type,
            contact_list_contact_info_list_mobile=a.contact_list_contact_info_list_mobile,
            contact_list_contact_info_list_user_custom_id=a.contact_list_contact_info_list_user_custom_id,
        )
    table[('corpgroup', 'import-chain-contact')] = _handle_corpgroup_import_chain_contact

    corpgroup_rule_list_ids_parser = corpgroup_sub.add_parser(
        'rule-list-ids',
        help='获取对接规则id列表',
    )
    corpgroup_rule_list_ids_parser.add_argument(
        '--chain-id',
        type=str,
        required=True,
        help='上下游id',
    )

    def _handle_corpgroup_rule_list_ids(a: argparse.Namespace) -> dict:
        return client.corpgroup_rule_list_ids(
            chain_id=a.chain_id,
        )
    table[('corpgroup', 'rule-list-ids')] = _handle_corpgroup_rule_list_ids

    corpgroup_unionid_to_external_userid_parser = corpgroup_sub.add_parser(
        'unionid-to-external-userid',
        help='上下游关联客户信息-已添加客户',
    )
    corpgroup_unionid_to_external_userid_parser.add_argument(
        '--unionid',
        type=str,
        required=True,
        help='微信客户的unionid',
    )
    corpgroup_unionid_to_external_userid_parser.add_argument(
        '--openid',
        type=str,
        required=True,
        help='微信客户的openid',
    )
    corpgroup_unionid_to_external_userid_parser.add_argument(
        '--corpid',
        type=str,
        help='需要换取的企业corpid，不填则拉取所有企业',
    )
    corpgroup_unionid_to_external_userid_parser.add_argument(
        '--mass-call-ticket',
        type=str,
        help='大批量调用凭据, 适用于数据初始化场景, 有获取及使用限制',
    )

    def _handle_corpgroup_unionid_to_external_userid(a: argparse.Namespace) -> dict:
        return client.corpgroup_unionid_to_external_userid(
            unionid=a.unionid,
            openid=a.openid,
            corpid=a.corpid,
            mass_call_ticket=a.mass_call_ticket,
        )
    table[('corpgroup', 'unionid-to-external-userid')] = _handle_corpgroup_unionid_to_external_userid

    customers_parser = subparsers.add_parser(
        'customers',
        help='customers',
    )
    customers_sub = customers_parser.add_subparsers(dest='__action', required=True)

    customers_add_contact_way_parser = customers_sub.add_parser(
        'add-contact-way',
        help='客户联系「联系我」管理',
    )
    customers_add_contact_way_parser.add_argument(
        '--type',
        type=str,
        required=True,
        help='联系方式类型,1-单人, 2-多人',
    )
    customers_add_contact_way_parser.add_argument(
        '--scene',
        type=str,
        required=True,
        help='场景，1-在小程序中联系，2-通过二维码联系',
    )
    customers_add_contact_way_parser.add_argument(
        '--style',
        type=str,
        help='在小程序中联系时使用的控件样式，详见附表',
    )
    customers_add_contact_way_parser.add_argument(
        '--remark',
        type=str,
        help='联系方式的备注信息，用于助记，不超过30个字符',
    )
    customers_add_contact_way_parser.add_argument(
        '--skip-verify',
        help='外部客户添加时是否无需验证，默认为true',
    )
    customers_add_contact_way_parser.add_argument(
        '--state',
        type=str,
        help='企业自定义的state参数，用于区分不同的添加渠道，在调用“获取客户详情”时会返回该参数值，不超过30个字符',
    )
    customers_add_contact_way_parser.add_argument(
        '--user',
        type=str,
        help='使用该联系方式的用户userID列表，在type为1时为必填，且只能有一个',
    )
    customers_add_contact_way_parser.add_argument(
        '--party',
        type=str,
        help='使用该联系方式的部门id列表，只在type为2时有效',
    )
    customers_add_contact_way_parser.add_argument(
        '--is-temp',
        help='是否临时会话模式，true表示使用临时会话模式，默认为false',
    )
    customers_add_contact_way_parser.add_argument(
        '--expires-in',
        type=str,
        help='临时会话二维码有效期，以秒为单位。该参数仅在is_temp为true时有效，默认7天，最多为14天',
    )
    customers_add_contact_way_parser.add_argument(
        '--chat-expires-in',
        type=str,
        help='临时会话有效期，以秒为单位。该参数仅在is_temp为true时有效，默认为添加好友后24小时，最多为14天',
    )
    customers_add_contact_way_parser.add_argument(
        '--unionid',
        type=str,
        help='可进行临时会话的客户unionid，该参数仅在is_temp为true时有效，如不指定则不进行限制',
    )
    customers_add_contact_way_parser.add_argument(
        '--is-exclusive',
        help='是否开启同一外部企业客户只能添加同一个员工，默认为否，开启后，同一个企业的客户会优先添加到同一个跟进人',
    )
    customers_add_contact_way_parser.add_argument(
        '--mark-source',
        help='是否标记客户添加来源为该应用创建的「联系我」, 默认为true; 仅对「营销获客」应用生效',
    )
    customers_add_contact_way_parser.add_argument(
        '--conclusions',
        type=str,
        help='结束语，会话结束时自动发送给客户，可参考“结束语定义”，仅在is_temp为true时有效',
    )

    def _handle_customers_add_contact_way(a: argparse.Namespace) -> dict:
        return client.customers_add_contact_way(
            type=a.type,
            scene=a.scene,
            style=a.style,
            remark=a.remark,
            skip_verify=a.skip_verify,
            state=a.state,
            user=a.user,
            party=a.party,
            is_temp=a.is_temp,
            expires_in=a.expires_in,
            chat_expires_in=a.chat_expires_in,
            unionid=a.unionid,
            is_exclusive=a.is_exclusive,
            mark_source=a.mark_source,
            conclusions=a.conclusions,
        )
    table[('customers', 'add-contact-way')] = _handle_customers_add_contact_way

    customers_batch_get_by_user_parser = customers_sub.add_parser(
        'batch-get-by-user',
        help='批量获取客户详情',
    )
    customers_batch_get_by_user_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='企业成员的userid列表，字符串类型，最多支持100个',
    )
    customers_batch_get_by_user_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    customers_batch_get_by_user_parser.add_argument(
        '--limit',
        type=str,
        help='返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值',
    )

    def _handle_customers_batch_get_by_user(a: argparse.Namespace) -> dict:
        return client.customers_batch_get_by_user(
            userid_list=a.userid_list,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('customers', 'batch-get-by-user')] = _handle_customers_batch_get_by_user

    customers_cancel_groupmsg_send_parser = customers_sub.add_parser(
        'cancel-groupmsg-send',
        help='停止企业群发',
    )
    customers_cancel_groupmsg_send_parser.add_argument(
        '--msgid',
        type=str,
        required=True,
        help='群发消息的id，通过获取群发记录列表接口返回',
    )

    def _handle_customers_cancel_groupmsg_send(a: argparse.Namespace) -> dict:
        return client.customers_cancel_groupmsg_send(
            msgid=a.msgid,
        )
    table[('customers', 'cancel-groupmsg-send')] = _handle_customers_cancel_groupmsg_send

    customers_cancel_moment_task_parser = customers_sub.add_parser(
        'cancel-moment-task',
        help='停止发表企业朋友圈',
    )
    customers_cancel_moment_task_parser.add_argument(
        '--moment-id',
        type=str,
        required=True,
        help='朋友圈id，可通过获取客户朋友圈企业发表的列表接口获取朋友圈企业发表的列表',
    )

    def _handle_customers_cancel_moment_task(a: argparse.Namespace) -> dict:
        return client.customers_cancel_moment_task(
            moment_id=a.moment_id,
        )
    table[('customers', 'cancel-moment-task')] = _handle_customers_cancel_moment_task

    customers_convert_to_openid_parser = customers_sub.add_parser(
        'convert-to-openid',
        help='外部联系人openid转换',
    )
    customers_convert_to_openid_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='外部联系人的userid，注意不是企业成员的账号',
    )

    def _handle_customers_convert_to_openid(a: argparse.Namespace) -> dict:
        return client.customers_convert_to_openid(
            external_userid=a.external_userid,
        )
    table[('customers', 'convert-to-openid')] = _handle_customers_convert_to_openid

    customers_customer_acquisition_list_link_parser = customers_sub.add_parser(
        'customer-acquisition-list-link',
        help='获客链接管理',
    )
    customers_customer_acquisition_list_link_parser.add_argument(
        '--limit',
        type=str,
        help='返回的最大记录数，整型，最大值100',
    )
    customers_customer_acquisition_list_link_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )

    def _handle_customers_customer_acquisition_list_link(a: argparse.Namespace) -> dict:
        return client.customers_customer_acquisition_list_link(
            limit=a.limit,
            cursor=a.cursor,
        )
    table[('customers', 'customer-acquisition-list-link')] = _handle_customers_customer_acquisition_list_link

    customers_customer_strategy_list_parser = customers_sub.add_parser(
        'customer-strategy-list',
        help='客户联系规则组管理',
    )
    customers_customer_strategy_list_parser.add_argument(
        '--cursor',
        type=str,
        help='分页查询游标，首次调用可不填',
    )
    customers_customer_strategy_list_parser.add_argument(
        '--limit',
        type=str,
        help='分页大小,默认为1000，最大不超过1000',
    )

    def _handle_customers_customer_strategy_list(a: argparse.Namespace) -> dict:
        return client.customers_customer_strategy_list(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('customers', 'customer-strategy-list')] = _handle_customers_customer_strategy_list

    customers_get_parser = customers_sub.add_parser(
        'get',
        help='获取客户详情',
    )
    customers_get_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='外部联系人的userid，注意不是企业成员的账号',
    )
    customers_get_parser.add_argument(
        '--cursor',
        type=str,
        help='上次请求返回的next_cursor',
    )

    def _handle_customers_get(a: argparse.Namespace) -> dict:
        return client.customers_get(
            external_userid=a.external_userid,
            cursor=a.cursor,
        )
    table[('customers', 'get')] = _handle_customers_get

    customers_sub.add_parser(
        'get-follow-user-list',
        help='获取配置了客户联系功能的成员列表',
    )

    def _handle_customers_get_follow_user_list(a: argparse.Namespace) -> dict:
        return client.customers_get_follow_user_list()
    table[('customers', 'get-follow-user-list')] = _handle_customers_get_follow_user_list

    customers_get_strategy_tag_list_parser = customers_sub.add_parser(
        'get-strategy-tag-list',
        help='管理企业规则组下的客户标签',
    )
    customers_get_strategy_tag_list_parser.add_argument(
        '--strategy-id',
        type=str,
        help='规则组id',
    )
    customers_get_strategy_tag_list_parser.add_argument(
        '--tag-id',
        type=str,
        help='要查询的标签id',
    )
    customers_get_strategy_tag_list_parser.add_argument(
        '--group-id',
        type=str,
        help='要查询的标签组id，返回该标签组以及其下的所有标签信息',
    )

    def _handle_customers_get_strategy_tag_list(a: argparse.Namespace) -> dict:
        return client.customers_get_strategy_tag_list(
            strategy_id=a.strategy_id,
            tag_id=a.tag_id,
            group_id=a.group_id,
        )
    table[('customers', 'get-strategy-tag-list')] = _handle_customers_get_strategy_tag_list

    customers_sub.add_parser(
        'get-subscribe-qr-code',
        help='获取「学校通知」二维码',
    )

    def _handle_customers_get_subscribe_qr_code(a: argparse.Namespace) -> dict:
        return client.customers_get_subscribe_qr_code()
    table[('customers', 'get-subscribe-qr-code')] = _handle_customers_get_subscribe_qr_code

    customers_groupchat_get_parser = customers_sub.add_parser(
        'groupchat-get',
        help='获取客户群详情',
    )
    customers_groupchat_get_parser.add_argument(
        '--chat-id',
        type=str,
        required=True,
        help='客户群ID',
    )
    customers_groupchat_get_parser.add_argument(
        '--need-name',
        help='是否需要返回群成员的名字group_chat.member_list.name。0-不返回；1-返回。默认不返回',
    )

    def _handle_customers_groupchat_get(a: argparse.Namespace) -> dict:
        return client.customers_groupchat_get(
            chat_id=a.chat_id,
            need_name=a.need_name,
        )
    table[('customers', 'groupchat-get')] = _handle_customers_groupchat_get

    customers_groupchat_list_parser = customers_sub.add_parser(
        'groupchat-list',
        help='获取客户群列表',
    )
    customers_groupchat_list_parser.add_argument(
        '--status-filter',
        type=str,
        help='客户群跟进状态过滤。 0 - 所有列表(即不过滤) 1 - 离职待继承 2 - 离职继承中 3 - 离职继承完成 默认为0',
    )
    customers_groupchat_list_parser.add_argument(
        '--owner-filter',
        type=str,
        help='群主过滤。 如果不填，表示获取应用可见范围内全部群主的数据（但是不建议这么用，如果可见范围人数超过1000人，为了防止数据包过大，会报错 81017） 当群主为离职成员时，必须要指定群主过滤才可拉取对应数据',
    )
    customers_groupchat_list_parser.add_argument(
        '--owner-filter-userid-list',
        type=str,
        help='用户ID列表。最多100个',
    )
    customers_groupchat_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用不填',
    )
    customers_groupchat_list_parser.add_argument(
        '--limit',
        type=str,
        required=True,
        help='分页，预期请求的数据量，取值范围 1 ~ 1000',
    )

    def _handle_customers_groupchat_list(a: argparse.Namespace) -> dict:
        return client.customers_groupchat_list(
            status_filter=a.status_filter,
            owner_filter=a.owner_filter,
            owner_filter_userid_list=a.owner_filter_userid_list,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('customers', 'groupchat-list')] = _handle_customers_groupchat_list

    customers_groupchat_onjob_transfer_parser = customers_sub.add_parser(
        'groupchat-onjob-transfer',
        help='分配在职成员的客户群',
    )
    customers_groupchat_onjob_transfer_parser.add_argument(
        '--chat-id-list',
        type=str,
        required=True,
        help='需要转群主的客户群ID列表。取值范围： 1 ~ 100',
    )
    customers_groupchat_onjob_transfer_parser.add_argument(
        '--new-owner',
        type=str,
        required=True,
        help='新群主ID',
    )

    def _handle_customers_groupchat_onjob_transfer(a: argparse.Namespace) -> dict:
        return client.customers_groupchat_onjob_transfer(
            chat_id_list=a.chat_id_list,
            new_owner=a.new_owner,
        )
    table[('customers', 'groupchat-onjob-transfer')] = _handle_customers_groupchat_onjob_transfer

    customers_list_parser = customers_sub.add_parser(
        'list',
        help='获取客户列表',
    )
    customers_list_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='企业成员的userid',
    )

    def _handle_customers_list(a: argparse.Namespace) -> dict:
        return client.customers_list(
            userid=a.userid,
        )
    table[('customers', 'list')] = _handle_customers_list

    customers_mark_tag_parser = customers_sub.add_parser(
        'mark-tag',
        help='编辑客户企业标签',
    )
    customers_mark_tag_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='添加外部联系人的userid',
    )
    customers_mark_tag_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='外部联系人userid',
    )
    customers_mark_tag_parser.add_argument(
        '--add-tag',
        type=str,
        help='要标记的标签列表',
    )
    customers_mark_tag_parser.add_argument(
        '--remove-tag',
        type=str,
        help='要移除的标签列表',
    )

    def _handle_customers_mark_tag(a: argparse.Namespace) -> dict:
        return client.customers_mark_tag(
            userid=a.userid,
            external_userid=a.external_userid,
            add_tag=a.add_tag,
            remove_tag=a.remove_tag,
        )
    table[('customers', 'mark-tag')] = _handle_customers_mark_tag

    customers_message_send_parser = customers_sub.add_parser(
        'message-send',
        help='发送「学校通知」',
    )
    customers_message_send_parser.add_argument(
        '--recv-scope',
        type=int,
        help='TODO: recv_scope',
    )
    customers_message_send_parser.add_argument(
        '--to-parent-userid',
        type=json.loads,
        help='TODO: to_parent_userid',
    )
    customers_message_send_parser.add_argument(
        '--to-student-userid',
        type=json.loads,
        help='TODO: to_student_userid',
    )
    customers_message_send_parser.add_argument(
        '--to-party',
        type=json.loads,
        help='TODO: to_party',
    )
    customers_message_send_parser.add_argument(
        '--toall',
        type=int,
        help='TODO: toall',
    )
    customers_message_send_parser.add_argument(
        '--msgtype',
        type=str,
        help='TODO: msgtype',
    )
    customers_message_send_parser.add_argument(
        '--agentid',
        type=int,
        help='TODO: agentid',
    )
    customers_message_send_parser.add_argument(
        '--text',
        type=json.loads,
        help='TODO: text',
    )
    customers_message_send_parser.add_argument(
        '--enable-id-trans',
        type=int,
        help='TODO: enable_id_trans',
    )
    customers_message_send_parser.add_argument(
        '--enable-duplicate-check',
        type=int,
        help='TODO: enable_duplicate_check',
    )
    customers_message_send_parser.add_argument(
        '--duplicate-check-interval',
        type=int,
        help='TODO: duplicate_check_interval',
    )

    def _handle_customers_message_send(a: argparse.Namespace) -> dict:
        return client.customers_message_send(
            recv_scope=a.recv_scope,
            to_parent_userid=a.to_parent_userid,
            to_student_userid=a.to_student_userid,
            to_party=a.to_party,
            toall=a.toall,
            msgtype=a.msgtype,
            agentid=a.agentid,
            text=a.text,
            enable_id_trans=a.enable_id_trans,
            enable_duplicate_check=a.enable_duplicate_check,
            duplicate_check_interval=a.duplicate_check_interval,
        )
    table[('customers', 'message-send')] = _handle_customers_message_send

    customers_opengid_to_chatid_parser = customers_sub.add_parser(
        'opengid-to-chatid',
        help='客户群opengid转换',
    )
    customers_opengid_to_chatid_parser.add_argument(
        '--opengid',
        type=str,
        required=True,
        help='小程序在微信获取到的群ID，参见wx.getGroupEnterInfo',
    )

    def _handle_customers_opengid_to_chatid(a: argparse.Namespace) -> dict:
        return client.customers_opengid_to_chatid(
            opengid=a.opengid,
        )
    table[('customers', 'opengid-to-chatid')] = _handle_customers_opengid_to_chatid

    customers_remark_parser = customers_sub.add_parser(
        'remark',
        help='修改客户备注信息',
    )
    customers_remark_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='企业成员的userid',
    )
    customers_remark_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='外部联系人userid',
    )
    customers_remark_parser.add_argument(
        '--remark',
        type=str,
        help='此用户对外部联系人的备注，最多20个字符',
    )
    customers_remark_parser.add_argument(
        '--description',
        type=str,
        help='此用户对外部联系人的描述，最多150个字符',
    )
    customers_remark_parser.add_argument(
        '--remark-company',
        type=str,
        help='此用户对外部联系人备注的所属公司名称，最多20个字符',
    )
    customers_remark_parser.add_argument(
        '--remark-mobiles',
        type=str,
        help='此用户对外部联系人备注的手机号',
    )
    customers_remark_parser.add_argument(
        '--remark-pic-mediaid',
        type=str,
        help='备注图片的mediaid，',
    )

    def _handle_customers_remark(a: argparse.Namespace) -> dict:
        return client.customers_remark(
            userid=a.userid,
            external_userid=a.external_userid,
            remark=a.remark,
            description=a.description,
            remark_company=a.remark_company,
            remark_mobiles=a.remark_mobiles,
            remark_pic_mediaid=a.remark_pic_mediaid,
        )
    table[('customers', 'remark')] = _handle_customers_remark

    customers_remind_groupmsg_send_parser = customers_sub.add_parser(
        'remind-groupmsg-send',
        help='提醒成员群发',
    )
    customers_remind_groupmsg_send_parser.add_argument(
        '--msgid',
        type=str,
        required=True,
        help='群发消息的id，通过获取群发记录列表接口返回',
    )

    def _handle_customers_remind_groupmsg_send(a: argparse.Namespace) -> dict:
        return client.customers_remind_groupmsg_send(
            msgid=a.msgid,
        )
    table[('customers', 'remind-groupmsg-send')] = _handle_customers_remind_groupmsg_send

    customers_resigned_transfer_customer_parser = customers_sub.add_parser(
        'resigned-transfer-customer',
        help='分配离职成员的客户',
    )
    customers_resigned_transfer_customer_parser.add_argument(
        '--handover-userid',
        type=str,
        required=True,
        help='原跟进成员的userid',
    )
    customers_resigned_transfer_customer_parser.add_argument(
        '--takeover-userid',
        type=str,
        required=True,
        help='接替成员的userid',
    )
    customers_resigned_transfer_customer_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='客户的external_userid列表，最多一次转移100个客户',
    )

    def _handle_customers_resigned_transfer_customer(a: argparse.Namespace) -> dict:
        return client.customers_resigned_transfer_customer(
            handover_userid=a.handover_userid,
            takeover_userid=a.takeover_userid,
            external_userid=a.external_userid,
        )
    table[('customers', 'resigned-transfer-customer')] = _handle_customers_resigned_transfer_customer

    customers_send_welcome_msg_parser = customers_sub.add_parser(
        'send-welcome-msg',
        help='发送新客户欢迎语',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--welcome-code',
        type=str,
        required=True,
        help='通过添加外部联系人事件推送给企业的发送欢迎语的凭证，有效期为20秒',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--text-content',
        type=str,
        help='消息文本内容,最长为4000字节',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--attachments',
        type=str,
        help='附件，最多可添加9个附件',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--attachments-msgtype',
        type=str,
        required=True,
        help='附件类型，可选image、link、miniprogram或者video',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--image-media-id',
        type=str,
        help='图片的media_id，可以通过素材管理接口获得',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--image-pic-url',
        type=str,
        help='图片的链接，仅可使用上传图片接口得到的链接',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--link-title',
        type=str,
        required=True,
        help='图文消息标题，最长为128字节',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--link-picurl',
        type=str,
        help='图文消息封面的url',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--link-desc',
        type=str,
        help='图文消息的描述，最长为512字节',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--link-url',
        type=str,
        required=True,
        help='图文消息的链接',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--miniprogram-title',
        type=str,
        required=True,
        help='小程序消息标题，最长为64字节',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--miniprogram-pic-media-id',
        type=str,
        required=True,
        help='小程序消息封面的mediaid，封面图建议尺寸为520*416',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--miniprogram-appid',
        type=str,
        required=True,
        help='小程序appid，必须是关联到企业的小程序应用',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--miniprogram-page',
        type=str,
        required=True,
        help='小程序page路径',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--video-media-id',
        type=str,
        required=True,
        help='视频的media_id，可以通过素材管理接口获得',
    )
    customers_send_welcome_msg_parser.add_argument(
        '--file-media-id',
        type=str,
        required=True,
        help='文件的media_id, 可以通过素材管理接口获得',
    )

    def _handle_customers_send_welcome_msg(a: argparse.Namespace) -> dict:
        return client.customers_send_welcome_msg(
            welcome_code=a.welcome_code,
            text_content=a.text_content,
            attachments=a.attachments,
            attachments_msgtype=a.attachments_msgtype,
            image_media_id=a.image_media_id,
            image_pic_url=a.image_pic_url,
            link_title=a.link_title,
            link_picurl=a.link_picurl,
            link_desc=a.link_desc,
            link_url=a.link_url,
            miniprogram_title=a.miniprogram_title,
            miniprogram_pic_media_id=a.miniprogram_pic_media_id,
            miniprogram_appid=a.miniprogram_appid,
            miniprogram_page=a.miniprogram_page,
            video_media_id=a.video_media_id,
            file_media_id=a.file_media_id,
        )
    table[('customers', 'send-welcome-msg')] = _handle_customers_send_welcome_msg

    customers_set_subscribe_mode_parser = customers_sub.add_parser(
        'set-subscribe-mode',
        help='管理「学校通知」的关注模式',
    )
    customers_set_subscribe_mode_parser.add_argument(
        '--subscribe-mode',
        type=str,
        required=True,
        help='关注模式, 1:可扫码填写资料加入, 2:禁止扫码填写资料加入',
    )

    def _handle_customers_set_subscribe_mode(a: argparse.Namespace) -> dict:
        return client.customers_set_subscribe_mode(
            subscribe_mode=a.subscribe_mode,
        )
    table[('customers', 'set-subscribe-mode')] = _handle_customers_set_subscribe_mode

    customers_transfer_customer_parser = customers_sub.add_parser(
        'transfer-customer',
        help='分配在职成员的客户',
    )
    customers_transfer_customer_parser.add_argument(
        '--handover-userid',
        type=str,
        required=True,
        help='原跟进成员的userid',
    )
    customers_transfer_customer_parser.add_argument(
        '--takeover-userid',
        type=str,
        required=True,
        help='接替成员的userid',
    )
    customers_transfer_customer_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='客户的external_userid列表，每次最多分配100个客户',
    )
    customers_transfer_customer_parser.add_argument(
        '--transfer-success-msg',
        type=str,
        help='转移成功后发给客户的消息，最多200个字符，不填则使用默认文案',
    )

    def _handle_customers_transfer_customer(a: argparse.Namespace) -> dict:
        return client.customers_transfer_customer(
            handover_userid=a.handover_userid,
            takeover_userid=a.takeover_userid,
            external_userid=a.external_userid,
            transfer_success_msg=a.transfer_success_msg,
        )
    table[('customers', 'transfer-customer')] = _handle_customers_transfer_customer

    departments_parser = subparsers.add_parser(
        'departments',
        help='departments',
    )
    departments_sub = departments_parser.add_subparsers(dest='__action', required=True)

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

    dial_parser = subparsers.add_parser(
        'dial',
        help='dial',
    )
    dial_sub = dial_parser.add_subparsers(dest='__action', required=True)

    dial_get_dial_record_parser = dial_sub.add_parser(
        'get-dial-record',
        help='获取公费电话拨打记录',
    )
    dial_get_dial_record_parser.add_argument(
        '--start-time',
        type=str,
        help='查询的起始时间戳',
    )
    dial_get_dial_record_parser.add_argument(
        '--end-time',
        type=str,
        help='查询的结束时间戳',
    )
    dial_get_dial_record_parser.add_argument(
        '--offset',
        type=str,
        help='分页查询的偏移量',
    )
    dial_get_dial_record_parser.add_argument(
        '--limit',
        type=str,
        help='分页查询的每页大小,默认为100条，如该参数大于100则按100处理',
    )

    def _handle_dial_get_dial_record(a: argparse.Namespace) -> dict:
        return client.dial_get_dial_record(
            start_time=a.start_time,
            end_time=a.end_time,
            offset=a.offset,
            limit=a.limit,
        )
    table[('dial', 'get-dial-record')] = _handle_dial_get_dial_record

    exmail_parser = subparsers.add_parser(
        'exmail',
        help='exmail',
    )
    exmail_sub = exmail_parser.add_subparsers(dest='__action', required=True)

    exmail_app_compose_send_parser = exmail_sub.add_parser(
        'app-compose-send',
        help='发送会议邮件',
    )
    exmail_app_compose_send_parser.add_argument(
        '--to',
        type=str,
        required=True,
        help='收件人，to.emails 和 to.userids 至少传一个',
    )
    exmail_app_compose_send_parser.add_argument(
        '--to-emails',
        type=str,
        help='收件人，邮箱地址',
    )
    exmail_app_compose_send_parser.add_argument(
        '--to-userids',
        type=str,
        help='收件人，企业内成员的userid',
    )
    exmail_app_compose_send_parser.add_argument(
        '--cc',
        type=str,
        help='抄送',
    )
    exmail_app_compose_send_parser.add_argument(
        '--cc-emails',
        type=str,
        help='抄送人，邮箱地址',
    )
    exmail_app_compose_send_parser.add_argument(
        '--cc-userids',
        type=str,
        help='抄送人，企业内成员的userid',
    )
    exmail_app_compose_send_parser.add_argument(
        '--bcc',
        type=str,
        help='密送',
    )
    exmail_app_compose_send_parser.add_argument(
        '--bcc-emails',
        type=str,
        help='密送人，邮箱地址',
    )
    exmail_app_compose_send_parser.add_argument(
        '--bcc-userids',
        type=str,
        help='密送人，企业内成员的userid',
    )
    exmail_app_compose_send_parser.add_argument(
        '--subject',
        type=str,
        required=True,
        help='邮件标题，同时也是会议标题',
    )
    exmail_app_compose_send_parser.add_argument(
        '--content',
        type=str,
        required=True,
        help='邮件正文，同时是会议描述',
    )
    exmail_app_compose_send_parser.add_argument(
        '--attachment-list',
        type=str,
        help='附件相关',
    )
    exmail_app_compose_send_parser.add_argument(
        '--attachment-list-file-name',
        type=str,
        required=True,
        help='文件名',
    )
    exmail_app_compose_send_parser.add_argument(
        '--attachment-list-content',
        type=str,
        required=True,
        help='文件内容（base64编码），所有附件加正文的大小不允许超过50M, 且附件个数不能超过200个',
    )
    exmail_app_compose_send_parser.add_argument(
        '--content-type',
        type=str,
        help='内容类型 html，text（默认是html）',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule',
        type=str,
        required=True,
        help='会议相关数据，发会议邮件都必须带上这个字段',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-schedule-id',
        type=str,
        help='会议ID (修改/取消会议必须带上schedule_id)',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-method',
        type=str,
        help='会议方法： request-请求（不传schedule_id时是创建会议，传了是修改会议） cancel-取消会议（必须带上schedule_id） 默认为request',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-location',
        type=str,
        help='地点',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-start-time',
        type=int,
        required=True,
        help='会议开始时间，Unix时间戳',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-end-time',
        type=int,
        required=True,
        help='会议结束时间，Unix时间戳',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders',
        type=str,
        help='重复和提醒相关字段',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-is-remind',
        help='是否有提醒 0-不提醒 1-提醒',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-remind-before-event-mins',
        type=int,
        help='会议开始（start_time）前多少分钟提醒，当is_remind=1时有效。例如： 15表示会议开始前15分钟提醒 -15表示会议开始后15分钟提醒',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-timezone',
        type=int,
        help='时区。UTC偏移量表示(即偏离零时区的小时数)，东区为正数，西区为负数。 例如：+8 表示北京时间东八区 默认为北京时间东八区 取值范围：-12 ~ +12',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-is-repeat',
        help='是否重复 0-否 1-是',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-is-custom-repeat',
        help='是否自定义重复 0-否 1-是。当is_repeat为1时有效。',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-repeat-type',
        type=int,
        help='重复类型，当is_repeat=1时有效。目前支持如下类型： 0 - 每日 1 - 每周 2 - 每月 5 - 每年',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-repeat-interval',
        type=int,
        help='重复间隔 仅当指定为自定义重复时有效，该字段随repeat_type不同而含义不同 例如： repeat_interval指定为2，repeat_type指定为每周重复，那么每2周重复一次； repeat_interval指定为2，repeat_type指定为每月重复，那么每2月重复一次',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-repeat-day-of-week',
        type=str,
        help='每周周几重复 仅当指定为自定义重复且重复类型为每周时有效 取值范围：1 ~ 7，分别表示周一至周日',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-repeat-day-of-month',
        type=str,
        help='每月哪几天重复 仅当指定为自定义重复, 且重复类型为每月或每年时有效 取值范围：1 ~ 31，分别表示1~31号',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-repeat-month-of-year',
        type=str,
        help='每年哪几个月重复 仅当指定为自定义重复且重复类型为每年时有效 取值范围：1 ~ 12，分别表示 1月 - 12月（每年重复需要repeat_month_of_year和repeat_day_of_month来指定某一天）',
    )
    exmail_app_compose_send_parser.add_argument(
        '--schedule-reminders-repeat-until',
        type=int,
        help='重复结束时刻，Unix时间戳，当is_repeat=1时有效。不填或填0表示一直重复',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting',
        type=str,
        help='会议相关，会议邮件必填，且必须同时带上schedule，会议的基本设置放在schedule里',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-hosts',
        type=str,
        help='会议主持人列表，最多10个。定义见收件人字段，只支持填userid',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-meeting-admins',
        type=str,
        required=True,
        help='会议管理员字段, , 仅可指定1人，只支持传userid，必须是同企业的用户，且在参与人中',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option',
        type=str,
        help='会议相关设置',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-password',
        type=str,
        help='入会密码，仅可输入4-6位纯数字',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-auto-record',
        help='是否自动录制 0：未开启自动录制，1：开启自动本地录制，2：开启自动云录制；默认不开启',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-enable-waiting-room',
        help='是否开启等候室 false:不开启等候室；true:开启等候室；默认不开',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-allow-enter-before-host',
        help='是否允许成员在主持人进会前加入。 true:允许；false:不允许。默认允许',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-enter-restraint',
        help='是否限制成员入会 0:所有人可入会 2:仅企业内部用户可入会；默认所有人可入会',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-enable-screen-watermark',
        help='是否开启屏幕水印 true:开启；false:不开启。默认不开启',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-enable-enter-mute',
        help='成员入会时是否静音 1:开启；0:关闭；2:超过6人后自动开启静音。默认超过6人自动开启静音',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-remind-scope',
        help='会议开始时是否提醒 1:不提醒 2:仅提醒主持人 3:提醒所有成员入会; 默认仅提醒主持人',
    )
    exmail_app_compose_send_parser.add_argument(
        '--meeting-option-water-mark-type',
        type=int,
        help='水印类型 0:单排水印 1:多排水印；默认单排水印',
    )
    exmail_app_compose_send_parser.add_argument(
        '--enable-id-trans',
        help='表示是否开启id转译，0表示否，1表示是，默认0。仅第三方应用需要用到，企业自建应用可以忽略。 目前仅subject、content、attachment_list[].file_name字段支持转译。',
    )

    def _handle_exmail_app_compose_send(a: argparse.Namespace) -> dict:
        return client.exmail_app_compose_send(
            to=a.to,
            to_emails=a.to_emails,
            to_userids=a.to_userids,
            cc=a.cc,
            cc_emails=a.cc_emails,
            cc_userids=a.cc_userids,
            bcc=a.bcc,
            bcc_emails=a.bcc_emails,
            bcc_userids=a.bcc_userids,
            subject=a.subject,
            content=a.content,
            attachment_list=a.attachment_list,
            attachment_list_file_name=a.attachment_list_file_name,
            attachment_list_content=a.attachment_list_content,
            content_type=a.content_type,
            schedule=a.schedule,
            schedule_schedule_id=a.schedule_schedule_id,
            schedule_method=a.schedule_method,
            schedule_location=a.schedule_location,
            schedule_start_time=a.schedule_start_time,
            schedule_end_time=a.schedule_end_time,
            schedule_reminders=a.schedule_reminders,
            schedule_reminders_is_remind=a.schedule_reminders_is_remind,
            schedule_reminders_remind_before_event_mins=a.schedule_reminders_remind_before_event_mins,
            schedule_reminders_timezone=a.schedule_reminders_timezone,
            schedule_reminders_is_repeat=a.schedule_reminders_is_repeat,
            schedule_reminders_is_custom_repeat=a.schedule_reminders_is_custom_repeat,
            schedule_reminders_repeat_type=a.schedule_reminders_repeat_type,
            schedule_reminders_repeat_interval=a.schedule_reminders_repeat_interval,
            schedule_reminders_repeat_day_of_week=a.schedule_reminders_repeat_day_of_week,
            schedule_reminders_repeat_day_of_month=a.schedule_reminders_repeat_day_of_month,
            schedule_reminders_repeat_month_of_year=a.schedule_reminders_repeat_month_of_year,
            schedule_reminders_repeat_until=a.schedule_reminders_repeat_until,
            meeting=a.meeting,
            meeting_hosts=a.meeting_hosts,
            meeting_meeting_admins=a.meeting_meeting_admins,
            meeting_option=a.meeting_option,
            meeting_option_password=a.meeting_option_password,
            meeting_option_auto_record=a.meeting_option_auto_record,
            meeting_option_enable_waiting_room=a.meeting_option_enable_waiting_room,
            meeting_option_allow_enter_before_host=a.meeting_option_allow_enter_before_host,
            meeting_option_enter_restraint=a.meeting_option_enter_restraint,
            meeting_option_enable_screen_watermark=a.meeting_option_enable_screen_watermark,
            meeting_option_enable_enter_mute=a.meeting_option_enable_enter_mute,
            meeting_option_remind_scope=a.meeting_option_remind_scope,
            meeting_option_water_mark_type=a.meeting_option_water_mark_type,
            enable_id_trans=a.enable_id_trans,
        )
    table[('exmail', 'app-compose-send')] = _handle_exmail_app_compose_send

    exmail_sub.add_parser(
        'app-get-email-alias',
        help='查询应用邮箱账号',
    )

    def _handle_exmail_app_get_email_alias(a: argparse.Namespace) -> dict:
        return client.exmail_app_get_email_alias()
    table[('exmail', 'app-get-email-alias')] = _handle_exmail_app_get_email_alias

    exmail_app_read_mail_parser = exmail_sub.add_parser(
        'app-read-mail',
        help='获取邮件内容',
    )
    exmail_app_read_mail_parser.add_argument(
        '--mail-id',
        type=str,
        required=True,
        help='邮件id',
    )

    def _handle_exmail_app_read_mail(a: argparse.Namespace) -> dict:
        return client.exmail_app_read_mail(
            mail_id=a.mail_id,
        )
    table[('exmail', 'app-read-mail')] = _handle_exmail_app_read_mail

    exmail_group_create_parser = exmail_sub.add_parser(
        'group-create',
        help='创建邮件群组',
    )
    exmail_group_create_parser.add_argument(
        '--groupid',
        type=str,
        required=True,
        help='邮件群组ID，邮箱格式',
    )
    exmail_group_create_parser.add_argument(
        '--groupname',
        type=str,
        required=True,
        help='邮件群组名称，不能与其他群组重名，长度限定200字节',
    )
    exmail_group_create_parser.add_argument(
        '--email-list',
        type=str,
        help='群组内成员邮箱地址，读取成员的biz_mail字段，email_list，group_list，department_list，tag_list至少填写一个，不可同时为空。成员由email_list，group_list，department_list，tag_list共同组成',
    )
    exmail_group_create_parser.add_argument(
        '--tag-list',
        type=str,
        help='群组内包含的标签ID',
    )
    exmail_group_create_parser.add_argument(
        '--department-list',
        type=str,
        help='群组内包含的部门ID',
    )
    exmail_group_create_parser.add_argument(
        '--group-list',
        type=str,
        help='群组内包含的群组邮箱',
    )
    exmail_group_create_parser.add_argument(
        '--allow-type',
        type=str,
        help='群组使用权限。0: 企业成员, 1任何人， 2:组内成员，3:自定义成员。当值为0、1、2时，不得传入allow_emaillist，allow_departmentlist，allow_taglist。当值为3时，必须传入allow_emaillist，allow_departmentlist，allow_taglist至少一项',
    )
    exmail_group_create_parser.add_argument(
        '--allow-emaillist',
        type=str,
        help='允许使用群组群发的成员邮箱地址，读取成员的biz_mail字段',
    )
    exmail_group_create_parser.add_argument(
        '--allow-departmentlist',
        type=str,
        help='允许使用群组群发的部门ID',
    )
    exmail_group_create_parser.add_argument(
        '--allow-taglist',
        type=str,
        help='允许使用群组群发的标签ID',
    )

    def _handle_exmail_group_create(a: argparse.Namespace) -> dict:
        return client.exmail_group_create(
            groupid=a.groupid,
            groupname=a.groupname,
            email_list=a.email_list,
            tag_list=a.tag_list,
            department_list=a.department_list,
            group_list=a.group_list,
            allow_type=a.allow_type,
            allow_emaillist=a.allow_emaillist,
            allow_departmentlist=a.allow_departmentlist,
            allow_taglist=a.allow_taglist,
        )
    table[('exmail', 'group-create')] = _handle_exmail_group_create

    exmail_group_delete_parser = exmail_sub.add_parser(
        'group-delete',
        help='删除邮件群组',
    )
    exmail_group_delete_parser.add_argument(
        '--groupid',
        type=str,
        required=True,
        help='邮件群组ID，邮箱格式',
    )

    def _handle_exmail_group_delete(a: argparse.Namespace) -> dict:
        return client.exmail_group_delete(
            groupid=a.groupid,
        )
    table[('exmail', 'group-delete')] = _handle_exmail_group_delete

    exmail_group_get_parser = exmail_sub.add_parser(
        'group-get',
        help='获取邮件群组详情',
    )
    exmail_group_get_parser.add_argument(
        '--groupid',
        type=str,
        required=True,
        help='邮件群组ID，邮箱格式',
    )

    def _handle_exmail_group_get(a: argparse.Namespace) -> dict:
        return client.exmail_group_get(
            groupid=a.groupid,
        )
    table[('exmail', 'group-get')] = _handle_exmail_group_get

    exmail_group_search_parser = exmail_sub.add_parser(
        'group-search',
        help='模糊搜索邮件群组',
    )
    exmail_group_search_parser.add_argument(
        '--fuzzy',
        type=str,
        required=True,
        help='1开启模糊搜索，0获取全部邮件群组',
    )
    exmail_group_search_parser.add_argument(
        '--groupid',
        type=str,
        help='邮件群组ID，邮箱格式',
    )

    def _handle_exmail_group_search(a: argparse.Namespace) -> dict:
        return client.exmail_group_search(
            fuzzy=a.fuzzy,
            groupid=a.groupid,
        )
    table[('exmail', 'group-search')] = _handle_exmail_group_search

    exmail_group_update_parser = exmail_sub.add_parser(
        'group-update',
        help='更新邮件群组',
    )
    exmail_group_update_parser.add_argument(
        '--groupid',
        type=str,
        required=True,
        help='邮件群组ID，邮箱格式',
    )
    exmail_group_update_parser.add_argument(
        '--groupname',
        type=str,
        help='邮件群组名称，不能与其他群组重名，长度限定200字节',
    )
    exmail_group_update_parser.add_argument(
        '--email-list',
        type=str,
        help='群组内成员邮箱地址，读取成员的biz_mail字段，不传则不变，传空则清空。成员由email_list，group_list，department_list，tag_list共同组成，不允许全部清空',
    )
    exmail_group_update_parser.add_argument(
        '--tag-list',
        type=str,
        help='群组内包含的标签ID，不传则不变，传空为清空',
    )
    exmail_group_update_parser.add_argument(
        '--department-list',
        type=str,
        help='群组内包含的部门ID，不传则不变，传空为清空',
    )
    exmail_group_update_parser.add_argument(
        '--group-list',
        type=str,
        help='群组内包含的群组邮箱ID，不传则不变，传空为清空',
    )
    exmail_group_update_parser.add_argument(
        '--allow-type',
        type=str,
        help='群组使用权限。0: 企业成员, 1任何人， 2:组内成员，3:自定义成员。当值为0、1、2时，不得传入allow_emaillist，allow_departmentlist，allow_taglist。当值为3时，必须传入allow_emaillist，allow_departmentlist，allow_taglist至少一项。若不需更新则不传入参数。',
    )
    exmail_group_update_parser.add_argument(
        '--allow-emaillist',
        type=str,
        help='允许使用群组群发的成员邮箱地址，不传则不变，传空为清空',
    )
    exmail_group_update_parser.add_argument(
        '--allow-departmentlist',
        type=str,
        help='允许使用群组群发的部门ID，不传则不变，传空为清空',
    )
    exmail_group_update_parser.add_argument(
        '--allow-taglist',
        type=str,
        help='允许使用群组群发的标签ID，不传则不变，传空为清空',
    )

    def _handle_exmail_group_update(a: argparse.Namespace) -> dict:
        return client.exmail_group_update(
            groupid=a.groupid,
            groupname=a.groupname,
            email_list=a.email_list,
            tag_list=a.tag_list,
            department_list=a.department_list,
            group_list=a.group_list,
            allow_type=a.allow_type,
            allow_emaillist=a.allow_emaillist,
            allow_departmentlist=a.allow_departmentlist,
            allow_taglist=a.allow_taglist,
        )
    table[('exmail', 'group-update')] = _handle_exmail_group_update

    exmail_useroption_update_parser = exmail_sub.add_parser(
        'useroption-update',
        help='更改用户功能属性',
    )
    exmail_useroption_update_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='用户UserID',
    )
    exmail_useroption_update_parser.add_argument(
        '--type',
        required=True,
        help='功能设置属性类型 1: 强制启用安全登录 2: IMAP/SMTP服务 3: POP/SMTP服务 4: 是否启用安全登录',
    )
    exmail_useroption_update_parser.add_argument(
        '--value',
        type=str,
        required=True,
        help='1表示启用，0表示关闭',
    )

    def _handle_exmail_useroption_update(a: argparse.Namespace) -> dict:
        return client.exmail_useroption_update(
            userid=a.userid,
            type=a.type,
            value=a.value,
        )
    table[('exmail', 'useroption-update')] = _handle_exmail_useroption_update

    export_parser = subparsers.add_parser(
        'export',
        help='export',
    )
    export_sub = export_parser.add_subparsers(dest='__action', required=True)

    export_department_parser = export_sub.add_parser(
        'department',
        help='导出部门',
    )
    export_department_parser.add_argument(
        '--encoding-aeskey',
        type=str,
        required=True,
        help='Base64编码后的加密密钥。长度固定为43，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。解码后即为32字节长的AESKey。加密方式采用AES-256-CBC方式，数据采用PKCS#7填充至32字节的倍数；IV初始向量大小为16字节，取AESKey前16字节，详见：https://datatracker.ietf.org/doc/html/rfc2315',
    )
    export_department_parser.add_argument(
        '--block-size',
        type=str,
        help='每块数据的部门数，支持范围[104,106]，默认值为106',
    )

    def _handle_export_department(a: argparse.Namespace) -> dict:
        return client.export_department(
            encoding_aeskey=a.encoding_aeskey,
            block_size=a.block_size,
        )
    table[('export', 'department')] = _handle_export_department

    export_get_result_parser = export_sub.add_parser(
        'get-result',
        help='获取导出结果',
    )
    export_get_result_parser.add_argument(
        '--jobid',
        type=str,
        required=True,
        help='导出任务接口成功后返回',
    )

    def _handle_export_get_result(a: argparse.Namespace) -> dict:
        return client.export_get_result(
            jobid=a.jobid,
        )
    table[('export', 'get-result')] = _handle_export_get_result

    export_simple_user_parser = export_sub.add_parser(
        'simple-user',
        help='导出成员',
    )
    export_simple_user_parser.add_argument(
        '--encoding-aeskey',
        type=str,
        required=True,
        help='Base64编码后的加密密钥。长度固定为43，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。解码后即为32字节长的AESKey。加密方式采用AES-256-CBC方式，数据采用PKCS#7填充至32字节的倍数；IV初始向量大小为16字节，取AESKey前16字节，详见：https://datatracker.ietf.org/doc/html/rfc2315',
    )
    export_simple_user_parser.add_argument(
        '--block-size',
        type=str,
        help='每块数据的人员数，支持范围[104,106]，默认值为106',
    )

    def _handle_export_simple_user(a: argparse.Namespace) -> dict:
        return client.export_simple_user(
            encoding_aeskey=a.encoding_aeskey,
            block_size=a.block_size,
        )
    table[('export', 'simple-user')] = _handle_export_simple_user

    export_taguser_parser = export_sub.add_parser(
        'taguser',
        help='导出标签成员',
    )
    export_taguser_parser.add_argument(
        '--tagid',
        type=str,
        required=True,
        help='需要导出的标签',
    )
    export_taguser_parser.add_argument(
        '--encoding-aeskey',
        type=str,
        required=True,
        help='Base64编码后的加密密钥。长度固定为43，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。解码后即为32字节长的AESKey。加密方式采用AES-256-CBC方式，数据采用PKCS#7填充至32字节的倍数；IV初始向量大小为16字节，取AESKey前16字节，详见：https://datatracker.ietf.org/doc/html/rfc2315',
    )
    export_taguser_parser.add_argument(
        '--block-size',
        type=str,
        help='每块数据的人员数和部门数之和，支持范围[104,106]，默认值为106',
    )

    def _handle_export_taguser(a: argparse.Namespace) -> dict:
        return client.export_taguser(
            tagid=a.tagid,
            encoding_aeskey=a.encoding_aeskey,
            block_size=a.block_size,
        )
    table[('export', 'taguser')] = _handle_export_taguser

    export_user_parser = export_sub.add_parser(
        'user',
        help='导出成员详情',
    )
    export_user_parser.add_argument(
        '--encoding-aeskey',
        type=str,
        required=True,
        help='Base64编码后的加密密钥。长度固定为43，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。解码后即为32字节长的AESKey。加密方式采用AES-256-CBC方式，数据采用PKCS#7填充至32字节的倍数；IV初始向量大小为16字节，取AESKey前16字节，详见：https://datatracker.ietf.org/doc/html/rfc2315',
    )
    export_user_parser.add_argument(
        '--block-size',
        type=str,
        help='每块数据的人员数，支持范围[104,106]，默认值为106',
    )

    def _handle_export_user(a: argparse.Namespace) -> dict:
        return client.export_user(
            encoding_aeskey=a.encoding_aeskey,
            block_size=a.block_size,
        )
    table[('export', 'user')] = _handle_export_user

    externalpay_parser = subparsers.add_parser(
        'externalpay',
        help='externalpay',
    )
    externalpay_sub = externalpay_parser.add_subparsers(dest='__action', required=True)

    externalpay_get_bill_list_parser = externalpay_sub.add_parser(
        'get-bill-list',
        help='获取对外收款记录',
    )
    externalpay_get_bill_list_parser.add_argument(
        '--begin-time',
        type=str,
        required=True,
        help='收款记录开始时间戳，单位为秒',
    )
    externalpay_get_bill_list_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='收款记录结束时间戳，单位为秒',
    )
    externalpay_get_bill_list_parser.add_argument(
        '--payee-userid',
        type=str,
        help='企业收款成员userid，不填则为全部成员',
    )
    externalpay_get_bill_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    externalpay_get_bill_list_parser.add_argument(
        '--limit',
        type=str,
        help='返回的最大记录数，整型，最大值1000',
    )

    def _handle_externalpay_get_bill_list(a: argparse.Namespace) -> dict:
        return client.externalpay_get_bill_list(
            begin_time=a.begin_time,
            end_time=a.end_time,
            payee_userid=a.payee_userid,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('externalpay', 'get-bill-list')] = _handle_externalpay_get_bill_list

    externalpay_get_fund_flow_parser = externalpay_sub.add_parser(
        'get-fund-flow',
        help='获取资金流水',
    )
    externalpay_get_fund_flow_parser.add_argument(
        '--begin-time',
        type=str,
        required=True,
        help='资金流水记录开始时间',
    )
    externalpay_get_fund_flow_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='资金流水记录结束时间',
    )
    externalpay_get_fund_flow_parser.add_argument(
        '--mch-id',
        type=str,
        help='商户号ID，若不填写则拉取所有商户号的资金流水',
    )
    externalpay_get_fund_flow_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    externalpay_get_fund_flow_parser.add_argument(
        '--limit',
        type=str,
        help='返回的最大记录数，默认值100，最大不超过200',
    )

    def _handle_externalpay_get_fund_flow(a: argparse.Namespace) -> dict:
        return client.externalpay_get_fund_flow(
            begin_time=a.begin_time,
            end_time=a.end_time,
            mch_id=a.mch_id,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('externalpay', 'get-fund-flow')] = _handle_externalpay_get_fund_flow

    externalpay_getmerchant_parser = externalpay_sub.add_parser(
        'getmerchant',
        help='收款商户号管理',
    )
    externalpay_getmerchant_parser.add_argument(
        '--mch-id',
        type=str,
        required=True,
        help='微信支付商户号,不超过32字节',
    )

    def _handle_externalpay_getmerchant(a: argparse.Namespace) -> dict:
        return client.externalpay_getmerchant(
            mch_id=a.mch_id,
        )
    table[('externalpay', 'getmerchant')] = _handle_externalpay_getmerchant

    hardware_parser = subparsers.add_parser(
        'hardware',
        help='hardware',
    )
    hardware_sub = hardware_parser.add_subparsers(dest='__action', required=True)

    hardware_get_hardware_checkin_data_parser = hardware_sub.add_parser(
        'get-hardware-checkin-data',
        help='获取设备打卡数据',
    )
    hardware_get_hardware_checkin_data_parser.add_argument(
        '--filter-type',
        type=str,
        help='过滤类型，1表示按打卡时间过滤，2表示按设备上传打卡记录的时间过滤，默认值是1',
    )
    hardware_get_hardware_checkin_data_parser.add_argument(
        '--starttime',
        type=str,
        required=True,
        help='Unix时间戳，当filter_type为1时，表示打卡的开始时间；当filter_type为2时，表示设备上传记录的开始时间',
    )
    hardware_get_hardware_checkin_data_parser.add_argument(
        '--endtime',
        type=str,
        required=True,
        help='Unix时间戳，当filter_type为1时，表示打卡的结束时间；当filter_type为2时，表示设备上传记录的结束时间',
    )
    hardware_get_hardware_checkin_data_parser.add_argument(
        '--useridlist',
        type=str,
        required=True,
        help='需要获取打卡记录的用户列表',
    )

    def _handle_hardware_get_hardware_checkin_data(a: argparse.Namespace) -> dict:
        return client.hardware_get_hardware_checkin_data(
            filter_type=a.filter_type,
            starttime=a.starttime,
            endtime=a.endtime,
            useridlist=a.useridlist,
        )
    table[('hardware', 'get-hardware-checkin-data')] = _handle_hardware_get_hardware_checkin_data

    health_parser = subparsers.add_parser(
        'health',
        help='health',
    )
    health_sub = health_parser.add_subparsers(dest='__action', required=True)

    health_get_health_report_stat_parser = health_sub.add_parser(
        'get-health-report-stat',
        help='获取健康上报使用统计',
    )
    health_get_health_report_stat_parser.add_argument(
        '--date',
        type=str,
        required=True,
        help='具体某天的使用统计，最长支持获取30天前数据',
    )

    def _handle_health_get_health_report_stat(a: argparse.Namespace) -> dict:
        return client.health_get_health_report_stat(
            date=a.date,
        )
    table[('health', 'get-health-report-stat')] = _handle_health_get_health_report_stat

    health_get_report_answer_parser = health_sub.add_parser(
        'get-report-answer',
        help='获取用户填写答案',
    )
    health_get_report_answer_parser.add_argument(
        '--jobid',
        type=str,
        required=True,
        help='任务ID',
    )
    health_get_report_answer_parser.add_argument(
        '--date',
        type=str,
        required=True,
        help='具体某天任务的填写答案，仅支持获取最近14天数据',
    )
    health_get_report_answer_parser.add_argument(
        '--offset',
        type=str,
        help='数据偏移量',
    )
    health_get_report_answer_parser.add_argument(
        '--limit',
        type=str,
        help='拉取的数据量，最大值100',
    )

    def _handle_health_get_report_answer(a: argparse.Namespace) -> dict:
        return client.health_get_report_answer(
            jobid=a.jobid,
            date=a.date,
            offset=a.offset,
            limit=a.limit,
        )
    table[('health', 'get-report-answer')] = _handle_health_get_report_answer

    health_get_report_job_info_parser = health_sub.add_parser(
        'get-report-job-info',
        help='获取健康上报任务详情',
    )
    health_get_report_job_info_parser.add_argument(
        '--jobid',
        type=str,
        required=True,
        help='任务ID',
    )
    health_get_report_job_info_parser.add_argument(
        '--date',
        type=str,
        required=True,
        help='具体某天任务详情，仅支持获取最近14天数据',
    )

    def _handle_health_get_report_job_info(a: argparse.Namespace) -> dict:
        return client.health_get_report_job_info(
            jobid=a.jobid,
            date=a.date,
        )
    table[('health', 'get-report-job-info')] = _handle_health_get_report_job_info

    health_get_report_jobids_parser = health_sub.add_parser(
        'get-report-jobids',
        help='获取健康上报任务ID列表',
    )
    health_get_report_jobids_parser.add_argument(
        '--offset',
        type=str,
        help='分页，偏移量, 默认为0',
    )
    health_get_report_jobids_parser.add_argument(
        '--limit',
        type=str,
        help='分页，预期请求的数据量，默认为100，取值范围 1 ~ 100',
    )

    def _handle_health_get_report_jobids(a: argparse.Namespace) -> dict:
        return client.health_get_report_jobids(
            offset=a.offset,
            limit=a.limit,
        )
    table[('health', 'get-report-jobids')] = _handle_health_get_report_jobids

    hr_parser = subparsers.add_parser(
        'hr',
        help='hr',
    )
    hr_sub = hr_parser.add_subparsers(dest='__action', required=True)

    hr_sub.add_parser(
        'get-fields',
        help='获取员工字段配置',
    )

    def _handle_hr_get_fields(a: argparse.Namespace) -> dict:
        return client.hr_get_fields()
    table[('hr', 'get-fields')] = _handle_hr_get_fields

    hr_get_staff_info_parser = hr_sub.add_parser(
        'get-staff-info',
        help='获取员工花名册信息',
    )
    hr_get_staff_info_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='需要获取花名册信息的员工的userid 该员工需要在调用应用的可见范围内，否则将返回错误码',
    )
    hr_get_staff_info_parser.add_argument(
        '--get-all',
        help='是否获取全部字段信息，不填时默认为否',
    )
    hr_get_staff_info_parser.add_argument(
        '--fieldids',
        type=str,
        help='需要获取的字段信息。 参数get_all为否或不填时，此字段不能为空； 参数get_all为是时，此字段填写的内容将被忽略',
    )
    hr_get_staff_info_parser.add_argument(
        '--fieldids-fieldid',
        type=str,
        required=True,
        help='需要获取的字段id',
    )
    hr_get_staff_info_parser.add_argument(
        '--fieldids-sub-idx',
        type=str,
        help='需要获取的字段下标。 当需要获取的字段属于可重复的组(参考可重复字段组列表)时，需要指定获取组内第几组数据的字段信息，当需要获取的字段不属于可重复的组时，需要为0。 不填时默认为0',
    )

    def _handle_hr_get_staff_info(a: argparse.Namespace) -> dict:
        return client.hr_get_staff_info(
            userid=a.userid,
            get_all=a.get_all,
            fieldids=a.fieldids,
            fieldids_fieldid=a.fieldids_fieldid,
            fieldids_sub_idx=a.fieldids_sub_idx,
        )
    table[('hr', 'get-staff-info')] = _handle_hr_get_staff_info

    hr_update_staff_info_parser = hr_sub.add_parser(
        'update-staff-info',
        help='更新员工花名册信息',
    )
    hr_update_staff_info_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='需要更新花名册信息的员工的userid 该员工需要在调用应用的可见范围内，否则将返回错误码',
    )
    hr_update_staff_info_parser.add_argument(
        '--update-items',
        type=str,
        help='需要更新、增加或清空单个字段的内容，参考更新字段说明。 有一些字段不支持更新，参考不支持更新字段表。 这个字段和remove_items、insert_items字段不能全部为空',
    )
    hr_update_staff_info_parser.add_argument(
        '--remove-items',
        type=str,
        help='可重复的字段组(参考可重复字段组列表)中需要整组字段进行删除的字段组，参考删除字段说明。 这个字段和update_items、insert_items字段不能全部为空',
    )
    hr_update_staff_info_parser.add_argument(
        '--insert-items',
        type=str,
        help='可重复的字段组(参考可重复字段组列表)中需要增加一组字段的字段组，参考增加字段说明。 这个字段和update_items、remove_items字段不能全部为空',
    )

    def _handle_hr_update_staff_info(a: argparse.Namespace) -> dict:
        return client.hr_update_staff_info(
            userid=a.userid,
            update_items=a.update_items,
            remove_items=a.remove_items,
            insert_items=a.insert_items,
        )
    table[('hr', 'update-staff-info')] = _handle_hr_update_staff_info

    idconvert_parser = subparsers.add_parser(
        'idconvert',
        help='idconvert',
    )
    idconvert_sub = idconvert_parser.add_subparsers(dest='__action', required=True)

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

    kf_parser = subparsers.add_parser(
        'kf',
        help='kf',
    )
    kf_sub = kf_parser.add_subparsers(dest='__action', required=True)

    kf_account_add_parser = kf_sub.add_parser(
        'account-add',
        help='添加客服账号',
    )
    kf_account_add_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='客服名称 不多于16个字符',
    )
    kf_account_add_parser.add_argument(
        '--media-id',
        type=str,
        required=True,
        help='客服头像临时素材。可以调用上传临时素材接口获取。 不多于128个字节',
    )

    def _handle_kf_account_add(a: argparse.Namespace) -> dict:
        return client.kf_account_add(
            name=a.name,
            media_id=a.media_id,
        )
    table[('kf', 'account-add')] = _handle_kf_account_add

    kf_account_del_parser = kf_sub.add_parser(
        'account-del',
        help='删除客服账号',
    )
    kf_account_del_parser.add_argument(
        '--open-kfid',
        type=str,
        required=True,
        help='客服账号ID。 不多于64字节',
    )

    def _handle_kf_account_del(a: argparse.Namespace) -> dict:
        return client.kf_account_del(
            open_kfid=a.open_kfid,
        )
    table[('kf', 'account-del')] = _handle_kf_account_del

    kf_get_corp_statistic_parser = kf_sub.add_parser(
        'get-corp-statistic',
        help='获取「客户数据统计」企业汇总数据',
    )
    kf_get_corp_statistic_parser.add_argument(
        '--open-kfid',
        type=str,
        required=True,
        help='客服账号ID',
    )
    kf_get_corp_statistic_parser.add_argument(
        '--start-time',
        type=str,
        required=True,
        help='起始日期的时间戳，填这一天的0时0分0秒（否则系统自动处理为当天的0分0秒）。取值范围：昨天至前180天',
    )
    kf_get_corp_statistic_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='结束日期的时间戳，填这一天的0时0分0秒（否则系统自动处理为当天的0分0秒）。取值范围：昨天至前180天',
    )

    def _handle_kf_get_corp_statistic(a: argparse.Namespace) -> dict:
        return client.kf_get_corp_statistic(
            open_kfid=a.open_kfid,
            start_time=a.start_time,
            end_time=a.end_time,
        )
    table[('kf', 'get-corp-statistic')] = _handle_kf_get_corp_statistic

    kf_get_servicer_statistic_parser = kf_sub.add_parser(
        'get-servicer-statistic',
        help='获取「客户数据统计」接待人员明细数据',
    )
    kf_get_servicer_statistic_parser.add_argument(
        '--open-kfid',
        type=str,
        required=True,
        help='客服账号ID',
    )
    kf_get_servicer_statistic_parser.add_argument(
        '--servicer-userid',
        type=str,
        help='接待人员的userid。第三方应用为密文userid，即open_userid',
    )
    kf_get_servicer_statistic_parser.add_argument(
        '--start-time',
        type=str,
        required=True,
        help='起始日期的时间戳，填当天的0时0分0秒（否则系统自动处理为当天的0分0秒）。取值范围：昨天至前180天',
    )
    kf_get_servicer_statistic_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='结束日期的时间戳，填当天的0时0分0秒（否则系统自动处理为当天的0分0秒）。取值范围：昨天至前180天',
    )

    def _handle_kf_get_servicer_statistic(a: argparse.Namespace) -> dict:
        return client.kf_get_servicer_statistic(
            open_kfid=a.open_kfid,
            servicer_userid=a.servicer_userid,
            start_time=a.start_time,
            end_time=a.end_time,
        )
    table[('kf', 'get-servicer-statistic')] = _handle_kf_get_servicer_statistic

    kf_knowledge_add_group_parser = kf_sub.add_parser(
        'knowledge-add-group',
        help='知识库分组管理',
    )
    kf_knowledge_add_group_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='分组名。不超过12个字',
    )

    def _handle_kf_knowledge_add_group(a: argparse.Namespace) -> dict:
        return client.kf_knowledge_add_group(
            name=a.name,
        )
    table[('kf', 'knowledge-add-group')] = _handle_kf_knowledge_add_group

    kf_knowledge_add_intent_parser = kf_sub.add_parser(
        'knowledge-add-intent',
        help='知识库问答管理',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--group-id',
        type=str,
        required=True,
        help='分组ID',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--question',
        type=str,
        required=True,
        help='主问题',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--question-text',
        type=str,
        required=True,
        help='主问题文本',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--question-text-content',
        type=str,
        required=True,
        help='主问题文本内容。不超过200个字',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--similar-questions',
        type=str,
        help='相似问题',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--similar-questions-items',
        type=str,
        help='相似问题列表。最多支持100个',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--similar-questions-items-text',
        type=str,
        required=True,
        help='相似问题文本',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--similar-questions-items-text-content',
        type=str,
        required=True,
        help='相似问题文本内容。不超过200个字',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--answers',
        type=str,
        required=True,
        help='回答列表。目前仅支持1个',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--answers-text',
        type=str,
        required=True,
        help='回答文本',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--answers-text-content',
        type=str,
        required=True,
        help='回答文本内容。不超过500个字',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--answers-attachments',
        type=str,
        help='回答附件列表。最多支持4个',
    )
    kf_knowledge_add_intent_parser.add_argument(
        '--answers-attachments-1',
        type=str,
        required=True,
        help='回答附件。具体见附录-问答附件类型',
    )

    def _handle_kf_knowledge_add_intent(a: argparse.Namespace) -> dict:
        return client.kf_knowledge_add_intent(
            group_id=a.group_id,
            question=a.question,
            question_text=a.question_text,
            question_text_content=a.question_text_content,
            similar_questions=a.similar_questions,
            similar_questions_items=a.similar_questions_items,
            similar_questions_items_text=a.similar_questions_items_text,
            similar_questions_items_text_content=a.similar_questions_items_text_content,
            answers=a.answers,
            answers_text=a.answers_text,
            answers_text_content=a.answers_text_content,
            answers_attachments=a.answers_attachments,
            answers_attachments_1=a.answers_attachments_1,
        )
    table[('kf', 'knowledge-add-intent')] = _handle_kf_knowledge_add_intent

    kf_send_msg_parser = kf_sub.add_parser(
        'send-msg',
        help='发送消息',
    )
    kf_send_msg_parser.add_argument(
        '--touser',
        type=str,
        help='TODO: touser',
    )
    kf_send_msg_parser.add_argument(
        '--open-kfid',
        type=str,
        help='TODO: open_kfid',
    )
    kf_send_msg_parser.add_argument(
        '--msgid',
        type=str,
        help='TODO: msgid',
    )
    kf_send_msg_parser.add_argument(
        '--msgtype',
        type=str,
        help='TODO: msgtype',
    )
    kf_send_msg_parser.add_argument(
        '--text',
        type=json.loads,
        help='TODO: text',
    )

    def _handle_kf_send_msg(a: argparse.Namespace) -> dict:
        return client.kf_send_msg(
            touser=a.touser,
            open_kfid=a.open_kfid,
            msgid=a.msgid,
            msgtype=a.msgtype,
            text=a.text,
        )
    table[('kf', 'send-msg')] = _handle_kf_send_msg

    kf_send_msg_on_event_parser = kf_sub.add_parser(
        'send-msg-on-event',
        help='发送欢迎语等事件响应消息',
    )
    kf_send_msg_on_event_parser.add_argument(
        '--code',
        type=str,
        required=True,
        help='事件响应消息对应的code。通过事件回调下发，仅可使用一次。',
    )
    kf_send_msg_on_event_parser.add_argument(
        '--msgid',
        type=str,
        help='消息ID。如果请求参数指定了msgid，则原样返回，否则系统自动生成并返回。 不多于32字节 字符串取值范围(正则表达式)：[0-9a-zA-Z_-]*',
    )
    kf_send_msg_on_event_parser.add_argument(
        '--msgtype',
        type=str,
        required=True,
        help='消息类型。对不同的msgtype，有相应的结构描述，详见消息类型',
    )

    def _handle_kf_send_msg_on_event(a: argparse.Namespace) -> dict:
        return client.kf_send_msg_on_event(
            code=a.code,
            msgid=a.msgid,
            msgtype=a.msgtype,
        )
    table[('kf', 'send-msg-on-event')] = _handle_kf_send_msg_on_event

    kf_service_state_get_parser = kf_sub.add_parser(
        'service-state-get',
        help='分配客服会话',
    )
    kf_service_state_get_parser.add_argument(
        '--open-kfid',
        type=str,
        required=True,
        help='客服账号ID',
    )
    kf_service_state_get_parser.add_argument(
        '--external-userid',
        type=str,
        required=True,
        help='微信客户的external_userid',
    )

    def _handle_kf_service_state_get(a: argparse.Namespace) -> dict:
        return client.kf_service_state_get(
            open_kfid=a.open_kfid,
            external_userid=a.external_userid,
        )
    table[('kf', 'service-state-get')] = _handle_kf_service_state_get

    kf_sync_msg_parser = kf_sub.add_parser(
        'sync-msg',
        help='接收消息和事件',
    )
    kf_sync_msg_parser.add_argument(
        '--cursor',
        type=str,
        help='上一次调用时返回的next_cursor，第一次拉取可以不填。若不填，从3天内最早的消息开始返回。 不多于64字节',
    )
    kf_sync_msg_parser.add_argument(
        '--token',
        type=str,
        help='回调事件返回的token字段，10分钟内有效；可不填，如果不填接口有严格的频率限制。 不多于128字节',
    )
    kf_sync_msg_parser.add_argument(
        '--limit',
        type=int,
        help='期望请求的数据量，默认值和最大值都为1000。 注意：可能会出现返回条数少于limit的情况，需结合返回的has_more字段判断是否继续请求。',
    )
    kf_sync_msg_parser.add_argument(
        '--voice-format',
        type=str,
        help='语音消息类型，0-Amr 1-Silk，默认0。可通过该参数控制返回的语音格式，开发者可按需选择自己程序支持的一种格式',
    )
    kf_sync_msg_parser.add_argument(
        '--open-kfid',
        type=str,
        required=True,
        help='指定拉取某个客服账号的消息',
    )

    def _handle_kf_sync_msg(a: argparse.Namespace) -> dict:
        return client.kf_sync_msg(
            cursor=a.cursor,
            token=a.token,
            limit=a.limit,
            voice_format=a.voice_format,
            open_kfid=a.open_kfid,
        )
    table[('kf', 'sync-msg')] = _handle_kf_sync_msg

    living_parser = subparsers.add_parser(
        'living',
        help='living',
    )
    living_sub = living_parser.add_subparsers(dest='__action', required=True)

    living_delete_replay_data_parser = living_sub.add_parser(
        'delete-replay-data',
        help='删除直播回放',
    )
    living_delete_replay_data_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播id',
    )

    def _handle_living_delete_replay_data(a: argparse.Namespace) -> dict:
        return client.living_delete_replay_data(
            livingid=a.livingid,
        )
    table[('living', 'delete-replay-data')] = _handle_living_delete_replay_data

    living_get_living_info_parser = living_sub.add_parser(
        'get-living-info',
        help='获取直播详情',
    )
    living_get_living_info_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播ID',
    )

    def _handle_living_get_living_info(a: argparse.Namespace) -> dict:
        return client.living_get_living_info(
            livingid=a.livingid,
        )
    table[('living', 'get-living-info')] = _handle_living_get_living_info

    living_get_user_all_livingid_parser = living_sub.add_parser(
        'get-user-all-livingid',
        help='获取老师直播ID列表',
    )
    living_get_user_all_livingid_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='企业成员的userid',
    )
    living_get_user_all_livingid_parser.add_argument(
        '--cursor',
        type=str,
        help='上一次调用时返回的next_cursor，第一次拉取可以不填',
    )
    living_get_user_all_livingid_parser.add_argument(
        '--limit',
        type=str,
        help='每次拉取的数据量，默认值和最大值都为100',
    )

    def _handle_living_get_user_all_livingid(a: argparse.Namespace) -> dict:
        return client.living_get_user_all_livingid(
            userid=a.userid,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('living', 'get-user-all-livingid')] = _handle_living_get_user_all_livingid

    meeting_parser = subparsers.add_parser(
        'meeting',
        help='meeting',
    )
    meeting_sub = meeting_parser.add_subparsers(dest='__action', required=True)

    meeting_cancel_parser = meeting_sub.add_parser(
        'cancel',
        help='取消预约会议',
    )
    meeting_cancel_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议id，仅允许取消预约状态下的会议',
    )

    def _handle_meeting_cancel(a: argparse.Namespace) -> dict:
        return client.meeting_cancel(
            meetingid=a.meetingid,
        )
    table[('meeting', 'cancel')] = _handle_meeting_cancel

    meeting_create_parser = meeting_sub.add_parser(
        'create',
        help='创建预约会议',
    )
    meeting_create_parser.add_argument(
        '--admin-userid',
        type=str,
        required=True,
        help='会议管理员userid',
    )
    meeting_create_parser.add_argument(
        '--title',
        type=str,
        required=True,
        help='会议的标题，最多支持40个字节或者20个utf8字符',
    )
    meeting_create_parser.add_argument(
        '--meeting-start',
        type=str,
        required=True,
        help='会议开始时间的unix时间戳。需大于当前时间',
    )
    meeting_create_parser.add_argument(
        '--meeting-duration',
        type=str,
        required=True,
        help='会议持续时间（单位秒），最小300秒，最大86399秒',
    )
    meeting_create_parser.add_argument(
        '--description',
        type=str,
        help='会议的描述，最多支持500个字节或者utf8字符',
    )
    meeting_create_parser.add_argument(
        '--location',
        type=str,
        help='会议地点,最多128个字符',
    )
    meeting_create_parser.add_argument(
        '--agentid',
        type=str,
        help='授权方安装的应用agentid。仅旧的第三方多应用套件需要填此参数',
    )
    meeting_create_parser.add_argument(
        '--invitees',
        type=str,
        help='邀请参会的成员。任何userid不合法或者不在应用可见范围，直接报错。参会人数上限不超过指定的「管理员」可预约的人数的上限，普通企业参会人员最多为100人；付费企业由企业选购的在线会议室或高级账号对应的容量决定，但最多为300人，超过300人请调用更新会议受邀成员列表接口。',
    )
    meeting_create_parser.add_argument(
        '--invitees-userid',
        type=str,
        help='参与会议的企业成员userid',
    )
    meeting_create_parser.add_argument(
        '--cal-id',
        type=str,
        help='会议所属日历ID。该日历必须是access_token所对应应用所创建的日历。 注意，若参与人在日历分享范围内，则插入到该日历（同时会插入会议参与人的默认日历），若不在分享范围内，否则仅插入到参与者默认日历； 如果不填，那么插入到参与者的默认日历上。 第三方应用必须指定cal_id 不多于64字节',
    )
    meeting_create_parser.add_argument(
        '--settings',
        type=str,
        help='会议配置，详见Settings',
    )
    meeting_create_parser.add_argument(
        '--reminders',
        type=str,
        help='重复会议相关配置，详见Reminders',
    )

    def _handle_meeting_create(a: argparse.Namespace) -> dict:
        return client.meeting_create(
            admin_userid=a.admin_userid,
            title=a.title,
            meeting_start=a.meeting_start,
            meeting_duration=a.meeting_duration,
            description=a.description,
            location=a.location,
            agentid=a.agentid,
            invitees=a.invitees,
            invitees_userid=a.invitees_userid,
            cal_id=a.cal_id,
            settings=a.settings,
            reminders=a.reminders,
        )
    table[('meeting', 'create')] = _handle_meeting_create

    meeting_create_customer_short_url_parser = meeting_sub.add_parser(
        'create-customer-short-url',
        help='创建用户专属参会链接',
    )
    meeting_create_customer_short_url_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_create_customer_short_url_parser.add_argument(
        '--customer-data',
        type=str,
        required=True,
        help='用户专属字段，长度不超过256字节。customer_data 需以 {"ver": "1.0", "userData":"自定义字段"} 的结构，进行 Base64编码。',
    )

    def _handle_meeting_create_customer_short_url(a: argparse.Namespace) -> dict:
        return client.meeting_create_customer_short_url(
            meetingid=a.meetingid,
            customer_data=a.customer_data,
        )
    table[('meeting', 'create-customer-short-url')] = _handle_meeting_create_customer_short_url

    meeting_enroll_approve_parser = meeting_sub.add_parser(
        'enroll-approve',
        help='审批会议报名信息',
    )
    meeting_enroll_approve_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_enroll_approve_parser.add_argument(
        '--action',
        type=str,
        required=True,
        help='审批动作： 1：取消批准 2：拒绝 3：批准 说明：取消批准后状态将变成待审批。',
    )
    meeting_enroll_approve_parser.add_argument(
        '--enroll-id-list',
        type=str,
        required=True,
        help='报名ID列表',
    )

    def _handle_meeting_enroll_approve(a: argparse.Namespace) -> dict:
        return client.meeting_enroll_approve(
            meetingid=a.meetingid,
            action=a.action,
            enroll_id_list=a.enroll_id_list,
        )
    table[('meeting', 'enroll-approve')] = _handle_meeting_enroll_approve

    meeting_enroll_delete_parser = meeting_sub.add_parser(
        'enroll-delete',
        help='删除会议报名信息',
    )
    meeting_enroll_delete_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_enroll_delete_parser.add_argument(
        '--enroll-id-list',
        type=str,
        required=True,
        help='报名ID列表。详见EnrollID。',
    )

    def _handle_meeting_enroll_delete(a: argparse.Namespace) -> dict:
        return client.meeting_enroll_delete(
            meetingid=a.meetingid,
            enroll_id_list=a.enroll_id_list,
        )
    table[('meeting', 'enroll-delete')] = _handle_meeting_enroll_delete

    meeting_enroll_import_parser = meeting_sub.add_parser(
        'enroll-import',
        help='导入会议报名信息',
    )
    meeting_enroll_import_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_enroll_import_parser.add_argument(
        '--enroll-list',
        type=str,
        required=True,
        help='报名成员列表。详见EnrollRequest。',
    )

    def _handle_meeting_enroll_import(a: argparse.Namespace) -> dict:
        return client.meeting_enroll_import(
            meetingid=a.meetingid,
            enroll_list=a.enroll_list,
        )
    table[('meeting', 'enroll-import')] = _handle_meeting_enroll_import

    meeting_enroll_set_config_parser = meeting_sub.add_parser(
        'enroll-set-config',
        help='修改会议报名配置',
    )
    meeting_enroll_set_config_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_enroll_set_config_parser.add_argument(
        '--approve-type',
        type=str,
        help='审批类型： 1：自动审批，默认自动审批。 2：手动审批。',
    )
    meeting_enroll_set_config_parser.add_argument(
        '--is-collect-question',
        help='是否收集问题： 1：不收集，默认不收集问题。 2：收集。',
    )
    meeting_enroll_set_config_parser.add_argument(
        '--question-list',
        type=str,
        help='报名问题列表，非特殊问题按传入的顺序排序，特殊问题会优先放在最前面，仅开启收集问题时有效。详见Question。',
    )
    meeting_enroll_set_config_parser.add_argument(
        '--no-registration-needed-for-staff',
        help='本企业成员无需报名。 true：本企业成员无需报名。 false：默认配置，本企业成员及企业外成员需要报名。',
    )

    def _handle_meeting_enroll_set_config(a: argparse.Namespace) -> dict:
        return client.meeting_enroll_set_config(
            meetingid=a.meetingid,
            approve_type=a.approve_type,
            is_collect_question=a.is_collect_question,
            question_list=a.question_list,
            no_registration_needed_for_staff=a.no_registration_needed_for_staff,
        )
    table[('meeting', 'enroll-set-config')] = _handle_meeting_enroll_set_config

    meeting_get_customer_short_url_parser = meeting_sub.add_parser(
        'get-customer-short-url',
        help='获取用户专属参会链接',
    )
    meeting_get_customer_short_url_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )

    def _handle_meeting_get_customer_short_url(a: argparse.Namespace) -> dict:
        return client.meeting_get_customer_short_url(
            meetingid=a.meetingid,
        )
    table[('meeting', 'get-customer-short-url')] = _handle_meeting_get_customer_short_url

    meeting_get_info_parser = meeting_sub.add_parser(
        'get-info',
        help='获取会议详情',
    )
    meeting_get_info_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议id',
    )

    def _handle_meeting_get_info(a: argparse.Namespace) -> dict:
        return client.meeting_get_info(
            meetingid=a.meetingid,
        )
    table[('meeting', 'get-info')] = _handle_meeting_get_info

    meeting_get_invitees_parser = meeting_sub.add_parser(
        'get-invitees',
        help='获取会议受邀成员列表',
    )
    meeting_get_invitees_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议id',
    )
    meeting_get_invitees_parser.add_argument(
        '--cursor',
        type=str,
        help='分页查询用，将上一个请求返回的next_cursor字段传入。第一次查询时可不传值',
    )

    def _handle_meeting_get_invitees(a: argparse.Namespace) -> dict:
        return client.meeting_get_invitees(
            meetingid=a.meetingid,
            cursor=a.cursor,
        )
    table[('meeting', 'get-invitees')] = _handle_meeting_get_invitees

    meeting_get_user_meetingid_parser = meeting_sub.add_parser(
        'get-user-meetingid',
        help='获取成员会议ID列表',
    )
    meeting_get_user_meetingid_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='企业成员的userid',
    )
    meeting_get_user_meetingid_parser.add_argument(
        '--cursor',
        type=str,
        help='上一次调用时返回的cursor，初次调用可以填"0"',
    )
    meeting_get_user_meetingid_parser.add_argument(
        '--limit',
        type=str,
        help='每次拉取的数据量，默认值和最大值都为100',
    )
    meeting_get_user_meetingid_parser.add_argument(
        '--begin-time',
        type=str,
        help='开始时间',
    )
    meeting_get_user_meetingid_parser.add_argument(
        '--end-time',
        type=str,
        help='结束时间，时间跨度不超过180天。如果begin_time和end_time都没填的话，默认end_time为当前时间。',
    )

    def _handle_meeting_get_user_meetingid(a: argparse.Namespace) -> dict:
        return client.meeting_get_user_meetingid(
            userid=a.userid,
            cursor=a.cursor,
            limit=a.limit,
            begin_time=a.begin_time,
            end_time=a.end_time,
        )
    table[('meeting', 'get-user-meetingid')] = _handle_meeting_get_user_meetingid

    meeting_layout_add_background_parser = meeting_sub.add_parser(
        'layout-add-background',
        help='添加会议背景',
    )
    meeting_layout_add_background_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议 ID',
    )
    meeting_layout_add_background_parser.add_argument(
        '--image-list',
        type=str,
        required=True,
        help='图片对象列表，详见Image',
    )
    meeting_layout_add_background_parser.add_argument(
        '--default-image-order',
        type=str,
        help='图片列表中会议需要使用的背景图片序号，从1开始计数。不填默认为1',
    )

    def _handle_meeting_layout_add_background(a: argparse.Namespace) -> dict:
        return client.meeting_layout_add_background(
            meetingid=a.meetingid,
            image_list=a.image_list,
            default_image_order=a.default_image_order,
        )
    table[('meeting', 'layout-add-background')] = _handle_meeting_layout_add_background

    meeting_layout_batch_delete_background_parser = meeting_sub.add_parser(
        'layout-batch-delete-background',
        help='批量删除会议背景',
    )
    meeting_layout_batch_delete_background_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议 ID',
    )
    meeting_layout_batch_delete_background_parser.add_argument(
        '--background-id-list',
        type=str,
        required=True,
        help='背景 ID 列表',
    )

    def _handle_meeting_layout_batch_delete_background(a: argparse.Namespace) -> dict:
        return client.meeting_layout_batch_delete_background(
            meetingid=a.meetingid,
            background_id_list=a.background_id_list,
        )
    table[('meeting', 'layout-batch-delete-background')] = _handle_meeting_layout_batch_delete_background

    meeting_layout_delete_background_parser = meeting_sub.add_parser(
        'layout-delete-background',
        help='删除会议背景',
    )
    meeting_layout_delete_background_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议 ID',
    )
    meeting_layout_delete_background_parser.add_argument(
        '--background-id',
        type=str,
        required=True,
        help='背景 ID',
    )

    def _handle_meeting_layout_delete_background(a: argparse.Namespace) -> dict:
        return client.meeting_layout_delete_background(
            meetingid=a.meetingid,
            background_id=a.background_id,
        )
    table[('meeting', 'layout-delete-background')] = _handle_meeting_layout_delete_background

    meeting_layout_set_default_parser = meeting_sub.add_parser(
        'layout-set-default',
        help='设置会议默认布局',
    )
    meeting_layout_set_default_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议 ID',
    )
    meeting_layout_set_default_parser.add_argument(
        '--selected-layout-id',
        type=str,
        required=True,
        help='会议应用的布局 ID（若送空""，表示恢复成会议自带的默认原始布局）',
    )

    def _handle_meeting_layout_set_default(a: argparse.Namespace) -> dict:
        return client.meeting_layout_set_default(
            meetingid=a.meetingid,
            selected_layout_id=a.selected_layout_id,
        )
    table[('meeting', 'layout-set-default')] = _handle_meeting_layout_set_default

    meeting_layout_set_default_background_parser = meeting_sub.add_parser(
        'layout-set-default-background',
        help='设置会议默认背景',
    )
    meeting_layout_set_default_background_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议 ID',
    )
    meeting_layout_set_default_background_parser.add_argument(
        '--selected-background-id',
        type=str,
        required=True,
        help='会议应用的背景 ID（若送空""，则表示恢复成会议默认的黑色背景）',
    )

    def _handle_meeting_layout_set_default_background(a: argparse.Namespace) -> dict:
        return client.meeting_layout_set_default_background(
            meetingid=a.meetingid,
            selected_background_id=a.selected_background_id,
        )
    table[('meeting', 'layout-set-default-background')] = _handle_meeting_layout_set_default_background

    meeting_mra_set_default_layout_parser = meeting_sub.add_parser(
        'mra-set-default-layout',
        help='切换 MRA 默认布局',
    )
    meeting_mra_set_default_layout_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_mra_set_default_layout_parser.add_argument(
        '--default-layout',
        type=str,
        required=True,
        help='当前成员的默认分屏设置： 1：等分模式 2：全屏模式 3：1+N',
    )
    meeting_mra_set_default_layout_parser.add_argument(
        '--default-novideo-user',
        type=str,
        required=True,
        help='默认非视频与会者在分屏中显示方式： 1：显示 2：隐藏',
    )
    meeting_mra_set_default_layout_parser.add_argument(
        '--mra-tmp-openid',
        type=str,
        required=True,
        help='被操作 mra 设备 的会中临时ID',
    )

    def _handle_meeting_mra_set_default_layout(a: argparse.Namespace) -> dict:
        return client.meeting_mra_set_default_layout(
            meetingid=a.meetingid,
            default_layout=a.default_layout,
            default_novideo_user=a.default_novideo_user,
            mra_tmp_openid=a.mra_tmp_openid,
        )
    table[('meeting', 'mra-set-default-layout')] = _handle_meeting_mra_set_default_layout

    meeting_mra_set_raise_hand_parser = meeting_sub.add_parser(
        'mra-set-raise-hand',
        help='设置 MRA 举手或手放下',
    )
    meeting_mra_set_raise_hand_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_mra_set_raise_hand_parser.add_argument(
        '--raise-hand',
        required=True,
        help='MRA 设备举手操作： true：举手 false：手放下',
    )
    meeting_mra_set_raise_hand_parser.add_argument(
        '--mra-tmp-openid',
        type=str,
        required=True,
        help='被操作 mra 设备 的会中临时ID',
    )

    def _handle_meeting_mra_set_raise_hand(a: argparse.Namespace) -> dict:
        return client.meeting_mra_set_raise_hand(
            meetingid=a.meetingid,
            raise_hand=a.raise_hand,
            mra_tmp_openid=a.mra_tmp_openid,
        )
    table[('meeting', 'mra-set-raise-hand')] = _handle_meeting_mra_set_raise_hand

    meeting_phone_callout_parser = meeting_sub.add_parser(
        'phone-callout',
        help='批量外呼',
    )
    meeting_phone_callout_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_phone_callout_parser.add_argument(
        '--phone-numbers',
        type=str,
        required=True,
        help='外呼的电话号码对象数组。详见PhoneNumber。',
    )

    def _handle_meeting_phone_callout(a: argparse.Namespace) -> dict:
        return client.meeting_phone_callout(
            meetingid=a.meetingid,
            phone_numbers=a.phone_numbers,
        )
    table[('meeting', 'phone-callout')] = _handle_meeting_phone_callout

    meeting_poll_create_theme_parser = meeting_sub.add_parser(
        'poll-create-theme',
        help='创建会议投票主题',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--operator-userid',
        type=str,
        required=True,
        help='操作者的openid',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--instance-id',
        type=int,
        required=True,
        help='操作者入会所用的设备id',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--poll-topic',
        type=str,
        required=True,
        help='投票主题，最多50个字符。',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--poll-desc',
        type=str,
        required=True,
        help='投票主题描述，最多100个字符。',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--is-anony',
        help='是否匿名。 0：实名，默认值 1：匿名',
    )
    meeting_poll_create_theme_parser.add_argument(
        '--poll-questions',
        type=str,
        required=True,
        help='投票问题数组，每个投票支持添加10个问题。详见Question',
    )

    def _handle_meeting_poll_create_theme(a: argparse.Namespace) -> dict:
        return client.meeting_poll_create_theme(
            operator_userid=a.operator_userid,
            instance_id=a.instance_id,
            meetingid=a.meetingid,
            poll_topic=a.poll_topic,
            poll_desc=a.poll_desc,
            is_anony=a.is_anony,
            poll_questions=a.poll_questions,
        )
    table[('meeting', 'poll-create-theme')] = _handle_meeting_poll_create_theme

    meeting_poll_delete_parser = meeting_sub.add_parser(
        'poll-delete',
        help='删除会议投票',
    )
    meeting_poll_delete_parser.add_argument(
        '--operator-userid',
        type=str,
        required=True,
        help='操作者的openid',
    )
    meeting_poll_delete_parser.add_argument(
        '--instance-id',
        type=int,
        required=True,
        help='操作者入会的设备id',
    )
    meeting_poll_delete_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_poll_delete_parser.add_argument(
        '--poll-theme-id',
        type=str,
        help='投票主题 ID，传入则代表删除投票主题，删除投票主题不影响投票实例。 投票主题 ID 和投票 ID 二选一，如果都传入，会使用投票 ID。',
    )
    meeting_poll_delete_parser.add_argument(
        '--poll-id',
        type=str,
        help='投票 ID，传入则代表删除投票实例。当主题下所有主题实例被删，则投票主题也被删除。 投票主题 ID 和投票 ID 二选一，如果都传入，会使用投票 ID。',
    )

    def _handle_meeting_poll_delete(a: argparse.Namespace) -> dict:
        return client.meeting_poll_delete(
            operator_userid=a.operator_userid,
            instance_id=a.instance_id,
            meetingid=a.meetingid,
            poll_theme_id=a.poll_theme_id,
            poll_id=a.poll_id,
        )
    table[('meeting', 'poll-delete')] = _handle_meeting_poll_delete

    meeting_poll_finish_parser = meeting_sub.add_parser(
        'poll-finish',
        help='结束会议投票',
    )
    meeting_poll_finish_parser.add_argument(
        '--operator-userid',
        type=str,
        required=True,
        help='操作者openid',
    )
    meeting_poll_finish_parser.add_argument(
        '--instance-id',
        type=int,
        required=True,
        help='操作者入会设备id',
    )
    meeting_poll_finish_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_poll_finish_parser.add_argument(
        '--poll-theme-id',
        type=str,
        required=True,
        help='投票主题ID',
    )
    meeting_poll_finish_parser.add_argument(
        '--poll-id',
        type=str,
        required=True,
        help='投票 ID',
    )

    def _handle_meeting_poll_finish(a: argparse.Namespace) -> dict:
        return client.meeting_poll_finish(
            operator_userid=a.operator_userid,
            instance_id=a.instance_id,
            meetingid=a.meetingid,
            poll_theme_id=a.poll_theme_id,
            poll_id=a.poll_id,
        )
    table[('meeting', 'poll-finish')] = _handle_meeting_poll_finish

    meeting_poll_start_parser = meeting_sub.add_parser(
        'poll-start',
        help='发起会议投票',
    )
    meeting_poll_start_parser.add_argument(
        '--operator-userid',
        type=str,
        required=True,
        help='操作者openid',
    )
    meeting_poll_start_parser.add_argument(
        '--instance-id',
        type=int,
        required=True,
        help='操作者入会的设备id',
    )
    meeting_poll_start_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_poll_start_parser.add_argument(
        '--poll-theme-id',
        type=str,
        required=True,
        help='投票主题 ID',
    )

    def _handle_meeting_poll_start(a: argparse.Namespace) -> dict:
        return client.meeting_poll_start(
            operator_userid=a.operator_userid,
            instance_id=a.instance_id,
            meetingid=a.meetingid,
            poll_theme_id=a.poll_theme_id,
        )
    table[('meeting', 'poll-start')] = _handle_meeting_poll_start

    meeting_poll_update_theme_parser = meeting_sub.add_parser(
        'poll-update-theme',
        help='修改会议投票主题',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--operator-userid',
        type=str,
        required=True,
        help='操作者openid',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--instance-id',
        type=int,
        required=True,
        help='操作者入会设备对应的id',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--poll-theme-id',
        type=str,
        required=True,
        help='投票主题id',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--poll-topic',
        type=str,
        required=True,
        help='投票主题，最多50个字符。',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--poll-desc',
        type=str,
        required=True,
        help='投票主题描述，最多100个字符。',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--is-anony',
        help='是否匿名。 0：实名，默认值 1：匿名',
    )
    meeting_poll_update_theme_parser.add_argument(
        '--poll-questions',
        type=str,
        required=True,
        help='投票问题数组，每个投票支持添加10个问题。详见Question',
    )

    def _handle_meeting_poll_update_theme(a: argparse.Namespace) -> dict:
        return client.meeting_poll_update_theme(
            operator_userid=a.operator_userid,
            instance_id=a.instance_id,
            meetingid=a.meetingid,
            poll_theme_id=a.poll_theme_id,
            poll_topic=a.poll_topic,
            poll_desc=a.poll_desc,
            is_anony=a.is_anony,
            poll_questions=a.poll_questions,
        )
    table[('meeting', 'poll-update-theme')] = _handle_meeting_poll_update_theme

    meeting_realcontrol_dismiss_parser = meeting_sub.add_parser(
        'realcontrol-dismiss',
        help='结束会议',
    )
    meeting_realcontrol_dismiss_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_realcontrol_dismiss_parser.add_argument(
        '--force-dismiss',
        help='是否强制结束会议，默认值为1： 0：不强制结束会议，会议中有参会者，则无法强制结束会议 1 ：强制结束会议，会议中有参会者，也会强制结束会议',
    )
    meeting_realcontrol_dismiss_parser.add_argument(
        '--retrieve-code',
        help='是否回收会议号，默认值为0： 0：不回收会议号，可以重新入会 1： 回收会议号，不可重新入会 说明：周期性会议如果还有子会议，需设置为不回收会议号，否则会导致后续子会议无法正常进行。 此字段对快速会议不生效，快速会议会强制收回会议号。',
    )

    def _handle_meeting_realcontrol_dismiss(a: argparse.Namespace) -> dict:
        return client.meeting_realcontrol_dismiss(
            meetingid=a.meetingid,
            force_dismiss=a.force_dismiss,
            retrieve_code=a.retrieve_code,
        )
    table[('meeting', 'realcontrol-dismiss')] = _handle_meeting_realcontrol_dismiss

    meeting_record_delete_parser = meeting_sub.add_parser(
        'record-delete',
        help='删除会议录制',
    )
    meeting_record_delete_parser.add_argument(
        '--meeting-record-id',
        type=str,
        required=True,
        help='会议录制ID',
    )
    meeting_record_delete_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )

    def _handle_meeting_record_delete(a: argparse.Namespace) -> dict:
        return client.meeting_record_delete(
            meeting_record_id=a.meeting_record_id,
            meetingid=a.meetingid,
        )
    table[('meeting', 'record-delete')] = _handle_meeting_record_delete

    meeting_record_delete_file_parser = meeting_sub.add_parser(
        'record-delete-file',
        help='删除单个录制文件',
    )
    meeting_record_delete_file_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议D',
    )
    meeting_record_delete_file_parser.add_argument(
        '--record-file-id',
        type=str,
        required=True,
        help='录制文件ID',
    )

    def _handle_meeting_record_delete_file(a: argparse.Namespace) -> dict:
        return client.meeting_record_delete_file(
            meetingid=a.meetingid,
            record_file_id=a.record_file_id,
        )
    table[('meeting', 'record-delete-file')] = _handle_meeting_record_delete_file

    meeting_record_update_sharing_config_parser = meeting_sub.add_parser(
        'record-update-sharing-config',
        help='修改会议录制共享设置',
    )
    meeting_record_update_sharing_config_parser.add_argument(
        '--meeting-record-id',
        type=str,
        required=True,
        help='会议录制ID',
    )
    meeting_record_update_sharing_config_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_record_update_sharing_config_parser.add_argument(
        '--sharing-config',
        type=str,
        help='共享配置，详见SharingConfig',
    )

    def _handle_meeting_record_update_sharing_config(a: argparse.Namespace) -> dict:
        return client.meeting_record_update_sharing_config(
            meeting_record_id=a.meeting_record_id,
            meetingid=a.meetingid,
            sharing_config=a.sharing_config,
        )
    table[('meeting', 'record-update-sharing-config')] = _handle_meeting_record_update_sharing_config

    meeting_statistics_get_start_list_parser = meeting_sub.add_parser(
        'statistics-get-start-list',
        help='获取会议发起记录',
    )
    meeting_statistics_get_start_list_parser.add_argument(
        '--type',
        type=int,
        required=True,
        help='查询类型。 1:发起成功的会议记录 2:发起失败的会议（企业同时发起的会议数已达上限，员工无法发起）',
    )
    meeting_statistics_get_start_list_parser.add_argument(
        '--begin-time',
        type=int,
        required=True,
        help='查询范围起始时间戳，单位为秒',
    )
    meeting_statistics_get_start_list_parser.add_argument(
        '--end-time',
        type=int,
        required=True,
        help='查询范围结束时间戳，单位为秒',
    )
    meeting_statistics_get_start_list_parser.add_argument(
        '--limit',
        type=int,
        help='每次拉取的数据量，默认值200，最大值1000',
    )
    meeting_statistics_get_start_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，由上一次调用返回，首次调用可不填',
    )

    def _handle_meeting_statistics_get_start_list(a: argparse.Namespace) -> dict:
        return client.meeting_statistics_get_start_list(
            type=a.type,
            begin_time=a.begin_time,
            end_time=a.end_time,
            limit=a.limit,
            cursor=a.cursor,
        )
    table[('meeting', 'statistics-get-start-list')] = _handle_meeting_statistics_get_start_list

    meeting_update_parser = meeting_sub.add_parser(
        'update',
        help='修改预约会议',
    )
    meeting_update_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议id，仅允许修改预约状态下的会议',
    )
    meeting_update_parser.add_argument(
        '--title',
        type=str,
        help='会议的标题，最多支持40个字节或者20个utf8字符',
    )
    meeting_update_parser.add_argument(
        '--meeting-start',
        type=str,
        help='会议开始时间的unix时间戳。需大于当前时间。注：修改该字段时必须同时指定meeting_duration。对于非周期性会议，如果创建会议时指定的开始时间小于当前时间，则在更新会议时需要指定meeting_start',
    )
    meeting_update_parser.add_argument(
        '--meeting-duration',
        type=str,
        help='会议持续时间（单位秒），最小300秒 ，最大86399秒。注：修改该字段时，必须同时指定meeting_start。对于非周期性会议，如果创建会议时指定的开始时间小于当前时间，则在更新会议时需要指定meeting_duration',
    )
    meeting_update_parser.add_argument(
        '--description',
        type=str,
        help='会议的描述，最多支持500个字节或者utf8字符',
    )
    meeting_update_parser.add_argument(
        '--location',
        type=str,
        help='会议地点,最多128个字符',
    )
    meeting_update_parser.add_argument(
        '--remind-time',
        type=str,
        help='指定会议开始前多久提醒成员，相对于meeting_start前的秒数，默认为0',
    )
    meeting_update_parser.add_argument(
        '--agentid',
        type=str,
        help='授权方安装的应用agentid。仅旧的第三方多应用套件需要填此参数',
    )
    meeting_update_parser.add_argument(
        '--invitees',
        type=str,
        help='邀请参会的成员。任何userid不合法或者不在应用可见范围，直接报错。参会人数上限不超过指定的「管理员」可预约的人数的上限，普通企业参会人员最多为100人；付费企业不超过企业选购的在线会议室容量，但最多为300人，超过300人请调用更新会议受邀成员列表接口',
    )
    meeting_update_parser.add_argument(
        '--invitees-userid',
        type=str,
        help='参与会议的企业成员userid',
    )
    meeting_update_parser.add_argument(
        '--cal-id',
        type=str,
        help='会议所属日历ID。该日历必须是access_token所对应应用所创建的日历。 注意，若参与人在日历分享范围内，则插入到该日历（同时会插入会议参与人的默认日历），若不在分享范围内，否则仅插入到参与者默认日历； 如果不填，那么插入到参与者的默认日历上。 第三方应用必须指定cal_id 不多于64字节',
    )
    meeting_update_parser.add_argument(
        '--settings',
        type=str,
        help='会议配置，详见Settings',
    )
    meeting_update_parser.add_argument(
        '--reminders',
        type=str,
        help='重复会议相关配置，详见Reminders',
    )

    def _handle_meeting_update(a: argparse.Namespace) -> dict:
        return client.meeting_update(
            meetingid=a.meetingid,
            title=a.title,
            meeting_start=a.meeting_start,
            meeting_duration=a.meeting_duration,
            description=a.description,
            location=a.location,
            remind_time=a.remind_time,
            agentid=a.agentid,
            invitees=a.invitees,
            invitees_userid=a.invitees_userid,
            cal_id=a.cal_id,
            settings=a.settings,
            reminders=a.reminders,
        )
    table[('meeting', 'update')] = _handle_meeting_update

    meeting_vip_list_parser = meeting_sub.add_parser(
        'vip-list',
        help='获取高级功能账号列表',
    )
    meeting_vip_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    meeting_vip_list_parser.add_argument(
        '--limit',
        type=int,
        help='用于分页查询，每次请求返回的数据上限。默认100，最大200 注意：不保证每次返回的数据刚好为指定limit，必须用返回的has_more判断是否继续请求',
    )

    def _handle_meeting_vip_list(a: argparse.Namespace) -> dict:
        return client.meeting_vip_list(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('meeting', 'vip-list')] = _handle_meeting_vip_list

    meeting_vip_submit_batch_add_job_parser = meeting_sub.add_parser(
        'vip-submit-batch-add-job',
        help='分配高级功能账号',
    )
    meeting_vip_submit_batch_add_job_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要分配高级功能的企业成员userid列表，单次操作最大限制100个',
    )

    def _handle_meeting_vip_submit_batch_add_job(a: argparse.Namespace) -> dict:
        return client.meeting_vip_submit_batch_add_job(
            userid_list=a.userid_list,
        )
    table[('meeting', 'vip-submit-batch-add-job')] = _handle_meeting_vip_submit_batch_add_job

    meeting_vip_submit_batch_del_job_parser = meeting_sub.add_parser(
        'vip-submit-batch-del-job',
        help='取消高级功能账号',
    )
    meeting_vip_submit_batch_del_job_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要撤销分配高级功能的企业成员userid列表，单次操作最多限制100个',
    )

    def _handle_meeting_vip_submit_batch_del_job(a: argparse.Namespace) -> dict:
        return client.meeting_vip_submit_batch_del_job(
            userid_list=a.userid_list,
        )
    table[('meeting', 'vip-submit-batch-del-job')] = _handle_meeting_vip_submit_batch_del_job

    meeting_waitingroom_get_current_user_list_parser = meeting_sub.add_parser(
        'waitingroom-get-current-user-list',
        help='获取实时等候室成员列表',
    )
    meeting_waitingroom_get_current_user_list_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='会议ID',
    )
    meeting_waitingroom_get_current_user_list_parser.add_argument(
        '--limit',
        type=str,
        help='分页大小，默认10，最大50',
    )
    meeting_waitingroom_get_current_user_list_parser.add_argument(
        '--cursor',
        type=str,
        help='分页查询用，将上一个请求返回的next_cursor字段传入。第一次查询时可不传值',
    )

    def _handle_meeting_waitingroom_get_current_user_list(a: argparse.Namespace) -> dict:
        return client.meeting_waitingroom_get_current_user_list(
            meetingid=a.meetingid,
            limit=a.limit,
            cursor=a.cursor,
        )
    table[('meeting', 'waitingroom-get-current-user-list')] = _handle_meeting_waitingroom_get_current_user_list

    meeting_webinar_cancel_parser = meeting_sub.add_parser(
        'webinar-cancel',
        help='取消网络研讨会',
    )
    meeting_webinar_cancel_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='网络研讨会ID。',
    )

    def _handle_meeting_webinar_cancel(a: argparse.Namespace) -> dict:
        return client.meeting_webinar_cancel(
            meetingid=a.meetingid,
        )
    table[('meeting', 'webinar-cancel')] = _handle_meeting_webinar_cancel

    meeting_webinar_create_parser = meeting_sub.add_parser(
        'webinar-create',
        help='创建网络研讨会',
    )
    meeting_webinar_create_parser.add_argument(
        '--admin-userid',
        type=str,
        required=True,
        help='网络研讨会管理员userid。',
    )
    meeting_webinar_create_parser.add_argument(
        '--title',
        type=str,
        required=True,
        help='网络研讨会主题（1~255位字符长度）。',
    )
    meeting_webinar_create_parser.add_argument(
        '--sponsor',
        type=str,
        help='主办方名称（1~40位字符长度）。',
    )
    meeting_webinar_create_parser.add_argument(
        '--start-time',
        type=str,
        required=True,
        help='会议开始时间戳（单位秒），不能少于当前时间戳半小时以上。',
    )
    meeting_webinar_create_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='会议结束时间戳（单位秒）。',
    )
    meeting_webinar_create_parser.add_argument(
        '--admission-type',
        type=str,
        required=True,
        help='观众观看限制类型： 0：公开 1：报名 2：密码',
    )
    meeting_webinar_create_parser.add_argument(
        '--hosts',
        type=str,
        help='主持人的成员 ID，默认为网络研讨会管理员admin_userid。 注意：修改时传入，则会覆盖原有设置。详见HostInfo 。',
    )
    meeting_webinar_create_parser.add_argument(
        '--password',
        type=str,
        help='观众观看密码（4~6位数字），当 admission_type = 2 时必传，且仅当 admission_type = 2 时才生效。',
    )
    meeting_webinar_create_parser.add_argument(
        '--cover-url',
        type=str,
        help='封面图片 URL，图片仅支持 PNG 和 JPEG 格式，分辨率需大于640360，推荐使用1280720的高清图片，文件需控制在 5 MB 以内。 该参数需要开启活动页配置（activity_page）。 接口上传封面方式为异步上传，可通过订阅 素材上传结果 获得上传结果通知。',
    )
    meeting_webinar_create_parser.add_argument(
        '--description',
        type=str,
        help='网络研讨会描述详情，仅支持纯文本，1~5000位字符长度。 该参数需要开启活动页配置（activity_page）。',
    )
    meeting_webinar_create_parser.add_argument(
        '--enable-guest-invite-link',
        help='是否开启通过邀请链接自动成为嘉宾： true：开启 false：不开启，默认 false。',
    )
    meeting_webinar_create_parser.add_argument(
        '--media-setting',
        type=str,
        help='媒体参数配置。详见MediaSetting。',
    )
    meeting_webinar_create_parser.add_argument(
        '--enable-qa',
        help='是否开启问答： true：开启 false：不开启，默认 true。',
    )
    meeting_webinar_create_parser.add_argument(
        '--sensitive-words',
        type=str,
        help='聊天敏感词，包含敏感词的观众公共聊天将不会出现在您的会议中，最多可添加50个敏感词，单个敏感词限制10个中文字符长度。',
    )
    meeting_webinar_create_parser.add_argument(
        '--enable-manual-check',
        help='是否开启人工审核： true：开启 false：不开启，默认 false。',
    )
    meeting_webinar_create_parser.add_argument(
        '--activity-page',
        help='活动页开启配置： true：开启活动页，默认开启。 false：不开启活动页。 查询时返回默认值true。',
    )
    meeting_webinar_create_parser.add_argument(
        '--display-number-of-attendees',
        type=str,
        help='活动页展示已报名或已预约人数： 0：不展示 1：展示，默认开启。 该参数需要开启活动页配置（activity_page）。',
    )
    meeting_webinar_create_parser.add_argument(
        '--playback-for-audience',
        required=True,
        help='允许观众观看回放。 true：允许 false：不允许，默认值为 false 开启本选项时必须开启云录制，即 auto_record_type 的值必须为 cloud。',
    )
    meeting_webinar_create_parser.add_argument(
        '--preparation-mode',
        help='是否开启准备模式： true：开启 false：关闭',
    )

    def _handle_meeting_webinar_create(a: argparse.Namespace) -> dict:
        return client.meeting_webinar_create(
            admin_userid=a.admin_userid,
            title=a.title,
            sponsor=a.sponsor,
            start_time=a.start_time,
            end_time=a.end_time,
            admission_type=a.admission_type,
            hosts=a.hosts,
            password=a.password,
            cover_url=a.cover_url,
            description=a.description,
            enable_guest_invite_link=a.enable_guest_invite_link,
            media_setting=a.media_setting,
            enable_qa=a.enable_qa,
            sensitive_words=a.sensitive_words,
            enable_manual_check=a.enable_manual_check,
            activity_page=a.activity_page,
            display_number_of_attendees=a.display_number_of_attendees,
            playback_for_audience=a.playback_for_audience,
            preparation_mode=a.preparation_mode,
        )
    table[('meeting', 'webinar-create')] = _handle_meeting_webinar_create

    meeting_webinar_enroll_approve_parser = meeting_sub.add_parser(
        'webinar-enroll-approve',
        help='审批网络研讨会报名信息',
    )
    meeting_webinar_enroll_approve_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='网络研讨会 ID',
    )
    meeting_webinar_enroll_approve_parser.add_argument(
        '--enroll-id-list',
        type=str,
        required=True,
        help='报名 ID 列表',
    )
    meeting_webinar_enroll_approve_parser.add_argument(
        '--action',
        type=str,
        required=True,
        help='审批动作： 1：取消批准 2：拒绝 3：批准 取消批准后状态将变成待审批。',
    )

    def _handle_meeting_webinar_enroll_approve(a: argparse.Namespace) -> dict:
        return client.meeting_webinar_enroll_approve(
            meetingid=a.meetingid,
            enroll_id_list=a.enroll_id_list,
            action=a.action,
        )
    table[('meeting', 'webinar-enroll-approve')] = _handle_meeting_webinar_enroll_approve

    meeting_webinar_enroll_delete_parser = meeting_sub.add_parser(
        'webinar-enroll-delete',
        help='删除网络研讨会报名信息',
    )
    meeting_webinar_enroll_delete_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='网络研讨会ID',
    )
    meeting_webinar_enroll_delete_parser.add_argument(
        '--enroll-id-list',
        type=str,
        required=True,
        help='报名ID列表。详见EnrollID。',
    )

    def _handle_meeting_webinar_enroll_delete(a: argparse.Namespace) -> dict:
        return client.meeting_webinar_enroll_delete(
            meetingid=a.meetingid,
            enroll_id_list=a.enroll_id_list,
        )
    table[('meeting', 'webinar-enroll-delete')] = _handle_meeting_webinar_enroll_delete

    meeting_webinar_enroll_import_parser = meeting_sub.add_parser(
        'webinar-enroll-import',
        help='导入网络研讨会报名信息',
    )
    meeting_webinar_enroll_import_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='网络研讨会ID',
    )
    meeting_webinar_enroll_import_parser.add_argument(
        '--enroll-list',
        type=str,
        required=True,
        help='报名成员列表。详见EnrollRequest。',
    )

    def _handle_meeting_webinar_enroll_import(a: argparse.Namespace) -> dict:
        return client.meeting_webinar_enroll_import(
            meetingid=a.meetingid,
            enroll_list=a.enroll_list,
        )
    table[('meeting', 'webinar-enroll-import')] = _handle_meeting_webinar_enroll_import

    meeting_webinar_update_parser = meeting_sub.add_parser(
        'webinar-update',
        help='修改网络研讨会',
    )
    meeting_webinar_update_parser.add_argument(
        '--meetingid',
        type=str,
        required=True,
        help='网络研讨会ID。',
    )
    meeting_webinar_update_parser.add_argument(
        '--title',
        type=str,
        required=True,
        help='网络研讨会主题（1~255位字符长度）。',
    )
    meeting_webinar_update_parser.add_argument(
        '--sponsor',
        type=str,
        help='主办方名称（1~40位字符长度）。',
    )
    meeting_webinar_update_parser.add_argument(
        '--start-time',
        type=str,
        required=True,
        help='会议开始时间戳（单位秒），不能少于当前时间戳半小时以上。',
    )
    meeting_webinar_update_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='会议结束时间戳（单位秒）。',
    )
    meeting_webinar_update_parser.add_argument(
        '--admission-type',
        type=str,
        required=True,
        help='观众观看限制类型： 0：公开 1：报名 2：密码',
    )
    meeting_webinar_update_parser.add_argument(
        '--hosts',
        type=str,
        help='主持人的成员 ID，默认为网络研讨会管理员admin_userid。 注意：修改时传入，则会覆盖原有设置。详见HostInfo 。',
    )
    meeting_webinar_update_parser.add_argument(
        '--password',
        type=str,
        help='观众观看密码（4~6位数字），当 admission_type = 2 时必传，且仅当 admission_type = 2 时才生效。',
    )
    meeting_webinar_update_parser.add_argument(
        '--cover-url',
        type=str,
        help='封面图片 URL，图片仅支持 PNG 和 JPEG 格式，分辨率需大于640360，推荐使用1280720的高清图片，文件需控制在 5 MB 以内。 该参数需要开启活动页配置（activity_page）。 接口上传封面方式为异步上传，可通过订阅 素材上传结果 获得上传结果通知。',
    )
    meeting_webinar_update_parser.add_argument(
        '--description',
        type=str,
        help='网络研讨会描述详情，仅支持纯文本，1~5000位字符长度。 该参数需要开启活动页配置（activity_page）。',
    )
    meeting_webinar_update_parser.add_argument(
        '--enable-guest-invite-link',
        help='是否开启通过邀请链接自动成为嘉宾： true：开启 false：不开启，默认 false。',
    )
    meeting_webinar_update_parser.add_argument(
        '--media-setting',
        type=str,
        help='媒体参数配置。详见MediaSetting。',
    )
    meeting_webinar_update_parser.add_argument(
        '--enable-qa',
        help='是否开启问答： true：开启 false：不开启，默认 true。',
    )
    meeting_webinar_update_parser.add_argument(
        '--sensitive-words',
        type=str,
        help='聊天敏感词，包含敏感词的观众公共聊天将不会出现在您的会议中，最多可添加50个敏感词，单个敏感词限制10个中文字符长度。',
    )
    meeting_webinar_update_parser.add_argument(
        '--enable-manual-check',
        help='是否开启人工审核： true：开启 false：不开启，默认 false。',
    )
    meeting_webinar_update_parser.add_argument(
        '--activity-page',
        help='活动页开启配置： true：开启活动页，默认开启。 false：不开启活动页。 查询时返回默认值true。',
    )
    meeting_webinar_update_parser.add_argument(
        '--display-number-of-attendees',
        type=str,
        help='活动页展示已报名或已预约人数： 0：不展示 1：展示，默认开启。 该参数需要开启活动页配置（activity_page）。',
    )
    meeting_webinar_update_parser.add_argument(
        '--playback-for-audience',
        required=True,
        help='允许观众观看回放。 true：允许 false：不允许，默认值为 false 开启本选项时必须开启云录制，即 auto_record_type 的值必须为 cloud。',
    )
    meeting_webinar_update_parser.add_argument(
        '--preparation-mode',
        help='是否开启准备模式： true：开启 false：关闭',
    )

    def _handle_meeting_webinar_update(a: argparse.Namespace) -> dict:
        return client.meeting_webinar_update(
            meetingid=a.meetingid,
            title=a.title,
            sponsor=a.sponsor,
            start_time=a.start_time,
            end_time=a.end_time,
            admission_type=a.admission_type,
            hosts=a.hosts,
            password=a.password,
            cover_url=a.cover_url,
            description=a.description,
            enable_guest_invite_link=a.enable_guest_invite_link,
            media_setting=a.media_setting,
            enable_qa=a.enable_qa,
            sensitive_words=a.sensitive_words,
            enable_manual_check=a.enable_manual_check,
            activity_page=a.activity_page,
            display_number_of_attendees=a.display_number_of_attendees,
            playback_for_audience=a.playback_for_audience,
            preparation_mode=a.preparation_mode,
        )
    table[('meeting', 'webinar-update')] = _handle_meeting_webinar_update

    messages_parser = subparsers.add_parser(
        'messages',
        help='messages',
    )
    messages_sub = messages_parser.add_subparsers(dest='__action', required=True)

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
    messages_send_text_parser.add_argument(
        '--touser',
        type=str,
        help='TODO: touser',
    )
    messages_send_text_parser.add_argument(
        '--toparty',
        type=str,
        help='TODO: toparty',
    )
    messages_send_text_parser.add_argument(
        '--totag',
        type=str,
        help='TODO: totag',
    )
    messages_send_text_parser.add_argument(
        '--msgtype',
        type=str,
        help='TODO: msgtype',
    )
    messages_send_text_parser.add_argument(
        '--agentid',
        type=int,
        help='TODO: agentid',
    )
    messages_send_text_parser.add_argument(
        '--text',
        type=json.loads,
        help='TODO: text',
    )
    messages_send_text_parser.add_argument(
        '--safe',
        type=int,
        help='TODO: safe',
    )
    messages_send_text_parser.add_argument(
        '--enable-id-trans',
        type=int,
        help='TODO: enable_id_trans',
    )
    messages_send_text_parser.add_argument(
        '--enable-duplicate-check',
        type=int,
        help='TODO: enable_duplicate_check',
    )
    messages_send_text_parser.add_argument(
        '--duplicate-check-interval',
        type=int,
        help='TODO: duplicate_check_interval',
    )

    def _handle_messages_send_text(a: argparse.Namespace) -> dict:
        return client.messages_send_text(
            to_user=a.to_user,
            agent_id=a.agent_id,
            content=a.content,
            touser=a.touser,
            toparty=a.toparty,
            totag=a.totag,
            msgtype=a.msgtype,
            agentid=a.agentid,
            text=a.text,
            safe=a.safe,
            enable_id_trans=a.enable_id_trans,
            enable_duplicate_check=a.enable_duplicate_check,
            duplicate_check_interval=a.duplicate_check_interval,
        )
    table[('messages', 'send-text')] = _handle_messages_send_text

    messages_recall_parser = messages_sub.add_parser(
        'recall',
        help='撤回应用消息',
    )
    messages_recall_parser.add_argument(
        '--msgid',
        type=str,
        required=True,
        help='消息ID。从应用发送消息接口处获得。',
    )

    def _handle_messages_recall(a: argparse.Namespace) -> dict:
        return client.messages_recall(
            msgid=a.msgid,
        )
    table[('messages', 'recall')] = _handle_messages_recall

    miniapppay_parser = subparsers.add_parser(
        'miniapppay',
        help='miniapppay',
    )
    miniapppay_sub = miniapppay_parser.add_subparsers(dest='__action', required=True)

    miniapppay_close_order_parser = miniapppay_sub.add_parser(
        'close-order',
        help='关闭订单',
    )
    miniapppay_close_order_parser.add_argument(
        '--商户号',
        type=str,
        required=True,
        help='二级商户号，由企业微信生成并下发。',
    )
    miniapppay_close_order_parser.add_argument(
        '--商户订单号',
        type=str,
        required=True,
        help='商户系统内部订单号，只能是数字、大小 写字母_-*且在同一个商户号下唯一。',
    )

    def _handle_miniapppay_close_order(a: argparse.Namespace) -> dict:
        return client.miniapppay_close_order(
            商户号=a.商户号,
            商户订单号=a.商户订单号,
        )
    table[('miniapppay', 'close-order')] = _handle_miniapppay_close_order

    miniapppay_create_order_parser = miniapppay_sub.add_parser(
        'create-order',
        help='小程序下单',
    )
    miniapppay_create_order_parser.add_argument(
        '--应用ID',
        type=str,
        required=True,
        help='二级商户申请的公众号或移动应用appid。',
    )
    miniapppay_create_order_parser.add_argument(
        '--商户号',
        type=str,
        required=True,
        help='二级商户号，由企业微信生成并下发。',
    )
    miniapppay_create_order_parser.add_argument(
        '--商户订单号',
        type=str,
        required=True,
        help='商户系统内部订单号，只能是数字、大小写字母、_-|* 且在同一个商户号下唯一。',
    )
    miniapppay_create_order_parser.add_argument(
        '--商品描述',
        type=str,
        required=True,
        help='商品描述',
    )
    miniapppay_create_order_parser.add_argument(
        '--下单场景key',
        type=str,
        help='用来统计企微成员发出小程序的交易业绩，可从小程序URL获取。统计结果将在对外收款-成员业绩中展示。若不传入该项，则不做统计。',
    )
    miniapppay_create_order_parser.add_argument(
        '--订单总金额',
        type=int,
        required=True,
        help='订单总金额，单位为分。',
    )
    miniapppay_create_order_parser.add_argument(
        '--货币类型',
        type=str,
        required=True,
        help='CNY：人民币，境内商户号仅支持人民币。',
    )
    miniapppay_create_order_parser.add_argument(
        '--支付者标识',
        type=str,
        required=True,
        help='用户在子商户appid下的唯一标识。',
    )
    miniapppay_create_order_parser.add_argument(
        '--交易结束时间',
        type=str,
        help='订单失效时间，遵循rfc3339标准，格式为 yyyy-MM-DDTHH:mm:ss+TIMEZONE',
    )
    miniapppay_create_order_parser.add_argument(
        '--附加数据',
        type=str,
        help='附加数据，在查单和支付通知中原样返回',
    )
    miniapppay_create_order_parser.add_argument(
        '--订单优惠标记',
        type=str,
        help='订单优惠标记',
    )
    miniapppay_create_order_parser.add_argument(
        '--订单原价',
        type=int,
        help='1、商户侧一张小票订单可能被分多次支付，订单原价用于记录整张小票的交易金额。 2、当订单原价与支付金额不相等，则不享受优惠。 3、该字段主要用于防止同一张小票分多次支付，以享受多次优惠的情况，正常支付订单不必上传此参数。',
    )
    miniapppay_create_order_parser.add_argument(
        '--商品小票ID',
        type=str,
        help='商家小票ID',
    )
    miniapppay_create_order_parser.add_argument(
        '--商户侧商品编码',
        type=str,
        required=True,
        help='由半角的大小写字母、数字、中划线、下划线中的一种或几种组成。',
    )
    miniapppay_create_order_parser.add_argument(
        '--微信支付商品编码',
        type=str,
        help='微信支付定义的统一商品编号（没有可不传）',
    )
    miniapppay_create_order_parser.add_argument(
        '--商品名称',
        type=str,
        help='商品的实际名称',
    )
    miniapppay_create_order_parser.add_argument(
        '--商品数量',
        type=int,
        required=True,
        help='用户购买的数量',
    )
    miniapppay_create_order_parser.add_argument(
        '--商品单价',
        type=int,
        required=True,
        help='商品单价，单位为分',
    )
    miniapppay_create_order_parser.add_argument(
        '--用户终端IP',
        type=str,
        required=True,
        help='用户的客户端IP，支持IPv4和IPv6两种格式的IP地址。',
    )
    miniapppay_create_order_parser.add_argument(
        '--商户端设备号',
        type=str,
        help='商户端设备号（门店号或收银设备ID）。',
    )
    miniapppay_create_order_parser.add_argument(
        '--门店编号',
        type=str,
        required=True,
        help='商户侧门店编号',
    )
    miniapppay_create_order_parser.add_argument(
        '--门店名称',
        type=str,
        help='商户侧门店名称',
    )
    miniapppay_create_order_parser.add_argument(
        '--地区编码',
        type=str,
        help='地区编码，详细请见省市区编号对照表。',
    )
    miniapppay_create_order_parser.add_argument(
        '--详细地址',
        type=str,
        help='详细的商户门店地址',
    )

    def _handle_miniapppay_create_order(a: argparse.Namespace) -> dict:
        return client.miniapppay_create_order(
            应用ID=a.应用ID,
            商户号=a.商户号,
            商户订单号=a.商户订单号,
            商品描述=a.商品描述,
            下单场景key=a.下单场景key,
            订单总金额=a.订单总金额,
            货币类型=a.货币类型,
            支付者标识=a.支付者标识,
            交易结束时间=a.交易结束时间,
            附加数据=a.附加数据,
            订单优惠标记=a.订单优惠标记,
            订单原价=a.订单原价,
            商品小票ID=a.商品小票ID,
            商户侧商品编码=a.商户侧商品编码,
            微信支付商品编码=a.微信支付商品编码,
            商品名称=a.商品名称,
            商品数量=a.商品数量,
            商品单价=a.商品单价,
            用户终端IP=a.用户终端IP,
            商户端设备号=a.商户端设备号,
            门店编号=a.门店编号,
            门店名称=a.门店名称,
            地区编码=a.地区编码,
            详细地址=a.详细地址,
        )
    table[('miniapppay', 'create-order')] = _handle_miniapppay_create_order

    miniapppay_get_applyment_status_parser = miniapppay_sub.add_parser(
        'get-applyment-status',
        help='查询申请单状态',
    )
    miniapppay_get_applyment_status_parser.add_argument(
        '--out-request-no',
        type=str,
        required=True,
        help='业务申请编号，长度限制为1~32个字符，在提交创建对外收款账户的申请单中提交',
    )

    def _handle_miniapppay_get_applyment_status(a: argparse.Namespace) -> dict:
        return client.miniapppay_get_applyment_status(
            out_request_no=a.out_request_no,
        )
    table[('miniapppay', 'get-applyment-status')] = _handle_miniapppay_get_applyment_status

    miniapppay_get_order_parser = miniapppay_sub.add_parser(
        'get-order',
        help='查询订单',
    )
    miniapppay_get_order_parser.add_argument(
        '--商户号',
        type=str,
        required=True,
        help='二级商户号，由企业微信生成并下发。',
    )
    miniapppay_get_order_parser.add_argument(
        '--商户订单号',
        type=str,
        required=True,
        help='商户系统内部订单号，只能是数字、大小 写字母_-*且在同一个商户号下唯一。',
    )

    def _handle_miniapppay_get_order(a: argparse.Namespace) -> dict:
        return client.miniapppay_get_order(
            商户号=a.商户号,
            商户订单号=a.商户订单号,
        )
    table[('miniapppay', 'get-order')] = _handle_miniapppay_get_order

    miniapppay_get_refund_detail_parser = miniapppay_sub.add_parser(
        'get-refund-detail',
        help='查询退款',
    )
    miniapppay_get_refund_detail_parser.add_argument(
        '--商户号',
        type=str,
        required=True,
        help='企业微信分配的商户号。 示例值：1900000109',
    )
    miniapppay_get_refund_detail_parser.add_argument(
        '--商户退款单号',
        type=str,
        required=True,
        help='商户系统内部的退款单号，商户系统内部唯一，只能是数字、大小写字母_-|*@，同一退款单号多次请求只退一笔。 示例值：1217752501201407033233368018',
    )

    def _handle_miniapppay_get_refund_detail(a: argparse.Namespace) -> dict:
        return client.miniapppay_get_refund_detail(
            商户号=a.商户号,
            商户退款单号=a.商户退款单号,
        )
    table[('miniapppay', 'get-refund-detail')] = _handle_miniapppay_get_refund_detail

    miniapppay_get_sign_parser = miniapppay_sub.add_parser(
        'get-sign',
        help='获取支付签名',
    )
    miniapppay_get_sign_parser.add_argument(
        '--应用ID',
        type=str,
        required=True,
        help='二级商户申请的公众号或移动应用appid。',
    )
    miniapppay_get_sign_parser.add_argument(
        '--预支付交易会话标识',
        type=str,
        required=True,
        help='小程序下单接口返回的prepay_id参数值.仅支持下单两小时内的prepay_id',
    )
    miniapppay_get_sign_parser.add_argument(
        '--签名方式',
        type=str,
        help='签名类型，默认为RSA，仅支持RSA。',
    )
    miniapppay_get_sign_parser.add_argument(
        '--随机字符串',
        type=str,
        required=True,
        help='随机字符串，不长于32位，内容仅支持数字、大小写字母。',
    )
    miniapppay_get_sign_parser.add_argument(
        '--时间戳',
        type=int,
        required=True,
        help='当前的秒级时间戳',
    )

    def _handle_miniapppay_get_sign(a: argparse.Namespace) -> dict:
        return client.miniapppay_get_sign(
            应用ID=a.应用ID,
            预支付交易会话标识=a.预支付交易会话标识,
            签名方式=a.签名方式,
            随机字符串=a.随机字符串,
            时间戳=a.时间戳,
        )
    table[('miniapppay', 'get-sign')] = _handle_miniapppay_get_sign

    miniapppay_refund_parser = miniapppay_sub.add_parser(
        'refund',
        help='申请退款',
    )
    miniapppay_refund_parser.add_argument(
        '--商户号',
        type=str,
        required=True,
        help='企业微信分配商户号。 示例值： 1900000109',
    )
    miniapppay_refund_parser.add_argument(
        '--商户APPID',
        type=str,
        required=True,
        help='小程序appid。 示例值：wx8888888888888888',
    )
    miniapppay_refund_parser.add_argument(
        '--商户订单号',
        type=str,
        required=True,
        help='原支付交易对应的商户订单号。 示例值：1217752501201407033233368018',
    )
    miniapppay_refund_parser.add_argument(
        '--商户退款单号',
        type=str,
        required=True,
        help='商户系统内部的退款单号，商户系统内部唯一，只能是数字、大小写字母_-|*@，同一退款单号多次请求只退一笔。 示例值：1217752501201407033233368018',
    )
    miniapppay_refund_parser.add_argument(
        '--退款原因',
        type=str,
        help='若商户传入，会在下发给用户的退款消息中体现退款原因。 注意：若订单退款金额≤1元，且属于部分退款，则不会在退款消息中体现退款原因 示例值：商品已售完',
    )
    miniapppay_refund_parser.add_argument(
        '--订单金额',
        type=str,
        required=True,
        help='订单金额信息，详见Amount。',
    )
    miniapppay_refund_parser.add_argument(
        '--资金账户',
        type=str,
        help='若订单处于待分账状态，填写该字段后，退款时直接从二级商户余额中退款。 AVAILABLE：可用余额',
    )

    def _handle_miniapppay_refund(a: argparse.Namespace) -> dict:
        return client.miniapppay_refund(
            商户号=a.商户号,
            商户APPID=a.商户APPID,
            商户订单号=a.商户订单号,
            商户退款单号=a.商户退款单号,
            退款原因=a.退款原因,
            订单金额=a.订单金额,
            资金账户=a.资金账户,
        )
    table[('miniapppay', 'refund')] = _handle_miniapppay_refund

    miniapppay_sub.add_parser(
        'upload-image',
        help='提交图片',
    )

    def _handle_miniapppay_upload_image(a: argparse.Namespace) -> dict:
        return client.miniapppay_upload_image()
    table[('miniapppay', 'upload-image')] = _handle_miniapppay_upload_image

    miniprogram_parser = subparsers.add_parser(
        'miniprogram',
        help='miniprogram',
    )
    miniprogram_sub = miniprogram_parser.add_subparsers(dest='__action', required=True)

    miniprogram_transfer_session_parser = miniprogram_sub.add_parser(
        'transfer-session',
        help='获取下级/下游企业小程序session',
    )
    miniprogram_transfer_session_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='通过code2Session接口获取到的加密的userid 不多于64字节',
    )
    miniprogram_transfer_session_parser.add_argument(
        '--session-key',
        type=str,
        required=True,
        help='通过code2Session接口获取到的属于上级/上游企业的会话密钥- 不多于64字节',
    )

    def _handle_miniprogram_transfer_session(a: argparse.Namespace) -> dict:
        return client.miniprogram_transfer_session(
            userid=a.userid,
            session_key=a.session_key,
        )
    table[('miniprogram', 'transfer-session')] = _handle_miniprogram_transfer_session

    msgaudit_parser = subparsers.add_parser(
        'msgaudit',
        help='msgaudit',
    )
    msgaudit_sub = msgaudit_parser.add_subparsers(dest='__action', required=True)

    msgaudit_check_single_agree_parser = msgaudit_sub.add_parser(
        'check-single-agree',
        help='获取会话同意情况',
    )
    msgaudit_check_single_agree_parser.add_argument(
        '--info',
        type=str,
        required=True,
        help='待查询的会话信息，数组',
    )
    msgaudit_check_single_agree_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='内部成员的userid',
    )
    msgaudit_check_single_agree_parser.add_argument(
        '--exteranalopenid',
        type=str,
        required=True,
        help='外部成员的exteranalopenid',
    )

    def _handle_msgaudit_check_single_agree(a: argparse.Namespace) -> dict:
        return client.msgaudit_check_single_agree(
            info=a.info,
            userid=a.userid,
            exteranalopenid=a.exteranalopenid,
        )
    table[('msgaudit', 'check-single-agree')] = _handle_msgaudit_check_single_agree

    msgaudit_get_permit_user_list_parser = msgaudit_sub.add_parser(
        'get-permit-user-list',
        help='获取会话内容存档开启成员列表',
    )
    msgaudit_get_permit_user_list_parser.add_argument(
        '--type',
        type=str,
        help='拉取对应版本的开启成员列表。1表示办公版；2表示服务版；3表示企业版。非必填，不填写的时候返回全量成员列表。',
    )

    def _handle_msgaudit_get_permit_user_list(a: argparse.Namespace) -> dict:
        return client.msgaudit_get_permit_user_list(
            type=a.type,
        )
    table[('msgaudit', 'get-permit-user-list')] = _handle_msgaudit_get_permit_user_list

    msgaudit_get_robot_info_parser = msgaudit_sub.add_parser(
        'get-robot-info',
        help='获取会话内容',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--msgid',
        type=str,
        help='消息id，消息的唯一标识，企业可以使用此字段进行消息去重。String类型',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--action',
        type=str,
        help='消息动作，目前有send(发送消息)/recall(撤回消息)/switch(切换企业日志)三种类型。String类型',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--from-',
        type=str,
        help='消息发送方id。同一企业内容为userid，非相同企业为external_userid。消息如果是机器人发出，也为external_userid。String类型',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--tolist',
        type=str,
        help='消息接收方列表，可能是多个，同一个企业内容为userid，非相同企业为external_userid。数组，内容为string类型',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--roomid',
        type=str,
        help='群聊消息的群id。如果是单聊则为空。String类型',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--msgtime',
        type=str,
        help='消息发送时间戳，utc时间，ms单位。',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--msgtype',
        type=str,
        help='文本消息为：text。String类型',
    )
    msgaudit_get_robot_info_parser.add_argument(
        '--content',
        type=str,
        help='消息内容。String类型',
    )

    def _handle_msgaudit_get_robot_info(a: argparse.Namespace) -> dict:
        return client.msgaudit_get_robot_info(
            msgid=a.msgid,
            action=a.action,
            from_=a.from_,
            tolist=a.tolist,
            roomid=a.roomid,
            msgtime=a.msgtime,
            msgtype=a.msgtype,
            content=a.content,
        )
    table[('msgaudit', 'get-robot-info')] = _handle_msgaudit_get_robot_info

    msgaudit_groupchat_get_parser = msgaudit_sub.add_parser(
        'groupchat-get',
        help='获取会话内容存档内部群信息',
    )
    msgaudit_groupchat_get_parser.add_argument(
        '--roomid',
        type=str,
        required=True,
        help='待查询的群id',
    )

    def _handle_msgaudit_groupchat_get(a: argparse.Namespace) -> dict:
        return client.msgaudit_groupchat_get(
            roomid=a.roomid,
        )
    table[('msgaudit', 'groupchat-get')] = _handle_msgaudit_groupchat_get

    network_parser = subparsers.add_parser(
        'network',
        help='network',
    )
    network_sub = network_parser.add_subparsers(dest='__action', required=True)

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

    oa_parser = subparsers.add_parser(
        'oa',
        help='oa',
    )
    oa_sub = oa_parser.add_subparsers(dest='__action', required=True)

    oa_applyevent_parser = oa_sub.add_parser(
        'applyevent',
        help='提交审批申请',
    )
    oa_applyevent_parser.add_argument(
        '--creator-userid',
        type=str,
        required=True,
        help='申请人userid，此审批申请将以此员工身份提交，申请人需在应用可见范围内',
    )
    oa_applyevent_parser.add_argument(
        '--template-id',
        type=str,
        required=True,
        help='模板id。可在“获取审批申请详情”、“审批状态变化回调通知”中获得，也可在审批模板的模板编辑页面链接中获得。暂不支持通过接口提交[打卡补卡][调班]模板审批单。',
    )
    oa_applyevent_parser.add_argument(
        '--use-template-approver',
        type=str,
        required=True,
        help='审批人模式：0-通过接口指定审批人、抄送人（此时process参数必填）; 1-使用此模板在管理后台设置的审批流程(需要保证审批流程中没有“申请人自选”节点)，支持条件审批。默认为0',
    )
    oa_applyevent_parser.add_argument(
        '--choose-department',
        type=str,
        help='提单者提单部门id，不填默认为主部门',
    )
    oa_applyevent_parser.add_argument(
        '--apply-data',
        type=str,
        required=True,
        help='审批申请数据，可定义审批申请中各个控件的值，其中必填项必须有值，选填项可为空，数据结构同“获取审批申请详情”接口返回值中同名参数“apply_data”',
    )
    oa_applyevent_parser.add_argument(
        '--contents',
        type=str,
        required=True,
        help='审批申请详情，由多个表单控件及其内容组成，其中包含需要对控件赋值的信息',
    )
    oa_applyevent_parser.add_argument(
        '--control',
        type=str,
        required=True,
        help='控件类型：Text-文本；Textarea-多行文本；Number-数字；Money-金额；Date-日期/日期+时间；Selector-单选/多选；；Contact-成员/部门；Tips-说明文字；File-附件；Table-明细；Location-位置；RelatedApproval-关联审批单；Formula-公式；DateRange-时长；',
    )
    oa_applyevent_parser.add_argument(
        '--id',
        type=str,
        required=True,
        help='控件id：控件的唯一id，可通过“获取审批模板详情”接口获取',
    )
    oa_applyevent_parser.add_argument(
        '--value',
        type=str,
        required=True,
        help='控件值 ，需在此为申请人在各个控件中填写内容不同控件有不同的赋值参数，具体说明详见附录。模板配置的控件属性为必填时，对应value值需要有值。',
    )
    oa_applyevent_parser.add_argument(
        '--summary-list',
        type=str,
        required=True,
        help='摘要信息，用于显示在审批通知卡片、审批列表的摘要信息，最多3行',
    )
    oa_applyevent_parser.add_argument(
        '--summary-info',
        type=str,
        required=True,
        help='摘要行信息，用于定义某一行摘要显示的内容',
    )
    oa_applyevent_parser.add_argument(
        '--text',
        type=str,
        required=True,
        help='摘要行显示文字，用于记录列表和消息通知的显示，不要超过20个字符',
    )
    oa_applyevent_parser.add_argument(
        '--lang',
        type=str,
        required=True,
        help='摘要行显示语言，中文：zh_CN（注意不是zh-CN），英文：en。',
    )
    oa_applyevent_parser.add_argument(
        '--process',
        type=str,
        help='新版流程列表',
    )
    oa_applyevent_parser.add_argument(
        '--node-list',
        type=str,
        required=True,
        help='流程节点',
    )
    oa_applyevent_parser.add_argument(
        '--type',
        type=str,
        required=True,
        help='节点类型 1:审批人 2:抄送人 3:办理人',
    )
    oa_applyevent_parser.add_argument(
        '--apv-rel',
        type=str,
        help='多人审批方式 1-会签；2-或签 3-依次审批',
    )
    oa_applyevent_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='用户id',
    )

    def _handle_oa_applyevent(a: argparse.Namespace) -> dict:
        return client.oa_applyevent(
            creator_userid=a.creator_userid,
            template_id=a.template_id,
            use_template_approver=a.use_template_approver,
            choose_department=a.choose_department,
            apply_data=a.apply_data,
            contents=a.contents,
            control=a.control,
            id=a.id,
            value=a.value,
            summary_list=a.summary_list,
            summary_info=a.summary_info,
            text=a.text,
            lang=a.lang,
            process=a.process,
            node_list=a.node_list,
            type=a.type,
            apv_rel=a.apv_rel,
            userid=a.userid,
        )
    table[('oa', 'applyevent')] = _handle_oa_applyevent

    oa_approval_create_template_parser = oa_sub.add_parser(
        'approval-create-template',
        help='创建审批模板',
    )
    oa_approval_create_template_parser.add_argument(
        '--template-name',
        type=str,
        required=True,
        help='模版名称数组',
    )
    oa_approval_create_template_parser.add_argument(
        '--text',
        type=str,
        required=True,
        help='模版名称。需满足以下条件：1-模版名称不得和现有模版名称重复；2-长度不得超过40个字符。',
    )
    oa_approval_create_template_parser.add_argument(
        '--lang',
        type=str,
        required=True,
        help='显示语言，中文：zh_CN（注意不是zh-CN）',
    )
    oa_approval_create_template_parser.add_argument(
        '--template-content',
        type=str,
        required=True,
        help='审批模版控件设置，由多个表单控件及其内容组成，其中包含需要对控件赋值的信息',
    )
    oa_approval_create_template_parser.add_argument(
        '--controls',
        type=str,
        required=True,
        help='控件数组，模版中可以设置多个控件类型，排列顺序和管理端展示的相同',
    )
    oa_approval_create_template_parser.add_argument(
        '--property',
        type=str,
        required=True,
        help='控件的基础属性',
    )
    oa_approval_create_template_parser.add_argument(
        '--control',
        type=str,
        required=True,
        help='控件类型：Text-文本；Textarea-多行文本；Number-数字；Money-金额；Date-日期/日期+时间；Selector-单选/多选；；Contact-成员/部门；Tips-说明文字；File-附件；Table-明细；Location-位置；RelatedApproval-关联审批单；DateRange-时长；PhoneNumber-电话号码；Vacation-假期；Attendance-外出/出差/加班；BankAccount-收款账户 。以上为目前可支持的控件类型',
    )
    oa_approval_create_template_parser.add_argument(
        '--id',
        type=str,
        required=True,
        help='控件id。1-模版内控件id必须唯一；2-控件id格式：control-数字，如"Text-01"',
    )
    oa_approval_create_template_parser.add_argument(
        '--title',
        type=str,
        required=True,
        help='控件名称',
    )
    oa_approval_create_template_parser.add_argument(
        '--text-1',
        type=str,
        required=True,
        help='控件名称。需满足以下条件：1-控件名称不得和现有控件名称重复；2-长度不得超过40个字符。3-Attendance-外出/出差/加班控件title固定为外出/出差/加班，暂不支持自定义',
    )
    oa_approval_create_template_parser.add_argument(
        '--lang-1',
        type=str,
        required=True,
        help='显示语言，中文：zh_CN（注意不是zh-CN）',
    )
    oa_approval_create_template_parser.add_argument(
        '--placeholder',
        type=str,
        help='控件说明，假勤组件（Vacation、Attendance）暂不支持设置',
    )
    oa_approval_create_template_parser.add_argument(
        '--text-2',
        type=str,
        help='控件说明。需满足以下条件：长度不得超过80个字符。',
    )
    oa_approval_create_template_parser.add_argument(
        '--lang-2',
        type=str,
        help='显示语言，中文：zh_CN（注意不是zh-CN）；若text填写，则该项为必填',
    )
    oa_approval_create_template_parser.add_argument(
        '--require',
        help='控件是否必填。0-非必填；1-必填；默认为0;假勤组件（Vacation、Attendance）不支持设置非必填',
    )
    oa_approval_create_template_parser.add_argument(
        '--un-print',
        help='控件是否可打印。0-可打印；1-不可打印；默认为0；假勤组件（Vacation、Attendance）不支持设置不可打印',
    )
    oa_approval_create_template_parser.add_argument(
        '--config',
        type=str,
        help='控件配置。控件的类型不同，其中填的参数不相同，下方将为每一个控件配置进行详细说明',
    )

    def _handle_oa_approval_create_template(a: argparse.Namespace) -> dict:
        return client.oa_approval_create_template(
            template_name=a.template_name,
            text=a.text,
            lang=a.lang,
            template_content=a.template_content,
            controls=a.controls,
            property=a.property,
            control=a.control,
            id=a.id,
            title=a.title,
            text_1=a.text_1,
            lang_1=a.lang_1,
            placeholder=a.placeholder,
            text_2=a.text_2,
            lang_2=a.lang_2,
            require=a.require,
            un_print=a.un_print,
            config=a.config,
        )
    table[('oa', 'approval-create-template')] = _handle_oa_approval_create_template

    oa_approval_update_template_parser = oa_sub.add_parser(
        'approval-update-template',
        help='更新审批模板',
    )
    oa_approval_update_template_parser.add_argument(
        '--template-id',
        type=str,
        required=True,
        help='模版id',
    )
    oa_approval_update_template_parser.add_argument(
        '--template-name',
        type=str,
        required=True,
        help='模版名称数组',
    )
    oa_approval_update_template_parser.add_argument(
        '--text',
        type=str,
        required=True,
        help='模版名称。需满足以下条件：1-模版名称不得和现有模版名称重复；2-长度不得超过40个字符。',
    )
    oa_approval_update_template_parser.add_argument(
        '--lang',
        type=str,
        required=True,
        help='显示语言，中文：zh_CN（注意不是zh-CN）',
    )
    oa_approval_update_template_parser.add_argument(
        '--template-content',
        type=str,
        required=True,
        help='审批模版控件设置，可以参考创建审批模板一节 template_content 参数说明',
    )

    def _handle_oa_approval_update_template(a: argparse.Namespace) -> dict:
        return client.oa_approval_update_template(
            template_id=a.template_id,
            template_name=a.template_name,
            text=a.text,
            lang=a.lang,
            template_content=a.template_content,
        )
    table[('oa', 'approval-update-template')] = _handle_oa_approval_update_template

    oa_calendar_del_parser = oa_sub.add_parser(
        'calendar-del',
        help='删除日历',
    )
    oa_calendar_del_parser.add_argument(
        '--cal-id',
        type=str,
        required=True,
        help='日历ID',
    )

    def _handle_oa_calendar_del(a: argparse.Namespace) -> dict:
        return client.oa_calendar_del(
            cal_id=a.cal_id,
        )
    table[('oa', 'calendar-del')] = _handle_oa_calendar_del

    oa_calendar_get_parser = oa_sub.add_parser(
        'calendar-get',
        help='获取日历详情',
    )
    oa_calendar_get_parser.add_argument(
        '--cal-id-list',
        type=str,
        required=True,
        help='日历ID列表，调用创建日历接口后获得。一次最多可获取1000条',
    )

    def _handle_oa_calendar_get(a: argparse.Namespace) -> dict:
        return client.oa_calendar_get(
            cal_id_list=a.cal_id_list,
        )
    table[('oa', 'calendar-get')] = _handle_oa_calendar_get

    oa_calendar_update_parser = oa_sub.add_parser(
        'calendar-update',
        help='更新日历',
    )
    oa_calendar_update_parser.add_argument(
        '--skip-public-range',
        help='是否不更新可订阅范围。0-否；1-是。默认会为0，会更新可订阅范围',
    )
    oa_calendar_update_parser.add_argument(
        '--calendar',
        type=str,
        required=True,
        help='日历信息',
    )
    oa_calendar_update_parser.add_argument(
        '--cal-id',
        type=str,
        required=True,
        help='日历ID',
    )
    oa_calendar_update_parser.add_argument(
        '--admins',
        type=str,
        help='日历的管理员userid列表。最多指定3人',
    )
    oa_calendar_update_parser.add_argument(
        '--summary',
        type=str,
        required=True,
        help='日历标题。1 ~ 128 字符',
    )
    oa_calendar_update_parser.add_argument(
        '--color',
        type=str,
        required=True,
        help='日历颜色，RGB颜色编码16进制表示，例如："#0000FF" 表示纯蓝色',
    )
    oa_calendar_update_parser.add_argument(
        '--description',
        type=str,
        help='日历描述。0 ~ 512 字符',
    )
    oa_calendar_update_parser.add_argument(
        '--public-range',
        type=str,
        help='公开范围。仅当是公共日历时有效',
    )
    oa_calendar_update_parser.add_argument(
        '--public-range-userids',
        type=str,
        help='公开的成员列表范围 。最多指定1000个成员',
    )
    oa_calendar_update_parser.add_argument(
        '--public-range-partyids',
        type=str,
        help='公开的部门列表范围 。最多指定100个部门',
    )
    oa_calendar_update_parser.add_argument(
        '--shares',
        type=str,
        help='日历通知范围成员列表。最多2000人',
    )
    oa_calendar_update_parser.add_argument(
        '--shares-userid',
        type=str,
        required=True,
        help='日历通知范围成员的id',
    )
    oa_calendar_update_parser.add_argument(
        '--shares-permission',
        type=str,
        help='日历通知范围成员权限（不填则默认为「可查看」）。 1：可查看 3：仅查看闲忙状态',
    )

    def _handle_oa_calendar_update(a: argparse.Namespace) -> dict:
        return client.oa_calendar_update(
            skip_public_range=a.skip_public_range,
            calendar=a.calendar,
            cal_id=a.cal_id,
            admins=a.admins,
            summary=a.summary,
            color=a.color,
            description=a.description,
            public_range=a.public_range,
            public_range_userids=a.public_range_userids,
            public_range_partyids=a.public_range_partyids,
            shares=a.shares,
            shares_userid=a.shares_userid,
            shares_permission=a.shares_permission,
        )
    table[('oa', 'calendar-update')] = _handle_oa_calendar_update

    oa_getapprovaldetail_parser = oa_sub.add_parser(
        'getapprovaldetail',
        help='获取审批申请详情',
    )
    oa_getapprovaldetail_parser.add_argument(
        '--sp-no',
        type=str,
        required=True,
        help='审批单编号。',
    )

    def _handle_oa_getapprovaldetail(a: argparse.Namespace) -> dict:
        return client.oa_getapprovaldetail(
            sp_no=a.sp_no,
        )
    table[('oa', 'getapprovaldetail')] = _handle_oa_getapprovaldetail

    oa_getapprovalinfo_parser = oa_sub.add_parser(
        'getapprovalinfo',
        help='批量获取审批单号',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--starttime',
        type=str,
        required=True,
        help='审批单提交的时间范围，开始时间，UNix时间戳',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--endtime',
        type=str,
        required=True,
        help='审批单提交的时间范围，结束时间，Unix时间戳',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--new-cursor',
        type=str,
        required=True,
        help='分页查询游标，默认为空串，后续使用返回的new_next_cursor进行分页拉取',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--size',
        type=int,
        required=True,
        help='一次请求拉取审批单数量，默认值为100，上限值为100。若accesstoken为自建应用，仅允许获取在应用可见范围内申请人提交的表单，返回的sp_no_list个数可能和size不一致，开发者需用next_cursor判断表单记录是否拉取完',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--filters',
        type=str,
        help='筛选条件，可对批量拉取的审批申请设置约束条件，支持设置多个条件',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--key',
        type=str,
        help='筛选类型，包括： template_id - 模板类型/模板id； creator - 申请人； department - 审批单提单者所在部门； sp_status - 审批状态; record_type - 审批单类型属性，1-请假；2-打卡补卡；3-出差；4-外出；5-加班； 6- 调班；7-会议室预定；8-退款审批；9-红包报销审批 注意: 1、仅“部门”支持同时配置多个筛选条件。 2、不同类型的筛选条件之间为“与”的关系，同类型筛选条件之间为“或”的关系 3、record_type筛选类型仅支持2021/05/31以后新提交的审批单，历史单不支持表单类型属性过滤',
    )
    oa_getapprovalinfo_parser.add_argument(
        '--value',
        type=str,
        help='筛选值，对应为：template_id-模板id；creator-申请人userid ；department-所在部门id；sp_status-审批单状态（1-审批中；2-已通过；3-已驳回；4-已撤销；6-通过后撤销；7-已删除；10-已支付）',
    )

    def _handle_oa_getapprovalinfo(a: argparse.Namespace) -> dict:
        return client.oa_getapprovalinfo(
            starttime=a.starttime,
            endtime=a.endtime,
            new_cursor=a.new_cursor,
            size=a.size,
            filters=a.filters,
            key=a.key,
            value=a.value,
        )
    table[('oa', 'getapprovalinfo')] = _handle_oa_getapprovalinfo

    oa_gettemplatedetail_parser = oa_sub.add_parser(
        'gettemplatedetail',
        help='获取审批模板详情',
    )
    oa_gettemplatedetail_parser.add_argument(
        '--template-id',
        type=str,
        required=True,
        help='模板的唯一标识id。可在“获取审批单据详情”、“审批状态变化回调通知”中获得，也可在审批模板的模板编辑页面浏览器Url链接中获得。',
    )

    def _handle_oa_gettemplatedetail(a: argparse.Namespace) -> dict:
        return client.oa_gettemplatedetail(
            template_id=a.template_id,
        )
    table[('oa', 'gettemplatedetail')] = _handle_oa_gettemplatedetail

    oa_journal_download_wedrive_file_parser = oa_sub.add_parser(
        'journal-download-wedrive-file',
        help='下载微盘文件',
    )
    oa_journal_download_wedrive_file_parser.add_argument(
        '--journaluuid',
        type=str,
        required=True,
        help='汇报记录id',
    )
    oa_journal_download_wedrive_file_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='微盘fileid。获取汇报记录详情返回的微盘附件fileid。必须是journaluuid对应的汇报关联的wedrive_files。',
    )

    def _handle_oa_journal_download_wedrive_file(a: argparse.Namespace) -> dict:
        return client.oa_journal_download_wedrive_file(
            journaluuid=a.journaluuid,
            fileid=a.fileid,
        )
    table[('oa', 'journal-download-wedrive-file')] = _handle_oa_journal_download_wedrive_file

    oa_journal_get_record_detail_parser = oa_sub.add_parser(
        'journal-get-record-detail',
        help='获取汇报记录详情',
    )
    oa_journal_get_record_detail_parser.add_argument(
        '--journaluuid',
        type=str,
        required=True,
        help='- 不多于256字节',
    )

    def _handle_oa_journal_get_record_detail(a: argparse.Namespace) -> dict:
        return client.oa_journal_get_record_detail(
            journaluuid=a.journaluuid,
        )
    table[('oa', 'journal-get-record-detail')] = _handle_oa_journal_get_record_detail

    oa_meetingroom_add_parser = oa_sub.add_parser(
        'meetingroom-add',
        help='会议室管理',
    )
    oa_meetingroom_add_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='会议室名称，最多30个字符',
    )
    oa_meetingroom_add_parser.add_argument(
        '--capacity',
        type=str,
        required=True,
        help='会议室所能容纳的人数',
    )
    oa_meetingroom_add_parser.add_argument(
        '--city',
        type=str,
        help='会议室所在城市',
    )
    oa_meetingroom_add_parser.add_argument(
        '--building',
        type=str,
        help='会议室所在楼宇',
    )
    oa_meetingroom_add_parser.add_argument(
        '--floor',
        type=str,
        help='会议室所在楼层',
    )
    oa_meetingroom_add_parser.add_argument(
        '--equipment',
        type=str,
        help='会议室支持的设备列表,参数详细含义见附录',
    )
    oa_meetingroom_add_parser.add_argument(
        '--coordinate-latitude',
        type=str,
        help='会议室所在建筑纬度,可通过腾讯地图坐标拾取器获取',
    )
    oa_meetingroom_add_parser.add_argument(
        '--coordinate-longitude',
        type=str,
        help='会议室所在建筑经度,可通过腾讯地图坐标拾取器获取',
    )
    oa_meetingroom_add_parser.add_argument(
        '--range-user-list',
        type=str,
        help='会议室使用范围的userid列表，最多指定1000个成员',
    )
    oa_meetingroom_add_parser.add_argument(
        '--range-department-list',
        type=str,
        help='会议室使用范围的部门id列表，最多指定1000个部门',
    )

    def _handle_oa_meetingroom_add(a: argparse.Namespace) -> dict:
        return client.oa_meetingroom_add(
            name=a.name,
            capacity=a.capacity,
            city=a.city,
            building=a.building,
            floor=a.floor,
            equipment=a.equipment,
            coordinate_latitude=a.coordinate_latitude,
            coordinate_longitude=a.coordinate_longitude,
            range_user_list=a.range_user_list,
            range_department_list=a.range_department_list,
        )
    table[('oa', 'meetingroom-add')] = _handle_oa_meetingroom_add

    oa_meetingroom_get_booking_info_parser = oa_sub.add_parser(
        'meetingroom-get-booking-info',
        help='会议室预定管理',
    )
    oa_meetingroom_get_booking_info_parser.add_argument(
        '--meetingroom-id',
        type=str,
        help='会议室id',
    )
    oa_meetingroom_get_booking_info_parser.add_argument(
        '--start-time',
        type=str,
        help='查询预定的起始时间，默认为当前时间',
    )
    oa_meetingroom_get_booking_info_parser.add_argument(
        '--end-time',
        type=str,
        help='查询预定的结束时间， 默认为明日0时',
    )
    oa_meetingroom_get_booking_info_parser.add_argument(
        '--city',
        type=str,
        help='会议室所在城市',
    )
    oa_meetingroom_get_booking_info_parser.add_argument(
        '--building',
        type=str,
        help='会议室所在楼宇',
    )
    oa_meetingroom_get_booking_info_parser.add_argument(
        '--floor',
        type=str,
        help='会议室所在楼层',
    )

    def _handle_oa_meetingroom_get_booking_info(a: argparse.Namespace) -> dict:
        return client.oa_meetingroom_get_booking_info(
            meetingroom_id=a.meetingroom_id,
            start_time=a.start_time,
            end_time=a.end_time,
            city=a.city,
            building=a.building,
            floor=a.floor,
        )
    table[('oa', 'meetingroom-get-booking-info')] = _handle_oa_meetingroom_get_booking_info

    oa_schedule_add_attendees_parser = oa_sub.add_parser(
        'schedule-add-attendees',
        help='新增日程参与者',
    )
    oa_schedule_add_attendees_parser.add_argument(
        '--schedule-id',
        type=str,
        required=True,
        help='日程ID。创建日程时返回的ID',
    )
    oa_schedule_add_attendees_parser.add_argument(
        '--attendees',
        type=str,
        help='日程参与者列表。累计最多支持1000人',
    )
    oa_schedule_add_attendees_parser.add_argument(
        '--attendees-userid',
        type=str,
        required=True,
        help='日程参与者ID 不多于64字节',
    )

    def _handle_oa_schedule_add_attendees(a: argparse.Namespace) -> dict:
        return client.oa_schedule_add_attendees(
            schedule_id=a.schedule_id,
            attendees=a.attendees,
            attendees_userid=a.attendees_userid,
        )
    table[('oa', 'schedule-add-attendees')] = _handle_oa_schedule_add_attendees

    oa_schedule_del_parser = oa_sub.add_parser(
        'schedule-del',
        help='取消日程',
    )
    oa_schedule_del_parser.add_argument(
        '--schedule-id',
        type=str,
        required=True,
        help='日程ID',
    )
    oa_schedule_del_parser.add_argument(
        '--op-mode',
        type=str,
        help='操作模式。是重复日程时有效。 0-默认删除所有日程； 1-仅删除此日程； 2-删除本次及后续日程 详见重复日程的不同操作模式',
    )
    oa_schedule_del_parser.add_argument(
        '--op-start-time',
        type=str,
        help='操作起始时间。仅当操作模式是1或2时有效。该时间必须是重复日程的某一次开始时间',
    )

    def _handle_oa_schedule_del(a: argparse.Namespace) -> dict:
        return client.oa_schedule_del(
            schedule_id=a.schedule_id,
            op_mode=a.op_mode,
            op_start_time=a.op_start_time,
        )
    table[('oa', 'schedule-del')] = _handle_oa_schedule_del

    oa_schedule_del_attendees_parser = oa_sub.add_parser(
        'schedule-del-attendees',
        help='删除日程参与者',
    )
    oa_schedule_del_attendees_parser.add_argument(
        '--schedule-id',
        type=str,
        required=True,
        help='日程ID。创建日程时返回的ID',
    )
    oa_schedule_del_attendees_parser.add_argument(
        '--attendees',
        type=str,
        help='日程参与者列表，最多可添加1000人。',
    )
    oa_schedule_del_attendees_parser.add_argument(
        '--attendees-userid',
        type=str,
        required=True,
        help='日程参与者ID 不多于64字节',
    )

    def _handle_oa_schedule_del_attendees(a: argparse.Namespace) -> dict:
        return client.oa_schedule_del_attendees(
            schedule_id=a.schedule_id,
            attendees=a.attendees,
            attendees_userid=a.attendees_userid,
        )
    table[('oa', 'schedule-del-attendees')] = _handle_oa_schedule_del_attendees

    oa_schedule_get_parser = oa_sub.add_parser(
        'schedule-get',
        help='获取日程详情',
    )
    oa_schedule_get_parser.add_argument(
        '--schedule-id-list',
        type=str,
        required=True,
        help='日程ID列表。一次最多拉取1000条',
    )

    def _handle_oa_schedule_get(a: argparse.Namespace) -> dict:
        return client.oa_schedule_get(
            schedule_id_list=a.schedule_id_list,
        )
    table[('oa', 'schedule-get')] = _handle_oa_schedule_get

    oa_schedule_get_by_calendar_parser = oa_sub.add_parser(
        'schedule-get-by-calendar',
        help='获取日历下的日程列表',
    )
    oa_schedule_get_by_calendar_parser.add_argument(
        '--cal-id',
        type=str,
        required=True,
        help='日历ID',
    )
    oa_schedule_get_by_calendar_parser.add_argument(
        '--offset',
        type=str,
        help='分页，偏移量, 默认为0',
    )
    oa_schedule_get_by_calendar_parser.add_argument(
        '--limit',
        type=str,
        help='分页，预期请求的数据量，默认为500，取值范围 1 ~ 1000',
    )

    def _handle_oa_schedule_get_by_calendar(a: argparse.Namespace) -> dict:
        return client.oa_schedule_get_by_calendar(
            cal_id=a.cal_id,
            offset=a.offset,
            limit=a.limit,
        )
    table[('oa', 'schedule-get-by-calendar')] = _handle_oa_schedule_get_by_calendar

    oa_schedule_update_parser = oa_sub.add_parser(
        'schedule-update',
        help='更新日程',
    )
    oa_schedule_update_parser.add_argument(
        '--skip-attendees',
        help='是否不更新参与人。0-否；1-是。默认为0',
    )
    oa_schedule_update_parser.add_argument(
        '--op-mode',
        type=str,
        help='操作模式。是重复日程时有效。 0-默认全部修改； 1-仅修改此日程； 2-修改将来的所有日程 详见重复日程的不同操作模式',
    )
    oa_schedule_update_parser.add_argument(
        '--op-start-time',
        type=str,
        help='操作起始时间。仅当操作模式是1或2时有效。该时间必须是重复日程的某一次开始时间 例如：假如日程开始时间start_time为1661990950（2022-09-01 08:09:10），且重复类型是每周，那么op_start_time可以是：1661990950（2022-09-01 08:09:10）、1662595750（2022-09-08 08:09:10）、1663200550（2022-09-15 08:09:10）......',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule',
        type=str,
        required=True,
        help='日程信息',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-schedule-id',
        type=str,
        required=True,
        help='日程ID。创建日程时返回的ID',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-admins',
        type=str,
        help='日程的管理员userid列表，管理员必须在共享成员的列表中。最多指定3人',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-attendees',
        type=str,
        help='日程参与者列表。最多支持1000人',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-attendees-userid',
        type=str,
        required=True,
        help='日程参与者ID 不多于64字节',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-summary',
        type=str,
        help='日程标题。0 ~ 128 字符。不填会默认显示为“新建事件”',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-description',
        type=str,
        help='日程描述 不多于1000个字符',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders',
        type=str,
        help='提醒相关信息',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-is-remind',
        help='是否需要提醒。0-否；1-是',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-is-repeat',
        help='是否重复日程。0-否；1-是',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-remind-before-event-secs',
        type=str,
        help='日程开始（start_time）前多少秒提醒，当is_remind为1时有效。 例如： 300表示日程开始前5分钟提醒。目前仅支持以下数值： 0 - 事件开始时 300 - 事件开始前5分钟 900 - 事件开始前15分钟 3600 - 事件开始前1小时 86400 - 事件开始前1天',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-remind-time-diffs',
        type=str,
        help='提醒时间与日程开始时间（start_time）的差值，当is_remind为1时有效，可以指定多个提醒时间，目前仅支持以下数值： 0 - 事件开始时 -300 - 事件开始前5分钟 -900 - 事件开始前15分钟 -3600 - 事件开始前1小时 -86400 - 事件开始前1天 当is_whole_day=1时，还支持： 32400 - 事件开始当天（09：00） -172800 - 事件开始前两天 -604800 - 事件开始前1周 该字段与remind_before_event_secs仅一个字段会生效，当该字段有传值且列表不为空时，优先以该字段为准',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-repeat-type',
        type=str,
        help='重复类型，当is_repeat为1时有效。目前支持如下类型： 0 - 每日 1 - 每周 2 - 每月 5 - 每年 7 - 工作日',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-repeat-until',
        type=str,
        help='重复结束时刻，Unix时间戳，当is_repeat为1时有效。不填或填0表示一直重复',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-is-custom-repeat',
        help='是否自定义重复。0-否；1-是。当is_repeat为1时有效。',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-repeat-interval',
        type=str,
        help='重复间隔 仅当指定为自定义重复时有效 该字段随repeat_type不同而含义不同 例如： repeat_interval指定为2，repeat_type指定为每周重复，那么每2周重复一次； repeat_interval指定为2，repeat_type指定为每月重复，那么每2月重复一次',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-repeat-day-of-week',
        type=str,
        help='每周周几重复 仅当指定为自定义重复且重复类型为每周时有效 取值范围：1 ~ 7，分别表示周一至周日',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-repeat-day-of-month',
        type=str,
        help='每月哪几天重复 仅当指定为自定义重复且重复类型为每月时有效 取值范围：1 ~ 31，分别表示1~31号',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-reminders-timezone',
        type=str,
        help='时区。UTC偏移量表示(即偏离零时区的小时数)，东区为正数，西区为负数。 例如：+8 表示北京时间东八区 默认为北京时间东八区 取值范围：-12 ~ +12',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-location',
        type=str,
        help='日程地址 不多于128个字符',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-start-time',
        type=str,
        required=True,
        help='日程开始时间，Unix时间戳 注意，如果op_mode是1或2，start_time和end_time，必须是op_start_time当天或之后的时间',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-end-time',
        type=str,
        required=True,
        help='日程结束时间，Unix时间戳',
    )
    oa_schedule_update_parser.add_argument(
        '--schedule-is-whole-day',
        help='是否更新成全天日程，0-否；1-是',
    )

    def _handle_oa_schedule_update(a: argparse.Namespace) -> dict:
        return client.oa_schedule_update(
            skip_attendees=a.skip_attendees,
            op_mode=a.op_mode,
            op_start_time=a.op_start_time,
            schedule=a.schedule,
            schedule_schedule_id=a.schedule_schedule_id,
            schedule_admins=a.schedule_admins,
            schedule_attendees=a.schedule_attendees,
            schedule_attendees_userid=a.schedule_attendees_userid,
            schedule_summary=a.schedule_summary,
            schedule_description=a.schedule_description,
            schedule_reminders=a.schedule_reminders,
            schedule_reminders_is_remind=a.schedule_reminders_is_remind,
            schedule_reminders_is_repeat=a.schedule_reminders_is_repeat,
            schedule_reminders_remind_before_event_secs=a.schedule_reminders_remind_before_event_secs,
            schedule_reminders_remind_time_diffs=a.schedule_reminders_remind_time_diffs,
            schedule_reminders_repeat_type=a.schedule_reminders_repeat_type,
            schedule_reminders_repeat_until=a.schedule_reminders_repeat_until,
            schedule_reminders_is_custom_repeat=a.schedule_reminders_is_custom_repeat,
            schedule_reminders_repeat_interval=a.schedule_reminders_repeat_interval,
            schedule_reminders_repeat_day_of_week=a.schedule_reminders_repeat_day_of_week,
            schedule_reminders_repeat_day_of_month=a.schedule_reminders_repeat_day_of_month,
            schedule_reminders_timezone=a.schedule_reminders_timezone,
            schedule_location=a.schedule_location,
            schedule_start_time=a.schedule_start_time,
            schedule_end_time=a.schedule_end_time,
            schedule_is_whole_day=a.schedule_is_whole_day,
        )
    table[('oa', 'schedule-update')] = _handle_oa_schedule_update

    oa_vacation_getuservacationquota_parser = oa_sub.add_parser(
        'vacation-getuservacationquota',
        help='获取成员假期余额',
    )
    oa_vacation_getuservacationquota_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='需要获取假期余额的成员的userid',
    )

    def _handle_oa_vacation_getuservacationquota(a: argparse.Namespace) -> dict:
        return client.oa_vacation_getuservacationquota(
            userid=a.userid,
        )
    table[('oa', 'vacation-getuservacationquota')] = _handle_oa_vacation_getuservacationquota

    pstncc_parser = subparsers.add_parser(
        'pstncc',
        help='pstncc',
    )
    pstncc_sub = pstncc_parser.add_subparsers(dest='__action', required=True)

    pstncc_call_parser = pstncc_sub.add_parser(
        'call',
        help='发起语音电话',
    )
    pstncc_call_parser.add_argument(
        '--callee-userid',
        type=str,
        required=True,
        help='需要呼叫的列表',
    )

    def _handle_pstncc_call(a: argparse.Namespace) -> dict:
        return client.pstncc_call(
            callee_userid=a.callee_userid,
        )
    table[('pstncc', 'call')] = _handle_pstncc_call

    pstncc_getstates_parser = pstncc_sub.add_parser(
        'getstates',
        help='获取接听状态',
    )
    pstncc_getstates_parser.add_argument(
        '--callee-userid',
        type=str,
        required=True,
        help='用户id',
    )
    pstncc_getstates_parser.add_argument(
        '--callid',
        type=str,
        required=True,
        help='发起自动语音来电callid',
    )

    def _handle_pstncc_getstates(a: argparse.Namespace) -> dict:
        return client.pstncc_getstates(
            callee_userid=a.callee_userid,
            callid=a.callid,
        )
    table[('pstncc', 'getstates')] = _handle_pstncc_getstates

    school_parser = subparsers.add_parser(
        'school',
        help='school',
    )
    school_sub = school_parser.add_subparsers(dest='__action', required=True)

    school_agent_get_allow_scope_parser = school_sub.add_parser(
        'agent-get-allow-scope',
        help='获取可使用的家长范围',
    )
    school_agent_get_allow_scope_parser.add_argument(
        '--agentid',
        type=str,
        required=True,
        help='应用id',
    )

    def _handle_school_agent_get_allow_scope(a: argparse.Namespace) -> dict:
        return client.school_agent_get_allow_scope(
            agentid=a.agentid,
        )
    table[('school', 'agent-get-allow-scope')] = _handle_school_agent_get_allow_scope

    school_department_create_parser = school_sub.add_parser(
        'department-create',
        help='创建部门',
    )
    school_department_create_parser.add_argument(
        '--name',
        type=str,
        help='部门名称。长度限制为1~32个字符，字符不能包括-:*?"<>/，*，当设置了入学年份和标准年级时，该参数将被忽略',
    )
    school_department_create_parser.add_argument(
        '--parentid',
        type=str,
        required=True,
        help='父部门id，32位整型',
    )
    school_department_create_parser.add_argument(
        '--id',
        type=str,
        help='部门id，32位整型，指定时必须大于1。若不填该参数，将自动生成id',
    )
    school_department_create_parser.add_argument(
        '--type',
        type=str,
        required=True,
        help='部门类型，32位整型，1表示班级，2表示年级，3表示学段，4表示校区',
    )
    school_department_create_parser.add_argument(
        '--standard-grade',
        type=str,
        help='标准年级，32位整型，参数值含义详见标准年级对照表，仅当部门类型为年级（2）时生效',
    )
    school_department_create_parser.add_argument(
        '--register-year',
        type=str,
        help='入学年份，32位整型，格式为YYYY，输入范围为1970～2100，仅当部门类型为年级（2）时生效，如果在创建标准年级时不填此参数，则由系统自动计算出入学年份',
    )
    school_department_create_parser.add_argument(
        '--order',
        type=str,
        help='在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)',
    )
    school_department_create_parser.add_argument(
        '--department-admins',
        type=str,
        help='部门管理员列表',
    )
    school_department_create_parser.add_argument(
        '--department-admins-userid',
        type=str,
        required=True,
        help='对应管理端的账号，企业内必须唯一。不区分大小写，长度为1~64个字节',
    )
    school_department_create_parser.add_argument(
        '--department-admins-type',
        type=str,
        required=True,
        help='部门管理员类型， 1表示校区负责人，2表示年级负责人，3表示班主任，4表示任课老师，5表示学段负责人',
    )
    school_department_create_parser.add_argument(
        '--department-admins-subject',
        type=str,
        help='教师的科目，仅班主任和任课老师可以设置，科目的最多15个字符，仅支持设置一个科目',
    )

    def _handle_school_department_create(a: argparse.Namespace) -> dict:
        return client.school_department_create(
            name=a.name,
            parentid=a.parentid,
            id=a.id,
            type=a.type,
            standard_grade=a.standard_grade,
            register_year=a.register_year,
            order=a.order,
            department_admins=a.department_admins,
            department_admins_userid=a.department_admins_userid,
            department_admins_type=a.department_admins_type,
            department_admins_subject=a.department_admins_subject,
        )
    table[('school', 'department-create')] = _handle_school_department_create

    school_department_delete_parser = school_sub.add_parser(
        'department-delete',
        help='删除部门',
    )
    school_department_delete_parser.add_argument(
        '--id',
        type=str,
        help='部门id。（注：不能删除根部门；不能删除含有子部门、成员的部门）',
    )

    def _handle_school_department_delete(a: argparse.Namespace) -> dict:
        return client.school_department_delete(
            id=a.id,
        )
    table[('school', 'department-delete')] = _handle_school_department_delete

    school_department_list_parser = school_sub.add_parser(
        'department-list',
        help='获取部门列表',
    )
    school_department_list_parser.add_argument(
        '--id',
        type=str,
        help='部门id。获取指定部门及其下的子部门。 如果不填，默认获取全量组织架构',
    )

    def _handle_school_department_list(a: argparse.Namespace) -> dict:
        return client.school_department_list(
            id=a.id,
        )
    table[('school', 'department-list')] = _handle_school_department_list

    school_department_update_parser = school_sub.add_parser(
        'department-update',
        help='更新部门',
    )
    school_department_update_parser.add_argument(
        '--name',
        type=str,
        help='部门名称，如果部门为标准年级则忽略该字段。长度限制为1~32个字符，字符不能包括-:*?"<>/，*',
    )
    school_department_update_parser.add_argument(
        '--parentid',
        type=str,
        help='父部门id，32位整型',
    )
    school_department_update_parser.add_argument(
        '--id',
        type=str,
        required=True,
        help='部门id，32位整型，必须大于0。',
    )
    school_department_update_parser.add_argument(
        '--new-id',
        type=str,
        help='修改为新的id',
    )
    school_department_update_parser.add_argument(
        '--register-year',
        type=str,
        help='入学年份，32位整型，格式为YYYY，输入范围为1970～2100，仅当部门类型为年级（2）时生效',
    )
    school_department_update_parser.add_argument(
        '--standard-grade',
        type=str,
        help='标准年级，32位整型，参数值含义详见标准年级对照表，仅当部门类型为年级（2）时生效',
    )
    school_department_update_parser.add_argument(
        '--order',
        type=str,
        help='在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)',
    )
    school_department_update_parser.add_argument(
        '--department-admins',
        type=str,
        help='部门管理员列表',
    )
    school_department_update_parser.add_argument(
        '--department-admins-op',
        type=str,
        required=True,
        help='op=0表示新增或者更新，op=1表示删除管理员',
    )
    school_department_update_parser.add_argument(
        '--department-admins-userid',
        type=str,
        required=True,
        help='对应管理端的账号，企业内必须唯一。不区分大小写，长度为1~64个字节',
    )
    school_department_update_parser.add_argument(
        '--department-admins-type',
        type=str,
        help='部门管理员类型， 1表示校区负责人，2表示年级负责人，3表示班主任，4表示任课老师，5表示学段负责人',
    )
    school_department_update_parser.add_argument(
        '--department-admins-subject',
        type=str,
        help='教师的科目，仅班主任和任课老师可以设置，科目的最多15个字符，仅支持设置一个科目',
    )

    def _handle_school_department_update(a: argparse.Namespace) -> dict:
        return client.school_department_update(
            name=a.name,
            parentid=a.parentid,
            id=a.id,
            new_id=a.new_id,
            register_year=a.register_year,
            standard_grade=a.standard_grade,
            order=a.order,
            department_admins=a.department_admins,
            department_admins_op=a.department_admins_op,
            department_admins_userid=a.department_admins_userid,
            department_admins_type=a.department_admins_type,
            department_admins_subject=a.department_admins_subject,
        )
    table[('school', 'department-update')] = _handle_school_department_update

    school_sub.add_parser(
        'get-chat-create-mode',
        help='管理「班级群创建方式」',
    )

    def _handle_school_get_chat_create_mode(a: argparse.Namespace) -> dict:
        return client.school_get_chat_create_mode()
    table[('school', 'get-chat-create-mode')] = _handle_school_get_chat_create_mode

    school_get_payment_result_parser = school_sub.add_parser(
        'get-payment-result',
        help='获取学生付款结果',
    )
    school_get_payment_result_parser.add_argument(
        '--payment-id',
        type=str,
        required=True,
        help='收款项目id，由jssdk的发起班级收款接口 或者小程序的发起班级收款接口返回',
    )

    def _handle_school_get_payment_result(a: argparse.Namespace) -> dict:
        return client.school_get_payment_result(
            payment_id=a.payment_id,
        )
    table[('school', 'get-payment-result')] = _handle_school_get_payment_result

    school_get_trade_parser = school_sub.add_parser(
        'get-trade',
        help='获取订单详情',
    )
    school_get_trade_parser.add_argument(
        '--payment-id',
        type=str,
        required=True,
        help='收款项目id，由发起班级收款接口返回',
    )
    school_get_trade_parser.add_argument(
        '--trade-no',
        type=str,
        required=True,
        help='订单号，由获取学生付款结果返回',
    )

    def _handle_school_get_trade(a: argparse.Namespace) -> dict:
        return client.school_get_trade(
            payment_id=a.payment_id,
            trade_no=a.trade_no,
        )
    table[('school', 'get-trade')] = _handle_school_get_trade

    school_sub.add_parser(
        'getuserinfo',
        help='获取家校访问用户身份',
    )

    def _handle_school_getuserinfo(a: argparse.Namespace) -> dict:
        return client.school_getuserinfo()
    table[('school', 'getuserinfo')] = _handle_school_getuserinfo

    school_living_get_living_info_parser = school_sub.add_parser(
        'living-get-living-info',
        help='获取直播详情',
    )
    school_living_get_living_info_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播ID',
    )

    def _handle_school_living_get_living_info(a: argparse.Namespace) -> dict:
        return client.school_living_get_living_info(
            livingid=a.livingid,
        )
    table[('school', 'living-get-living-info')] = _handle_school_living_get_living_info

    school_living_get_unwatch_stat_parser = school_sub.add_parser(
        'living-get-unwatch-stat',
        help='获取未观看直播统计',
    )
    school_living_get_unwatch_stat_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播id',
    )
    school_living_get_unwatch_stat_parser.add_argument(
        '--next-key',
        type=str,
        help='上一次调用时返回的next_key，初次调用可以填"0"',
    )

    def _handle_school_living_get_unwatch_stat(a: argparse.Namespace) -> dict:
        return client.school_living_get_unwatch_stat(
            livingid=a.livingid,
            next_key=a.next_key,
        )
    table[('school', 'living-get-unwatch-stat')] = _handle_school_living_get_unwatch_stat

    school_living_get_unwatch_stat_v2_parser = school_sub.add_parser(
        'living-get-unwatch-stat-v2',
        help='获取未观看直播统计V2',
    )
    school_living_get_unwatch_stat_v2_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播id',
    )
    school_living_get_unwatch_stat_v2_parser.add_argument(
        '--next-cursor',
        type=str,
        help='上一次调用时返回的next_cursor，初次调用可以填"0"',
    )

    def _handle_school_living_get_unwatch_stat_v2(a: argparse.Namespace) -> dict:
        return client.school_living_get_unwatch_stat_v2(
            livingid=a.livingid,
            next_cursor=a.next_cursor,
        )
    table[('school', 'living-get-unwatch-stat-v2')] = _handle_school_living_get_unwatch_stat_v2

    school_living_get_watch_stat_parser = school_sub.add_parser(
        'living-get-watch-stat',
        help='获取观看直播统计',
    )
    school_living_get_watch_stat_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播的id',
    )
    school_living_get_watch_stat_parser.add_argument(
        '--next-key',
        type=str,
        help='上一次调用时返回的next_key，初次调用可以填"0"',
    )

    def _handle_school_living_get_watch_stat(a: argparse.Namespace) -> dict:
        return client.school_living_get_watch_stat(
            livingid=a.livingid,
            next_key=a.next_key,
        )
    table[('school', 'living-get-watch-stat')] = _handle_school_living_get_watch_stat

    school_living_get_watch_stat_v2_parser = school_sub.add_parser(
        'living-get-watch-stat-v2',
        help='获取观看直播统计V2',
    )
    school_living_get_watch_stat_v2_parser.add_argument(
        '--livingid',
        type=str,
        required=True,
        help='直播的id',
    )
    school_living_get_watch_stat_v2_parser.add_argument(
        '--next-cursor',
        type=str,
        help='上一次调用时返回的next_cursor，初次调用可以填"0"',
    )

    def _handle_school_living_get_watch_stat_v2(a: argparse.Namespace) -> dict:
        return client.school_living_get_watch_stat_v2(
            livingid=a.livingid,
            next_cursor=a.next_cursor,
        )
    table[('school', 'living-get-watch-stat-v2')] = _handle_school_living_get_watch_stat_v2

    school_set_arch_sync_mode_parser = school_sub.add_parser(
        'set-arch-sync-mode',
        help='设置家校通讯录自动同步模式',
    )
    school_set_arch_sync_mode_parser.add_argument(
        '--arch-sync-mode',
        type=str,
        required=True,
        help='家校通讯录同步模式：1-禁止将标签同步至家校通讯录，2-禁止将家校通讯录同步至标签，3-禁止家校通讯录和标签相互同步',
    )

    def _handle_school_set_arch_sync_mode(a: argparse.Namespace) -> dict:
        return client.school_set_arch_sync_mode(
            arch_sync_mode=a.arch_sync_mode,
        )
    table[('school', 'set-arch-sync-mode')] = _handle_school_set_arch_sync_mode

    school_set_upgrade_info_parser = school_sub.add_parser(
        'set-upgrade-info',
        help='修改自动升年级的配置',
    )
    school_set_upgrade_info_parser.add_argument(
        '--upgrade-time',
        type=str,
        help='自动升年级的时间，该时间戳只有月和日有效，不传则默认为传0，代表的1月1号',
    )
    school_set_upgrade_info_parser.add_argument(
        '--upgrade-switch',
        type=str,
        help='开启或关闭自动升年级。0：表示关闭，1：表示开启，不传默认关闭，传所有非1的值也视为关闭',
    )

    def _handle_school_set_upgrade_info(a: argparse.Namespace) -> dict:
        return client.school_set_upgrade_info(
            upgrade_time=a.upgrade_time,
            upgrade_switch=a.upgrade_switch,
        )
    table[('school', 'set-upgrade-info')] = _handle_school_set_upgrade_info

    school_user_batch_create_parent_parser = school_sub.add_parser(
        'user-batch-create-parent',
        help='批量创建家长',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents',
        type=str,
        required=True,
        help='家长列表，每次最多100个',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents-parent-userid',
        type=str,
        required=True,
        help='家长UserID。学校内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents-mobile',
        type=str,
        required=True,
        help='家长手机号',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents-to-invite',
        help='是否发起邀请，默认为true',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents-children',
        type=str,
        required=True,
        help='家长的孩子列表，最多10个',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents-children-student-userid',
        type=str,
        required=True,
        help='学生的UserID',
    )
    school_user_batch_create_parent_parser.add_argument(
        '--parents-children-relation',
        type=str,
        required=True,
        help='家长与学生的关系，最长32字节',
    )

    def _handle_school_user_batch_create_parent(a: argparse.Namespace) -> dict:
        return client.school_user_batch_create_parent(
            parents=a.parents,
            parents_parent_userid=a.parents_parent_userid,
            parents_mobile=a.parents_mobile,
            parents_to_invite=a.parents_to_invite,
            parents_children=a.parents_children,
            parents_children_student_userid=a.parents_children_student_userid,
            parents_children_relation=a.parents_children_relation,
        )
    table[('school', 'user-batch-create-parent')] = _handle_school_user_batch_create_parent

    school_user_batch_create_student_parser = school_sub.add_parser(
        'user-batch-create-student',
        help='批量创建学生',
    )
    school_user_batch_create_student_parser.add_argument(
        '--students',
        type=str,
        required=True,
        help='学生列表，每次最多100个学生',
    )
    school_user_batch_create_student_parser.add_argument(
        '--students-student-userid',
        type=str,
        required=True,
        help='学生UserID。学校内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_batch_create_student_parser.add_argument(
        '--students-mobile',
        type=str,
        help='学生手机号',
    )
    school_user_batch_create_student_parser.add_argument(
        '--students-to-invite',
        help='是否发起邀请，默认为true',
    )
    school_user_batch_create_student_parser.add_argument(
        '--students-name',
        type=str,
        required=True,
        help='学生姓名，长度为1~32个字符',
    )
    school_user_batch_create_student_parser.add_argument(
        '--students-department',
        type=str,
        required=True,
        help='学生所在的班级id列表,不超过20个',
    )

    def _handle_school_user_batch_create_student(a: argparse.Namespace) -> dict:
        return client.school_user_batch_create_student(
            students=a.students,
            students_student_userid=a.students_student_userid,
            students_mobile=a.students_mobile,
            students_to_invite=a.students_to_invite,
            students_name=a.students_name,
            students_department=a.students_department,
        )
    table[('school', 'user-batch-create-student')] = _handle_school_user_batch_create_student

    school_user_batch_delete_parent_parser = school_sub.add_parser(
        'user-batch-delete-parent',
        help='批量删除家长',
    )
    school_user_batch_delete_parent_parser.add_argument(
        '--useridlist',
        type=str,
        required=True,
        help='家长的userid列表，每次最多100个',
    )

    def _handle_school_user_batch_delete_parent(a: argparse.Namespace) -> dict:
        return client.school_user_batch_delete_parent(
            useridlist=a.useridlist,
        )
    table[('school', 'user-batch-delete-parent')] = _handle_school_user_batch_delete_parent

    school_user_batch_delete_student_parser = school_sub.add_parser(
        'user-batch-delete-student',
        help='批量删除学生',
    )
    school_user_batch_delete_student_parser.add_argument(
        '--useridlist',
        type=str,
        required=True,
        help='学生的userid列表，每次最多100个',
    )

    def _handle_school_user_batch_delete_student(a: argparse.Namespace) -> dict:
        return client.school_user_batch_delete_student(
            useridlist=a.useridlist,
        )
    table[('school', 'user-batch-delete-student')] = _handle_school_user_batch_delete_student

    school_user_batch_update_parent_parser = school_sub.add_parser(
        'user-batch-update-parent',
        help='批量更新家长',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents',
        type=str,
        help='家长列表，每次最多100个',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents-parent-userid',
        type=str,
        required=True,
        help='家长UserID。学校内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents-new-parent-userid',
        type=str,
        help='更新的家长UserID。不能与已经存在的家长userid相同。每个家长仅能更新一次。',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents-mobile',
        type=str,
        help='家长手机号',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents-children',
        type=str,
        help='家长的孩子列表，最多10个',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents-children-student-userid',
        type=str,
        required=True,
        help='学生的UserID',
    )
    school_user_batch_update_parent_parser.add_argument(
        '--parents-children-relation',
        type=str,
        required=True,
        help='家长与学生的关系，最长32字节',
    )

    def _handle_school_user_batch_update_parent(a: argparse.Namespace) -> dict:
        return client.school_user_batch_update_parent(
            parents=a.parents,
            parents_parent_userid=a.parents_parent_userid,
            parents_new_parent_userid=a.parents_new_parent_userid,
            parents_mobile=a.parents_mobile,
            parents_children=a.parents_children,
            parents_children_student_userid=a.parents_children_student_userid,
            parents_children_relation=a.parents_children_relation,
        )
    table[('school', 'user-batch-update-parent')] = _handle_school_user_batch_update_parent

    school_user_batch_update_student_parser = school_sub.add_parser(
        'user-batch-update-student',
        help='批量更新学生',
    )
    school_user_batch_update_student_parser.add_argument(
        '--students',
        type=str,
        help='学生列表，每次最多100个',
    )
    school_user_batch_update_student_parser.add_argument(
        '--students-student-userid',
        type=str,
        required=True,
        help='学生UserID。学校内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_batch_update_student_parser.add_argument(
        '--students-mobile',
        type=str,
        help='学生手机号',
    )
    school_user_batch_update_student_parser.add_argument(
        '--students-new-student-userid',
        type=str,
        help='要变更的学生UserID,不能与已存在的UserID相同。每个学生仅能修改一次。',
    )
    school_user_batch_update_student_parser.add_argument(
        '--students-name',
        type=str,
        help='学生姓名，长度为1~32个字符',
    )
    school_user_batch_update_student_parser.add_argument(
        '--students-department',
        type=str,
        help='学生所在的班级id列表,不超过20个',
    )

    def _handle_school_user_batch_update_student(a: argparse.Namespace) -> dict:
        return client.school_user_batch_update_student(
            students=a.students,
            students_student_userid=a.students_student_userid,
            students_mobile=a.students_mobile,
            students_new_student_userid=a.students_new_student_userid,
            students_name=a.students_name,
            students_department=a.students_department,
        )
    table[('school', 'user-batch-update-student')] = _handle_school_user_batch_update_student

    school_user_create_parent_parser = school_sub.add_parser(
        'user-create-parent',
        help='创建家长',
    )
    school_user_create_parent_parser.add_argument(
        '--parent-userid',
        type=str,
        required=True,
        help='家长UserID。学校内必须唯一，可以与企业通讯录内成员UserID相同。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_create_parent_parser.add_argument(
        '--mobile',
        type=str,
        required=True,
        help='家长手机号',
    )
    school_user_create_parent_parser.add_argument(
        '--to-invite',
        help='是否发起邀请，默认为true，仅验证的学校才能发起邀请。',
    )
    school_user_create_parent_parser.add_argument(
        '--children',
        type=str,
        required=True,
        help='家长的孩子列表，最多10',
    )
    school_user_create_parent_parser.add_argument(
        '--children-student-userid',
        type=str,
        required=True,
        help='学生的UserID',
    )
    school_user_create_parent_parser.add_argument(
        '--children-relation',
        type=str,
        required=True,
        help='家长与学生的关系，最长32字节',
    )

    def _handle_school_user_create_parent(a: argparse.Namespace) -> dict:
        return client.school_user_create_parent(
            parent_userid=a.parent_userid,
            mobile=a.mobile,
            to_invite=a.to_invite,
            children=a.children,
            children_student_userid=a.children_student_userid,
            children_relation=a.children_relation,
        )
    table[('school', 'user-create-parent')] = _handle_school_user_create_parent

    school_user_create_student_parser = school_sub.add_parser(
        'user-create-student',
        help='创建学生',
    )
    school_user_create_student_parser.add_argument(
        '--student-userid',
        type=str,
        required=True,
        help='学生UserID。学校内必须唯一，可以与企业通讯录内成员UserID相同。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_create_student_parser.add_argument(
        '--mobile',
        type=str,
        help='学生手机号',
    )
    school_user_create_student_parser.add_argument(
        '--to-invite',
        help='是否发起邀请，默认为true，仅验证的学校才能发起邀请。',
    )
    school_user_create_student_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='学生姓名，长度为1~32个字符',
    )
    school_user_create_student_parser.add_argument(
        '--department',
        type=str,
        required=True,
        help='学生所在的班级id列表,不超过20个',
    )

    def _handle_school_user_create_student(a: argparse.Namespace) -> dict:
        return client.school_user_create_student(
            student_userid=a.student_userid,
            mobile=a.mobile,
            to_invite=a.to_invite,
            name=a.name,
            department=a.department,
        )
    table[('school', 'user-create-student')] = _handle_school_user_create_student

    school_user_delete_parent_parser = school_sub.add_parser(
        'user-delete-parent',
        help='删除家长',
    )
    school_user_delete_parent_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='家校通信录中家长的userid',
    )

    def _handle_school_user_delete_parent(a: argparse.Namespace) -> dict:
        return client.school_user_delete_parent(
            userid=a.userid,
        )
    table[('school', 'user-delete-parent')] = _handle_school_user_delete_parent

    school_user_delete_student_parser = school_sub.add_parser(
        'user-delete-student',
        help='删除学生',
    )
    school_user_delete_student_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='家校通信录中学生的userid',
    )

    def _handle_school_user_delete_student(a: argparse.Namespace) -> dict:
        return client.school_user_delete_student(
            userid=a.userid,
        )
    table[('school', 'user-delete-student')] = _handle_school_user_delete_student

    school_user_get_parser = school_sub.add_parser(
        'user-get',
        help='读取学生或家长',
    )
    school_user_get_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='家校通讯录的userid，家长或者学生的userid。不区分大小写，长度为1~64个字节',
    )

    def _handle_school_user_get(a: argparse.Namespace) -> dict:
        return client.school_user_get(
            userid=a.userid,
        )
    table[('school', 'user-get')] = _handle_school_user_get

    school_user_list_parent_parser = school_sub.add_parser(
        'user-list-parent',
        help='获取部门家长详情',
    )
    school_user_list_parent_parser.add_argument(
        '--department-id',
        type=str,
        required=True,
        help='获取的部门id',
    )

    def _handle_school_user_list_parent(a: argparse.Namespace) -> dict:
        return client.school_user_list_parent(
            department_id=a.department_id,
        )
    table[('school', 'user-list-parent')] = _handle_school_user_list_parent

    school_user_update_parent_parser = school_sub.add_parser(
        'user-update-parent',
        help='更新家长',
    )
    school_user_update_parent_parser.add_argument(
        '--parent-userid',
        type=str,
        required=True,
        help='家长UserID。学校内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_update_parent_parser.add_argument(
        '--new-parent-userid',
        type=str,
        help='更新的家长UserID。不能与已经存在的家长UserID相同。每个家长仅能更新一次。',
    )
    school_user_update_parent_parser.add_argument(
        '--mobile',
        type=str,
        help='家长手机号',
    )
    school_user_update_parent_parser.add_argument(
        '--children',
        type=str,
        help='家长的孩子列表，该字段是全量更新，如果孩子列表为空则忽略该字段，最多10个',
    )
    school_user_update_parent_parser.add_argument(
        '--children-student-userid',
        type=str,
        required=True,
        help='学生的UserID',
    )
    school_user_update_parent_parser.add_argument(
        '--children-relation',
        type=str,
        required=True,
        help='家长与学生的关系，最长32字节',
    )

    def _handle_school_user_update_parent(a: argparse.Namespace) -> dict:
        return client.school_user_update_parent(
            parent_userid=a.parent_userid,
            new_parent_userid=a.new_parent_userid,
            mobile=a.mobile,
            children=a.children,
            children_student_userid=a.children_student_userid,
            children_relation=a.children_relation,
        )
    table[('school', 'user-update-parent')] = _handle_school_user_update_parent

    school_user_update_student_parser = school_sub.add_parser(
        'user-update-student',
        help='更新学生',
    )
    school_user_update_student_parser.add_argument(
        '--student-userid',
        type=str,
        required=True,
        help='学生UserID。学校内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。',
    )
    school_user_update_student_parser.add_argument(
        '--mobile',
        type=str,
        help='学生手机号',
    )
    school_user_update_student_parser.add_argument(
        '--new-student-userid',
        type=str,
        help='要变更的学生UserID,不能与已存在的UserID相同。每个学生仅能修改一次。',
    )
    school_user_update_student_parser.add_argument(
        '--name',
        type=str,
        help='学生姓名，长度为1~32个字符',
    )
    school_user_update_student_parser.add_argument(
        '--department',
        type=str,
        help='学生所在的班级id列表,不超过20个',
    )

    def _handle_school_user_update_student(a: argparse.Namespace) -> dict:
        return client.school_user_update_student(
            student_userid=a.student_userid,
            mobile=a.mobile,
            new_student_userid=a.new_student_userid,
            name=a.name,
            department=a.department,
        )
    table[('school', 'user-update-student')] = _handle_school_user_update_student

    security_parser = subparsers.add_parser(
        'security',
        help='security',
    )
    security_sub = security_parser.add_subparsers(dest='__action', required=True)

    security_admin_oper_log_list_parser = security_sub.add_parser(
        'admin-oper-log-list',
        help='获取管理端操作日志',
    )
    security_admin_oper_log_list_parser.add_argument(
        '--start-time',
        type=str,
        required=True,
        help='开始时间 取值范围：不早于180天前',
    )
    security_admin_oper_log_list_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='结束时间 取值范围：大于start_time，小于当前时间。开始时间和结束时间之间的跨度不能超过7天。',
    )
    security_admin_oper_log_list_parser.add_argument(
        '--oper-type',
        type=str,
        help='操作类型。不填表示全部 取值范围目前支持如下： 2 - 权限管理变更 3 - 成员与部门变更 7 - 其它 8 - 应用变更 11 - 通讯录与聊天管理 12 - 企业信息管理 13 - 外部联系人管理',
    )
    security_admin_oper_log_list_parser.add_argument(
        '--userid',
        type=str,
        help='操作者userid',
    )
    security_admin_oper_log_list_parser.add_argument(
        '--cusor',
        type=str,
        help='分页游标。不填表示首页',
    )
    security_admin_oper_log_list_parser.add_argument(
        '--limit',
        type=int,
        help='最大记录数。不填默认最多获取400个记录 取值范围：1 ~ 400 注意：不保证每次返回的数据刚好为指定limit ，必须用返回的 has_more 判断是否继续请求',
    )

    def _handle_security_admin_oper_log_list(a: argparse.Namespace) -> dict:
        return client.security_admin_oper_log_list(
            start_time=a.start_time,
            end_time=a.end_time,
            oper_type=a.oper_type,
            userid=a.userid,
            cusor=a.cusor,
            limit=a.limit,
        )
    table[('security', 'admin-oper-log-list')] = _handle_security_admin_oper_log_list

    security_get_screen_oper_record_parser = security_sub.add_parser(
        'get-screen-oper-record',
        help='截屏/录屏管理',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--start-time',
        type=int,
        required=True,
        help='开始时间',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--end-time',
        type=int,
        required=True,
        help='结束时间，开始时间到结束时间的范围不能超过14天',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--userid-list',
        type=str,
        help='需要查询的截屏操作者的userid，单次最多可以传100个用户。设置的userid需要在应用的可见范围内',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--department-id-list',
        type=str,
        help='需要查询的截屏操作者部门的department_id，单次最多可以传100个部门id。设置的department_id需要在应用的可见范围内',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--screen-shot-type',
        type=int,
        help='截屏内容的类型，不设置默认为全部 1: 聊天 2: 通讯录 3: 邮件 4: 文件 5: 日程 6: 其他',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--cursor',
        type=str,
        help='由企业微信后台返回，第一次调用可不填',
    )
    security_get_screen_oper_record_parser.add_argument(
        '--limit',
        type=int,
        help='限制返回的条数，最多设置为1000',
    )

    def _handle_security_get_screen_oper_record(a: argparse.Namespace) -> dict:
        return client.security_get_screen_oper_record(
            start_time=a.start_time,
            end_time=a.end_time,
            userid_list=a.userid_list,
            department_id_list=a.department_id_list,
            screen_shot_type=a.screen_shot_type,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('security', 'get-screen-oper-record')] = _handle_security_get_screen_oper_record

    security_sub.add_parser(
        'get-server-domain-ip',
        help='获取企业微信域名IP信息',
    )

    def _handle_security_get_server_domain_ip(a: argparse.Namespace) -> dict:
        return client.security_get_server_domain_ip()
    table[('security', 'get-server-domain-ip')] = _handle_security_get_server_domain_ip

    security_member_oper_log_list_parser = security_sub.add_parser(
        'member-oper-log-list',
        help='获取成员操作记录',
    )
    security_member_oper_log_list_parser.add_argument(
        '--start-time',
        type=str,
        required=True,
        help='开始时间 取值范围：不早于180天前',
    )
    security_member_oper_log_list_parser.add_argument(
        '--end-time',
        type=str,
        required=True,
        help='结束时间 取值范围：大于start_time，小于当前时间。开始时间和结束时间之间的跨度不能超过7天。',
    )
    security_member_oper_log_list_parser.add_argument(
        '--oper-type',
        type=str,
        help='操作类型。不填表示全部 取值范围目前支持如下： 1 - 添加外部联系人 2 - 删除外部联系人 3 - 标记企业客户 4 - 新设备登录 5 - 更换手机号 6 - 绑定微信号 7 - 换绑微信号 8 - 邀请成员 9 - 封禁登录 11 - 修改昵称 12 - 修改姓名 13 - 副设备登录 15 - 确认高级功能订单 16 - 应用变更 17 - 确认会话内容存档订单 20 - 封禁互通 21 - 锁定设备',
    )
    security_member_oper_log_list_parser.add_argument(
        '--userid',
        type=str,
        help='操作者userid过滤，需要在应用可见范围内。可不填',
    )
    security_member_oper_log_list_parser.add_argument(
        '--cursor',
        type=str,
        help='分页游标。不填表示首页',
    )
    security_member_oper_log_list_parser.add_argument(
        '--limit',
        type=int,
        help='最大记录数。不填默认最多获取400个记录 取值范围：1 ~ 400 注意：不保证每次返回的数据刚好为指定limit，必须用返回的 has_more 判断是否继续请求',
    )

    def _handle_security_member_oper_log_list(a: argparse.Namespace) -> dict:
        return client.security_member_oper_log_list(
            start_time=a.start_time,
            end_time=a.end_time,
            oper_type=a.oper_type,
            userid=a.userid,
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('security', 'member-oper-log-list')] = _handle_security_member_oper_log_list

    security_trustdevice_import_parser = security_sub.add_parser(
        'trustdevice-import',
        help='设备管理',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-system',
        type=str,
        required=True,
        help='设备的类型，Windows或Mac',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-mac-addr',
        type=str,
        required=True,
        help='设备MAC地址，当system为Windows时必填，Mac选填，每个设备最多100个',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-motherboard-uuid',
        type=str,
        help='主板UUID，当system为Windows可选填此参数',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-harddisk-uuid',
        type=str,
        help='硬盘序列号，当system为Windows时可选填此参数，每个设备最多100个',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-domain',
        type=str,
        help='Windows域名，当system为Windows时可选填此参数',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-pc-name',
        type=str,
        help='Windows计算机名，当system为Windows时可选填此参数',
    )
    security_trustdevice_import_parser.add_argument(
        '--device-list-seq-no',
        type=str,
        required=True,
        help='Mac序列号，当system为Mac时必填',
    )

    def _handle_security_trustdevice_import(a: argparse.Namespace) -> dict:
        return client.security_trustdevice_import(
            device_list_system=a.device_list_system,
            device_list_mac_addr=a.device_list_mac_addr,
            device_list_motherboard_uuid=a.device_list_motherboard_uuid,
            device_list_harddisk_uuid=a.device_list_harddisk_uuid,
            device_list_domain=a.device_list_domain,
            device_list_pc_name=a.device_list_pc_name,
            device_list_seq_no=a.device_list_seq_no,
        )
    table[('security', 'trustdevice-import')] = _handle_security_trustdevice_import

    security_vip_list_parser = security_sub.add_parser(
        'vip-list',
        help='获取高级功能账号列表',
    )
    security_vip_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    security_vip_list_parser.add_argument(
        '--limit',
        type=int,
        help='用于分页查询，每次请求返回的数据上限。默认100，最大200 注意：不保证每次返回的数据刚好为指定limit，必须用返回的has_more判断是否继续请求',
    )

    def _handle_security_vip_list(a: argparse.Namespace) -> dict:
        return client.security_vip_list(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('security', 'vip-list')] = _handle_security_vip_list

    security_vip_submit_batch_add_job_parser = security_sub.add_parser(
        'vip-submit-batch-add-job',
        help='分配高级功能账号',
    )
    security_vip_submit_batch_add_job_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要分配高级功能的企业成员userid列表，单次操作最大限制100个',
    )

    def _handle_security_vip_submit_batch_add_job(a: argparse.Namespace) -> dict:
        return client.security_vip_submit_batch_add_job(
            userid_list=a.userid_list,
        )
    table[('security', 'vip-submit-batch-add-job')] = _handle_security_vip_submit_batch_add_job

    security_vip_submit_batch_del_job_parser = security_sub.add_parser(
        'vip-submit-batch-del-job',
        help='取消高级功能账号',
    )
    security_vip_submit_batch_del_job_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要撤销分配高级功能的企业成员userid列表，单次操作最多限制100个',
    )

    def _handle_security_vip_submit_batch_del_job(a: argparse.Namespace) -> dict:
        return client.security_vip_submit_batch_del_job(
            userid_list=a.userid_list,
        )
    table[('security', 'vip-submit-batch-del-job')] = _handle_security_vip_submit_batch_del_job

    tags_parser = subparsers.add_parser(
        'tags',
        help='tags',
    )
    tags_sub = tags_parser.add_subparsers(dest='__action', required=True)

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

    ticket_parser = subparsers.add_parser(
        'ticket',
        help='ticket',
    )
    ticket_sub = ticket_parser.add_subparsers(dest='__action', required=True)

    ticket_sub.add_parser(
        'get',
        help='JS-SDK 签名算法',
    )

    def _handle_ticket_get(a: argparse.Namespace) -> dict:
        return client.ticket_get()
    table[('ticket', 'get')] = _handle_ticket_get

    unknown_parser = subparsers.add_parser(
        'unknown',
        help='unknown',
    )
    unknown_sub = unknown_parser.add_subparsers(dest='__action', required=True)

    unknown_sub.add_parser(
        'cgi-bin-get-jsapi-ticket',
        help='接口代码参考示例',
    )

    def _handle_unknown_cgi_bin_get_jsapi_ticket(a: argparse.Namespace) -> dict:
        return client.unknown_cgi_bin_get_jsapi_ticket()
    table[('unknown', 'cgi-bin-get-jsapi-ticket')] = _handle_unknown_cgi_bin_get_jsapi_ticket

    unknown_cgi_bin_get_launch_code_parser = unknown_sub.add_parser(
        'cgi-bin-get-launch-code',
        help='打开个人聊天窗口schema',
    )
    unknown_cgi_bin_get_launch_code_parser.add_argument(
        '--launch-code',
        type=str,
        required=True,
        help='唤起页面的code，可通过获取唤起企业微信code接口获取',
    )

    def _handle_unknown_cgi_bin_get_launch_code(a: argparse.Namespace) -> dict:
        return client.unknown_cgi_bin_get_launch_code(
            launch_code=a.launch_code,
        )
    table[('unknown', 'cgi-bin-get-launch-code')] = _handle_unknown_cgi_bin_get_launch_code

    users_parser = subparsers.add_parser(
        'users',
        help='users',
    )
    users_sub = users_parser.add_subparsers(dest='__action', required=True)

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

    users_getuserinfo_parser = users_sub.add_parser(
        'getuserinfo',
        help='Harmony应用',
    )
    users_getuserinfo_parser.add_argument(
        '--appId',
        type=str,
        required=True,
        help='企业唯一标识。创建企业后显示在，我的企业 CorpID字段',
    )
    users_getuserinfo_parser.add_argument(
        '--agentId',
        type=str,
        required=True,
        help='应用唯一标识。显示在具体应用下的 AgentId字段',
    )
    users_getuserinfo_parser.add_argument(
        '--scopes',
        type=str,
        required=True,
        help='授权域，现在只支持snsapi_base',
    )

    def _handle_users_getuserinfo(a: argparse.Namespace) -> dict:
        return client.users_getuserinfo(
            appId=a.appId,
            agentId=a.agentId,
            scopes=a.scopes,
        )
    table[('users', 'getuserinfo')] = _handle_users_getuserinfo

    wedoc_parser = subparsers.add_parser(
        'wedoc',
        help='wedoc',
    )
    wedoc_sub = wedoc_parser.add_subparsers(dest='__action', required=True)

    wedoc_doc_share_parser = wedoc_sub.add_parser(
        'doc-share',
        help='分享文档',
    )
    wedoc_doc_share_parser.add_argument(
        '--docid',
        type=str,
        help='文档id（docid、formid只能填其中一个）',
    )

    def _handle_wedoc_doc_share(a: argparse.Namespace) -> dict:
        return client.wedoc_doc_share(
            docid=a.docid,
        )
    table[('wedoc', 'doc-share')] = _handle_wedoc_doc_share

    wedoc_document_batch_update_parser = wedoc_sub.add_parser(
        'document-batch-update',
        help='编辑文档内容',
    )
    wedoc_document_batch_update_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_document_batch_update_parser.add_argument(
        '--version',
        type=str,
        help='操作的文档版本, 该参数可以通过获取文档内容接口获得。操作后文档版本将更新一版。要更新的文档版本与最新文档版本相差不能超过100个。',
    )
    wedoc_document_batch_update_parser.add_argument(
        '--requests',
        type=str,
        required=True,
        help='更新操作列表，详见 UpdateRequest',
    )

    def _handle_wedoc_document_batch_update(a: argparse.Namespace) -> dict:
        return client.wedoc_document_batch_update(
            docid=a.docid,
            version=a.version,
            requests=a.requests,
        )
    table[('wedoc', 'document-batch-update')] = _handle_wedoc_document_batch_update

    wedoc_document_get_parser = wedoc_sub.add_parser(
        'document-get',
        help='获取文档数据',
    )
    wedoc_document_get_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )

    def _handle_wedoc_document_get(a: argparse.Namespace) -> dict:
        return client.wedoc_document_get(
            docid=a.docid,
        )
    table[('wedoc', 'document-get')] = _handle_wedoc_document_get

    wedoc_get_doc_base_info_parser = wedoc_sub.add_parser(
        'get-doc-base-info',
        help='获取文档基础信息',
    )
    wedoc_get_doc_base_info_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档docid',
    )

    def _handle_wedoc_get_doc_base_info(a: argparse.Namespace) -> dict:
        return client.wedoc_get_doc_base_info(
            docid=a.docid,
        )
    table[('wedoc', 'get-doc-base-info')] = _handle_wedoc_get_doc_base_info

    wedoc_get_form_answer_parser = wedoc_sub.add_parser(
        'get-form-answer',
        help='读取收集表答案',
    )
    wedoc_get_form_answer_parser.add_argument(
        '--repeated-id',
        type=str,
        required=True,
        help='操作的收集表周期id',
    )
    wedoc_get_form_answer_parser.add_argument(
        '--answer-ids',
        type=str,
        required=True,
        help='需要拉取的答案列表，批次大小最大100',
    )

    def _handle_wedoc_get_form_answer(a: argparse.Namespace) -> dict:
        return client.wedoc_get_form_answer(
            repeated_id=a.repeated_id,
            answer_ids=a.answer_ids,
        )
    table[('wedoc', 'get-form-answer')] = _handle_wedoc_get_form_answer

    wedoc_get_form_info_parser = wedoc_sub.add_parser(
        'get-form-info',
        help='获取收集表信息',
    )
    wedoc_get_form_info_parser.add_argument(
        '--formid',
        type=str,
        required=True,
        help='操作的收集表ID',
    )

    def _handle_wedoc_get_form_info(a: argparse.Namespace) -> dict:
        return client.wedoc_get_form_info(
            formid=a.formid,
        )
    table[('wedoc', 'get-form-info')] = _handle_wedoc_get_form_info

    wedoc_get_form_statistic_parser = wedoc_sub.add_parser(
        'get-form-statistic',
        help='收集表的统计信息查询',
    )
    wedoc_get_form_statistic_parser.add_argument(
        '--repeated-id',
        type=str,
        required=True,
        help='操作的收集表的repeated_id,来源于get_form_info的返回',
    )
    wedoc_get_form_statistic_parser.add_argument(
        '--req-type',
        type=str,
        required=True,
        help='请求类型 1:只获取统计结果 2:获取已提交列表 3:获取未提交列表',
    )
    wedoc_get_form_statistic_parser.add_argument(
        '--start-time',
        type=str,
        help='拉取已提交列表时必填，其余type不填。筛选开始时间，以当天的00:00:00开始筛选',
    )
    wedoc_get_form_statistic_parser.add_argument(
        '--end-time',
        type=str,
        help='拉取已提交列表时必填，其余type不填。筛选结束时间，以当天的23:59:59结束筛选',
    )
    wedoc_get_form_statistic_parser.add_argument(
        '--limit',
        type=str,
        help='分页拉取时批次大小，最大10000',
    )
    wedoc_get_form_statistic_parser.add_argument(
        '--cursor',
        type=str,
        help='分页拉取的游标，首次不传',
    )

    def _handle_wedoc_get_form_statistic(a: argparse.Namespace) -> dict:
        return client.wedoc_get_form_statistic(
            repeated_id=a.repeated_id,
            req_type=a.req_type,
            start_time=a.start_time,
            end_time=a.end_time,
            limit=a.limit,
            cursor=a.cursor,
        )
    table[('wedoc', 'get-form-statistic')] = _handle_wedoc_get_form_statistic

    wedoc_image_upload_parser = wedoc_sub.add_parser(
        'image-upload',
        help='上传文档图片',
    )
    wedoc_image_upload_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档ID，通过新建文档接口创建后获得',
    )
    wedoc_image_upload_parser.add_argument(
        '--base64-content',
        type=str,
        required=True,
        help='base64之后的图片内容',
    )

    def _handle_wedoc_image_upload(a: argparse.Namespace) -> dict:
        return client.wedoc_image_upload(
            docid=a.docid,
            base64_content=a.base64_content,
        )
    table[('wedoc', 'image-upload')] = _handle_wedoc_image_upload

    wedoc_mod_doc_safty_setting_parser = wedoc_sub.add_parser(
        'mod-doc-safty-setting',
        help='修改文档安全设置',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='操作的文档id',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--enable-readonly-copy',
        help='是否允许只读成员复制、下载文档，有值则覆盖',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--watermark',
        type=str,
        help='水印设置',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--margin-type',
        type=str,
        help='水印疏密度，1:稀疏，2:紧密',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--show-visitor-name',
        help='是否展示访问者名字水印，有值则覆盖',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--show-text',
        help='是否展示文本水印，有值则覆盖',
    )
    wedoc_mod_doc_safty_setting_parser.add_argument(
        '--text',
        type=str,
        help='文字水印的文字，有值则覆盖',
    )

    def _handle_wedoc_mod_doc_safty_setting(a: argparse.Namespace) -> dict:
        return client.wedoc_mod_doc_safty_setting(
            docid=a.docid,
            enable_readonly_copy=a.enable_readonly_copy,
            watermark=a.watermark,
            margin_type=a.margin_type,
            show_visitor_name=a.show_visitor_name,
            show_text=a.show_text,
            text=a.text,
        )
    table[('wedoc', 'mod-doc-safty-setting')] = _handle_wedoc_mod_doc_safty_setting

    wedoc_modify_form_parser = wedoc_sub.add_parser(
        'modify-form',
        help='编辑收集表',
    )
    wedoc_modify_form_parser.add_argument(
        '--oper',
        type=str,
        required=True,
        help='操作类型。1：全量修改问题；2：全量修改设置',
    )
    wedoc_modify_form_parser.add_argument(
        '--formid',
        type=str,
        required=True,
        help='收集表id',
    )
    wedoc_modify_form_parser.add_argument(
        '--form-title',
        type=str,
        help='收集表标题（操作1修改）',
    )
    wedoc_modify_form_parser.add_argument(
        '--form-desc',
        type=str,
        help='收集表描述（操作1修改）',
    )
    wedoc_modify_form_parser.add_argument(
        '--form-header',
        type=str,
        help='收集表表头背景图链接（操作1修改）',
    )
    wedoc_modify_form_parser.add_argument(
        '--form-question',
        type=str,
        help='收集表的问题列表（操作1修改）',
    )
    wedoc_modify_form_parser.add_argument(
        '--items',
        type=str,
        required=True,
        help='问题数组',
    )
    wedoc_modify_form_parser.add_argument(
        '--question-id',
        type=str,
        required=True,
        help='问题id，从1开始。如果是家校范围收集表，id从2开始。',
    )
    wedoc_modify_form_parser.add_argument(
        '--title',
        type=str,
        required=True,
        help='问题描述',
    )
    wedoc_modify_form_parser.add_argument(
        '--pos',
        type=str,
        required=True,
        help='问题序号，从1开始。',
    )
    wedoc_modify_form_parser.add_argument(
        '--status',
        type=str,
        required=True,
        help='问题状态。1：正常；2：被删除',
    )
    wedoc_modify_form_parser.add_argument(
        '--reply-type',
        type=str,
        required=True,
        help='问题类型。1：文本；2：单选；3：多选；5：位置；9：图片；10：文件；11：日期；14：时间；15：下拉列表；16：体温；17：签名；18：部门；19：成员 22：时长',
    )
    wedoc_modify_form_parser.add_argument(
        '--must-reply',
        required=True,
        help='是否必答',
    )
    wedoc_modify_form_parser.add_argument(
        '--note',
        type=str,
        help='问题备注',
    )
    wedoc_modify_form_parser.add_argument(
        '--placeholder',
        type=str,
        help='编辑提示',
    )
    wedoc_modify_form_parser.add_argument(
        '--question-extend-setting',
        type=str,
        help='问题的额外设置。不同问题类型有相应的设置，详见question_extend_setting字段描述',
    )
    wedoc_modify_form_parser.add_argument(
        '--option-item',
        type=str,
        required=True,
        help='单选/多选/下拉列表题的选项列表',
    )
    wedoc_modify_form_parser.add_argument(
        '--key',
        type=str,
        required=True,
        help='选项key（1，2，3...）',
    )
    wedoc_modify_form_parser.add_argument(
        '--value',
        type=str,
        required=True,
        help='选项内容',
    )
    wedoc_modify_form_parser.add_argument(
        '--status-1',
        type=str,
        required=True,
        help='选项状态。1：正常；2：被删除',
    )
    wedoc_modify_form_parser.add_argument(
        '--form-setting',
        type=str,
        help='收集表设置（操作2修改）',
    )
    wedoc_modify_form_parser.add_argument(
        '--fill-out-auth',
        type=str,
        required=True,
        help='填写权限。0：所有人；1：企业内指定人/部门。若收集表当前为家校范围，则无法修改。',
    )
    wedoc_modify_form_parser.add_argument(
        '--fill-in-range',
        type=str,
        help='指定的可填写的人/部门',
    )
    wedoc_modify_form_parser.add_argument(
        '--userids',
        type=str,
        help='企业成员userid列表',
    )
    wedoc_modify_form_parser.add_argument(
        '--departmentids',
        type=str,
        help='部门id列表',
    )
    wedoc_modify_form_parser.add_argument(
        '--setting-manager-range',
        type=str,
        help='收集表管理员',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info',
        type=str,
        help='定时重复设置项',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-enable',
        help='是否开启定时重复',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-remind-time',
        type=str,
        help='提醒时间',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-repeat-type',
        type=str,
        help='重复类型。0：每周；1：每天；2：每月',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-week-flag',
        type=str,
        help='每周几重复，只能repeat_type = 0 时填写。1：星期一；2：星期二；4：星期三；8：星期四；16：星期五；32：星期六；64：星期日',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-skip-holiday',
        help='自动跳过节假日，只能repeat_type = 1 时填写。',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-day-of-month',
        type=str,
        help='每月的第几天（1 - 31），只能repeat_type = 2时填写',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-repeat-info-fork-finish-type',
        help='是否允许补填。0：允许；1：仅当天；2：最后五天内；3：一个月内；4：下一次生成前',
    )
    wedoc_modify_form_parser.add_argument(
        '--allow-multi-fill',
        help='是否允许每人提交多份。默认false',
    )
    wedoc_modify_form_parser.add_argument(
        '--timed-finish',
        type=str,
        help='定时关闭。定时重复与定时结束互斥，若都填，优先定时重复',
    )
    wedoc_modify_form_parser.add_argument(
        '--can-anonymous',
        help='是否支持匿名填写。默认false',
    )
    wedoc_modify_form_parser.add_argument(
        '--can-notify-submit',
        help='是否有回复时提醒。默认false',
    )

    def _handle_wedoc_modify_form(a: argparse.Namespace) -> dict:
        return client.wedoc_modify_form(
            oper=a.oper,
            formid=a.formid,
            form_title=a.form_title,
            form_desc=a.form_desc,
            form_header=a.form_header,
            form_question=a.form_question,
            items=a.items,
            question_id=a.question_id,
            title=a.title,
            pos=a.pos,
            status=a.status,
            reply_type=a.reply_type,
            must_reply=a.must_reply,
            note=a.note,
            placeholder=a.placeholder,
            question_extend_setting=a.question_extend_setting,
            option_item=a.option_item,
            key=a.key,
            value=a.value,
            status_1=a.status_1,
            form_setting=a.form_setting,
            fill_out_auth=a.fill_out_auth,
            fill_in_range=a.fill_in_range,
            userids=a.userids,
            departmentids=a.departmentids,
            setting_manager_range=a.setting_manager_range,
            timed_repeat_info=a.timed_repeat_info,
            timed_repeat_info_enable=a.timed_repeat_info_enable,
            timed_repeat_info_remind_time=a.timed_repeat_info_remind_time,
            timed_repeat_info_repeat_type=a.timed_repeat_info_repeat_type,
            timed_repeat_info_week_flag=a.timed_repeat_info_week_flag,
            timed_repeat_info_skip_holiday=a.timed_repeat_info_skip_holiday,
            timed_repeat_info_day_of_month=a.timed_repeat_info_day_of_month,
            timed_repeat_info_fork_finish_type=a.timed_repeat_info_fork_finish_type,
            allow_multi_fill=a.allow_multi_fill,
            timed_finish=a.timed_finish,
            can_anonymous=a.can_anonymous,
            can_notify_submit=a.can_notify_submit,
        )
    table[('wedoc', 'modify-form')] = _handle_wedoc_modify_form

    wedoc_smartsheet_add_field_group_parser = wedoc_sub.add_parser(
        'smartsheet-add-field-group',
        help='添加编组',
    )
    wedoc_smartsheet_add_field_group_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_add_field_group_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_add_field_group_parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='编组名称，不能和已有名称重复',
    )
    wedoc_smartsheet_add_field_group_parser.add_argument(
        '--children',
        type=str,
        help='编组内容',
    )
    wedoc_smartsheet_add_field_group_parser.add_argument(
        '--children-field-id',
        type=str,
        help='字段id',
    )

    def _handle_wedoc_smartsheet_add_field_group(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_add_field_group(
            docid=a.docid,
            sheet_id=a.sheet_id,
            name=a.name,
            children=a.children,
            children_field_id=a.children_field_id,
        )
    table[('wedoc', 'smartsheet-add-field-group')] = _handle_wedoc_smartsheet_add_field_group

    wedoc_smartsheet_add_fields_parser = wedoc_sub.add_parser(
        'smartsheet-add-fields',
        help='添加字段',
    )
    wedoc_smartsheet_add_fields_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_add_fields_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_add_fields_parser.add_argument(
        '--fields',
        type=str,
        required=True,
        help='字段详情',
    )

    def _handle_wedoc_smartsheet_add_fields(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_add_fields(
            docid=a.docid,
            sheet_id=a.sheet_id,
            fields=a.fields,
        )
    table[('wedoc', 'smartsheet-add-fields')] = _handle_wedoc_smartsheet_add_fields

    wedoc_smartsheet_add_records_parser = wedoc_sub.add_parser(
        'smartsheet-add-records',
        help='添加记录',
    )
    wedoc_smartsheet_add_records_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_add_records_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_add_records_parser.add_argument(
        '--key-type',
        type=str,
        help='返回记录中单元格的key类型，默认用标题',
    )
    wedoc_smartsheet_add_records_parser.add_argument(
        '--records',
        type=str,
        required=True,
        help='需要添加的记录的具体内容组成的 JSON 数组',
    )

    def _handle_wedoc_smartsheet_add_records(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_add_records(
            docid=a.docid,
            sheet_id=a.sheet_id,
            key_type=a.key_type,
            records=a.records,
        )
    table[('wedoc', 'smartsheet-add-records')] = _handle_wedoc_smartsheet_add_records

    wedoc_smartsheet_add_sheet_parser = wedoc_sub.add_parser(
        'smartsheet-add-sheet',
        help='添加子表',
    )
    wedoc_smartsheet_add_sheet_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_add_sheet_parser.add_argument(
        '--properties',
        type=str,
        help='智能表属性',
    )
    wedoc_smartsheet_add_sheet_parser.add_argument(
        '--properties-title',
        type=str,
        help='智能表标题',
    )
    wedoc_smartsheet_add_sheet_parser.add_argument(
        '--properties-index',
        type=str,
        help='智能表下标',
    )

    def _handle_wedoc_smartsheet_add_sheet(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_add_sheet(
            docid=a.docid,
            properties=a.properties,
            properties_title=a.properties_title,
            properties_index=a.properties_index,
        )
    table[('wedoc', 'smartsheet-add-sheet')] = _handle_wedoc_smartsheet_add_sheet

    wedoc_smartsheet_add_view_parser = wedoc_sub.add_parser(
        'smartsheet-add-view',
        help='添加视图',
    )
    wedoc_smartsheet_add_view_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_add_view_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_add_view_parser.add_argument(
        '--view-title',
        type=str,
        required=True,
        help='视图标题',
    )
    wedoc_smartsheet_add_view_parser.add_argument(
        '--view-type',
        type=str,
        required=True,
        help='视图类型。见ViewType',
    )
    wedoc_smartsheet_add_view_parser.add_argument(
        '--property-gantt',
        type=str,
        help='甘特视图属性,添加甘特图时必填',
    )
    wedoc_smartsheet_add_view_parser.add_argument(
        '--property-calendar',
        type=str,
        help='日历视图属性，添加日历视图时必填',
    )

    def _handle_wedoc_smartsheet_add_view(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_add_view(
            docid=a.docid,
            sheet_id=a.sheet_id,
            view_title=a.view_title,
            view_type=a.view_type,
            property_gantt=a.property_gantt,
            property_calendar=a.property_calendar,
        )
    table[('wedoc', 'smartsheet-add-view')] = _handle_wedoc_smartsheet_add_view

    wedoc_smartsheet_content_priv_get_sheet_priv_parser = wedoc_sub.add_parser(
        'smartsheet-content-priv-get-sheet-priv',
        help='管理智能表格内容权限',
    )
    wedoc_smartsheet_content_priv_get_sheet_priv_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='智能表ID，通过新建文档接口创建后获得',
    )
    wedoc_smartsheet_content_priv_get_sheet_priv_parser.add_argument(
        '--type',
        type=str,
        required=True,
        help='权限规则类型，1-全员权限，2-额外权限',
    )
    wedoc_smartsheet_content_priv_get_sheet_priv_parser.add_argument(
        '--rule-id-list',
        type=str,
        help='需要查询的规则id列表，查询额外权限时填写',
    )

    def _handle_wedoc_smartsheet_content_priv_get_sheet_priv(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_content_priv_get_sheet_priv(
            docid=a.docid,
            type=a.type,
            rule_id_list=a.rule_id_list,
        )
    table[('wedoc', 'smartsheet-content-priv-get-sheet-priv')] = _handle_wedoc_smartsheet_content_priv_get_sheet_priv

    wedoc_smartsheet_delete_field_groups_parser = wedoc_sub.add_parser(
        'smartsheet-delete-field-groups',
        help='删除编组',
    )
    wedoc_smartsheet_delete_field_groups_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_delete_field_groups_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='子表ID',
    )
    wedoc_smartsheet_delete_field_groups_parser.add_argument(
        '--field-group-ids',
        type=str,
        required=True,
        help='要删除的编组 ID',
    )

    def _handle_wedoc_smartsheet_delete_field_groups(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_delete_field_groups(
            docid=a.docid,
            sheet_id=a.sheet_id,
            field_group_ids=a.field_group_ids,
        )
    table[('wedoc', 'smartsheet-delete-field-groups')] = _handle_wedoc_smartsheet_delete_field_groups

    wedoc_smartsheet_delete_fields_parser = wedoc_sub.add_parser(
        'smartsheet-delete-fields',
        help='删除字段',
    )
    wedoc_smartsheet_delete_fields_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_delete_fields_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_delete_fields_parser.add_argument(
        '--field-ids',
        type=str,
        required=True,
        help='需要删除的字段id列表',
    )

    def _handle_wedoc_smartsheet_delete_fields(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_delete_fields(
            docid=a.docid,
            sheet_id=a.sheet_id,
            field_ids=a.field_ids,
        )
    table[('wedoc', 'smartsheet-delete-fields')] = _handle_wedoc_smartsheet_delete_fields

    wedoc_smartsheet_delete_records_parser = wedoc_sub.add_parser(
        'smartsheet-delete-records',
        help='删除记录',
    )
    wedoc_smartsheet_delete_records_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_delete_records_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_delete_records_parser.add_argument(
        '--record-ids',
        type=str,
        required=True,
        help='要删除的记录 ID',
    )

    def _handle_wedoc_smartsheet_delete_records(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_delete_records(
            docid=a.docid,
            sheet_id=a.sheet_id,
            record_ids=a.record_ids,
        )
    table[('wedoc', 'smartsheet-delete-records')] = _handle_wedoc_smartsheet_delete_records

    wedoc_smartsheet_delete_sheet_parser = wedoc_sub.add_parser(
        'smartsheet-delete-sheet',
        help='删除子表',
    )
    wedoc_smartsheet_delete_sheet_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_delete_sheet_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='删除的Smartsheet 子表 ID',
    )

    def _handle_wedoc_smartsheet_delete_sheet(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_delete_sheet(
            docid=a.docid,
            sheet_id=a.sheet_id,
        )
    table[('wedoc', 'smartsheet-delete-sheet')] = _handle_wedoc_smartsheet_delete_sheet

    wedoc_smartsheet_delete_views_parser = wedoc_sub.add_parser(
        'smartsheet-delete-views',
        help='删除视图',
    )
    wedoc_smartsheet_delete_views_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_delete_views_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_delete_views_parser.add_argument(
        '--view-ids',
        type=str,
        required=True,
        help='要删除的视图ID列表',
    )

    def _handle_wedoc_smartsheet_delete_views(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_delete_views(
            docid=a.docid,
            sheet_id=a.sheet_id,
            view_ids=a.view_ids,
        )
    table[('wedoc', 'smartsheet-delete-views')] = _handle_wedoc_smartsheet_delete_views

    wedoc_smartsheet_get_field_groups_parser = wedoc_sub.add_parser(
        'smartsheet-get-field-groups',
        help='获取编组',
    )
    wedoc_smartsheet_get_field_groups_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_get_field_groups_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_get_field_groups_parser.add_argument(
        '--offset',
        type=str,
        help='偏移量，初始值为 0',
    )
    wedoc_smartsheet_get_field_groups_parser.add_argument(
        '--limit',
        type=str,
        help='分页大小 , 每页返回多少条数据',
    )

    def _handle_wedoc_smartsheet_get_field_groups(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_get_field_groups(
            docid=a.docid,
            sheet_id=a.sheet_id,
            offset=a.offset,
            limit=a.limit,
        )
    table[('wedoc', 'smartsheet-get-field-groups')] = _handle_wedoc_smartsheet_get_field_groups

    wedoc_smartsheet_get_fields_parser = wedoc_sub.add_parser(
        'smartsheet-get-fields',
        help='查询字段',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--view-id',
        type=str,
        help='视图 ID',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--field-ids',
        type=str,
        help='由字段 ID 组成的 JSON 数组',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--field-titles',
        type=str,
        help='由字段标题组成的 JSON 数组',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--offset',
        type=int,
        help='偏移量，初始值为 0',
    )
    wedoc_smartsheet_get_fields_parser.add_argument(
        '--limit',
        type=int,
        help='分页大小 , 每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，如果总数大于 1000，一次性返回 1000 个字段，当总数小于 1000 时，返回全部字段；limit 最大值为 1000',
    )

    def _handle_wedoc_smartsheet_get_fields(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_get_fields(
            docid=a.docid,
            sheet_id=a.sheet_id,
            view_id=a.view_id,
            field_ids=a.field_ids,
            field_titles=a.field_titles,
            offset=a.offset,
            limit=a.limit,
        )
    table[('wedoc', 'smartsheet-get-fields')] = _handle_wedoc_smartsheet_get_fields

    wedoc_smartsheet_get_records_parser = wedoc_sub.add_parser(
        'smartsheet-get-records',
        help='查询记录',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--view-id',
        type=str,
        help='视图 ID',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--record-ids',
        type=str,
        help='由记录 ID 组成的 JSON 数组',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--key-type',
        type=str,
        help='返回记录中单元格的key类型',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--field-titles',
        type=str,
        help='返回指定列，由字段标题组成的 JSON 数组 ，key_type 为 CELL_VALUE_KEY_TYPE_FIELD_TITLE 时有效',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--field-ids',
        type=str,
        help='返回指定列，由字段 ID 组成的 JSON 数组 ，key_type 为 CELL_VALUE_KEY_TYPE_FIELD_ID 时有效',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--sort',
        type=str,
        help='对返回记录进行排序',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--offset',
        type=str,
        help='偏移量，初始值为 0',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--limit',
        type=str,
        help='分页大小 , 每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，如果总数大于 1000，一次性返回 1000 行记录，当总数小于 1000 时，返回全部记录；limit 最大值为 1000',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--ver',
        type=str,
        help='版本号',
    )
    wedoc_smartsheet_get_records_parser.add_argument(
        '--filter-spec',
        type=str,
        help='过滤设置，不支持和sort一起使用',
    )

    def _handle_wedoc_smartsheet_get_records(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_get_records(
            docid=a.docid,
            sheet_id=a.sheet_id,
            view_id=a.view_id,
            record_ids=a.record_ids,
            key_type=a.key_type,
            field_titles=a.field_titles,
            field_ids=a.field_ids,
            sort=a.sort,
            offset=a.offset,
            limit=a.limit,
            ver=a.ver,
            filter_spec=a.filter_spec,
        )
    table[('wedoc', 'smartsheet-get-records')] = _handle_wedoc_smartsheet_get_records

    wedoc_smartsheet_get_sheet_parser = wedoc_sub.add_parser(
        'smartsheet-get-sheet',
        help='查询子表',
    )
    wedoc_smartsheet_get_sheet_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_get_sheet_parser.add_argument(
        '--sheet-id',
        type=str,
        help='指定子表ID查询',
    )
    wedoc_smartsheet_get_sheet_parser.add_argument(
        '--need-all-type-sheet',
        help='获取所有类型子表。为true时可获取包含仪表盘和说明页在内的所有类型的子表',
    )

    def _handle_wedoc_smartsheet_get_sheet(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_get_sheet(
            docid=a.docid,
            sheet_id=a.sheet_id,
            need_all_type_sheet=a.need_all_type_sheet,
        )
    table[('wedoc', 'smartsheet-get-sheet')] = _handle_wedoc_smartsheet_get_sheet

    wedoc_smartsheet_get_views_parser = wedoc_sub.add_parser(
        'smartsheet-get-views',
        help='查询视图',
    )
    wedoc_smartsheet_get_views_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_get_views_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_get_views_parser.add_argument(
        '--view-ids',
        type=str,
        help='需要查询的视图 ID 数组',
    )
    wedoc_smartsheet_get_views_parser.add_argument(
        '--offset',
        type=str,
        help='偏移量，初始值为 0',
    )
    wedoc_smartsheet_get_views_parser.add_argument(
        '--limit',
        type=str,
        help='分页大小 , 每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，如果总数大于 1000，一次性返回 1000 个视图，当总数小于 1000 时，返回全部视图；limit 最大值为 1000',
    )

    def _handle_wedoc_smartsheet_get_views(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_get_views(
            docid=a.docid,
            sheet_id=a.sheet_id,
            view_ids=a.view_ids,
            offset=a.offset,
            limit=a.limit,
        )
    table[('wedoc', 'smartsheet-get-views')] = _handle_wedoc_smartsheet_get_views

    wedoc_smartsheet_update_field_group_parser = wedoc_sub.add_parser(
        'smartsheet-update-field-group',
        help='更新编组',
    )
    wedoc_smartsheet_update_field_group_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_update_field_group_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_update_field_group_parser.add_argument(
        '--field-group-id',
        type=str,
        required=True,
        help='编组id',
    )
    wedoc_smartsheet_update_field_group_parser.add_argument(
        '--name',
        type=str,
        help='编组名称，不能和已有名称重复',
    )
    wedoc_smartsheet_update_field_group_parser.add_argument(
        '--children',
        type=str,
        help='编组内容',
    )
    wedoc_smartsheet_update_field_group_parser.add_argument(
        '--children-field-id',
        type=str,
        help='字段id',
    )

    def _handle_wedoc_smartsheet_update_field_group(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_update_field_group(
            docid=a.docid,
            sheet_id=a.sheet_id,
            field_group_id=a.field_group_id,
            name=a.name,
            children=a.children,
            children_field_id=a.children_field_id,
        )
    table[('wedoc', 'smartsheet-update-field-group')] = _handle_wedoc_smartsheet_update_field_group

    wedoc_smartsheet_update_fields_parser = wedoc_sub.add_parser(
        'smartsheet-update-fields',
        help='更新字段',
    )
    wedoc_smartsheet_update_fields_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_update_fields_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='表格ID',
    )
    wedoc_smartsheet_update_fields_parser.add_argument(
        '--fields',
        type=str,
        required=True,
        help='字段详情',
    )

    def _handle_wedoc_smartsheet_update_fields(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_update_fields(
            docid=a.docid,
            sheet_id=a.sheet_id,
            fields=a.fields,
        )
    table[('wedoc', 'smartsheet-update-fields')] = _handle_wedoc_smartsheet_update_fields

    wedoc_smartsheet_update_records_parser = wedoc_sub.add_parser(
        'smartsheet-update-records',
        help='更新记录',
    )
    wedoc_smartsheet_update_records_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_update_records_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_update_records_parser.add_argument(
        '--key-type',
        type=str,
        help='返回记录中单元格的key类型',
    )
    wedoc_smartsheet_update_records_parser.add_argument(
        '--records',
        type=str,
        required=True,
        help='由需要更新的记录组成的 JSON 数组',
    )

    def _handle_wedoc_smartsheet_update_records(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_update_records(
            docid=a.docid,
            sheet_id=a.sheet_id,
            key_type=a.key_type,
            records=a.records,
        )
    table[('wedoc', 'smartsheet-update-records')] = _handle_wedoc_smartsheet_update_records

    wedoc_smartsheet_update_sheet_parser = wedoc_sub.add_parser(
        'smartsheet-update-sheet',
        help='更新子表',
    )
    wedoc_smartsheet_update_sheet_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_update_sheet_parser.add_argument(
        '--properties-sheet-id',
        type=str,
        required=True,
        help='子表 ID',
    )
    wedoc_smartsheet_update_sheet_parser.add_argument(
        '--properties-title',
        type=str,
        help='子表标题',
    )

    def _handle_wedoc_smartsheet_update_sheet(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_update_sheet(
            docid=a.docid,
            properties_sheet_id=a.properties_sheet_id,
            properties_title=a.properties_title,
        )
    table[('wedoc', 'smartsheet-update-sheet')] = _handle_wedoc_smartsheet_update_sheet

    wedoc_smartsheet_update_view_parser = wedoc_sub.add_parser(
        'smartsheet-update-view',
        help='更新视图',
    )
    wedoc_smartsheet_update_view_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_smartsheet_update_view_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='Smartsheet 子表ID',
    )
    wedoc_smartsheet_update_view_parser.add_argument(
        '--view-id',
        type=str,
        required=True,
        help='视图ID',
    )
    wedoc_smartsheet_update_view_parser.add_argument(
        '--view-title',
        type=str,
        help='视图标题',
    )
    wedoc_smartsheet_update_view_parser.add_argument(
        '--property',
        type=str,
        help='视图的排序/过滤/分组/填色配置，详见ViewProperty',
    )

    def _handle_wedoc_smartsheet_update_view(a: argparse.Namespace) -> dict:
        return client.wedoc_smartsheet_update_view(
            docid=a.docid,
            sheet_id=a.sheet_id,
            view_id=a.view_id,
            view_title=a.view_title,
            property=a.property,
        )
    table[('wedoc', 'smartsheet-update-view')] = _handle_wedoc_smartsheet_update_view

    wedoc_spreadsheet_batch_update_parser = wedoc_sub.add_parser(
        'spreadsheet-batch-update',
        help='编辑表格内容',
    )
    wedoc_spreadsheet_batch_update_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='文档的docid',
    )
    wedoc_spreadsheet_batch_update_parser.add_argument(
        '--requests',
        type=str,
        required=True,
        help='更新操作列表，详见 UpdateRequest',
    )

    def _handle_wedoc_spreadsheet_batch_update(a: argparse.Namespace) -> dict:
        return client.wedoc_spreadsheet_batch_update(
            docid=a.docid,
            requests=a.requests,
        )
    table[('wedoc', 'spreadsheet-batch-update')] = _handle_wedoc_spreadsheet_batch_update

    wedoc_spreadsheet_get_sheet_properties_parser = wedoc_sub.add_parser(
        'spreadsheet-get-sheet-properties',
        help='获取表格行列信息',
    )
    wedoc_spreadsheet_get_sheet_properties_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='在线表格的docid',
    )

    def _handle_wedoc_spreadsheet_get_sheet_properties(a: argparse.Namespace) -> dict:
        return client.wedoc_spreadsheet_get_sheet_properties(
            docid=a.docid,
        )
    table[('wedoc', 'spreadsheet-get-sheet-properties')] = _handle_wedoc_spreadsheet_get_sheet_properties

    wedoc_spreadsheet_get_sheet_range_data_parser = wedoc_sub.add_parser(
        'spreadsheet-get-sheet-range-data',
        help='获取表格数据',
    )
    wedoc_spreadsheet_get_sheet_range_data_parser.add_argument(
        '--docid',
        type=str,
        required=True,
        help='在线表格唯一标识',
    )
    wedoc_spreadsheet_get_sheet_range_data_parser.add_argument(
        '--sheet-id',
        type=str,
        required=True,
        help='工作表ID，工作表的唯一标识',
    )
    wedoc_spreadsheet_get_sheet_range_data_parser.add_argument(
        '--range',
        type=str,
        required=True,
        help='查询的范围，格式遵循 A1表示法',
    )

    def _handle_wedoc_spreadsheet_get_sheet_range_data(a: argparse.Namespace) -> dict:
        return client.wedoc_spreadsheet_get_sheet_range_data(
            docid=a.docid,
            sheet_id=a.sheet_id,
            range=a.range,
        )
    table[('wedoc', 'spreadsheet-get-sheet-range-data')] = _handle_wedoc_spreadsheet_get_sheet_range_data

    wedoc_vip_batch_add_parser = wedoc_sub.add_parser(
        'vip-batch-add',
        help='分配高级功能账号',
    )
    wedoc_vip_batch_add_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要分配高级功能的企业成员userid列表，单次操作最大限制100个',
    )

    def _handle_wedoc_vip_batch_add(a: argparse.Namespace) -> dict:
        return client.wedoc_vip_batch_add(
            userid_list=a.userid_list,
        )
    table[('wedoc', 'vip-batch-add')] = _handle_wedoc_vip_batch_add

    wedoc_vip_batch_del_parser = wedoc_sub.add_parser(
        'vip-batch-del',
        help='取消高级功能账号',
    )
    wedoc_vip_batch_del_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要撤销分配高级功能的企业成员userid列表，单次操作最多限制100个',
    )

    def _handle_wedoc_vip_batch_del(a: argparse.Namespace) -> dict:
        return client.wedoc_vip_batch_del(
            userid_list=a.userid_list,
        )
    table[('wedoc', 'vip-batch-del')] = _handle_wedoc_vip_batch_del

    wedoc_vip_list_parser = wedoc_sub.add_parser(
        'vip-list',
        help='获取高级功能账号列表',
    )
    wedoc_vip_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    wedoc_vip_list_parser.add_argument(
        '--limit',
        type=int,
        help='用于分页查询，每次请求返回的数据上限。默认100，最大200 注意：不保证每次返回的数据刚好为指定limit，必须用返回的has_more判断是否继续请求',
    )

    def _handle_wedoc_vip_list(a: argparse.Namespace) -> dict:
        return client.wedoc_vip_list(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('wedoc', 'vip-list')] = _handle_wedoc_vip_list

    wedrive_parser = subparsers.add_parser(
        'wedrive',
        help='wedrive',
    )
    wedrive_sub = wedrive_parser.add_subparsers(dest='__action', required=True)

    wedrive_file_acl_del_parser = wedrive_sub.add_parser(
        'file-acl-del',
        help='删除成员',
    )
    wedrive_file_acl_del_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )
    wedrive_file_acl_del_parser.add_argument(
        '--auth-info',
        type=str,
        required=True,
        help='被移除的成员信息',
    )
    wedrive_file_acl_del_parser.add_argument(
        '--type-后续将废弃',
        type=str,
        required=True,
        help='成员类型 1:个人 2:部门',
    )
    wedrive_file_acl_del_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员userid,字符串',
    )
    wedrive_file_acl_del_parser.add_argument(
        '--departmentid-后续将废弃',
        type=str,
        required=True,
        help='部门departmentid, 32位整型范围是[0, 2^32) (type为2时填写)',
    )

    def _handle_wedrive_file_acl_del(a: argparse.Namespace) -> dict:
        return client.wedrive_file_acl_del(
            fileid=a.fileid,
            auth_info=a.auth_info,
            type_后续将废弃=a.type_后续将废弃,
            userid=a.userid,
            departmentid_后续将废弃=a.departmentid_后续将废弃,
        )
    table[('wedrive', 'file-acl-del')] = _handle_wedrive_file_acl_del

    wedrive_file_create_parser = wedrive_sub.add_parser(
        'file-create',
        help='新建文件夹/文档',
    )
    wedrive_file_create_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )
    wedrive_file_create_parser.add_argument(
        '--fatherid',
        type=str,
        required=True,
        help='父目录fileid, 在根目录时为空间spaceid',
    )
    wedrive_file_create_parser.add_argument(
        '--file-type',
        type=str,
        required=True,
        help='文件类型, 1:文件夹 3:文档(文档) 4:文档(表格)',
    )
    wedrive_file_create_parser.add_argument(
        '--file-name',
        type=str,
        required=True,
        help='文件名字（注意：文件名最多填255个字符, 英文算1个, 汉字算2个）',
    )

    def _handle_wedrive_file_create(a: argparse.Namespace) -> dict:
        return client.wedrive_file_create(
            spaceid=a.spaceid,
            fatherid=a.fatherid,
            file_type=a.file_type,
            file_name=a.file_name,
        )
    table[('wedrive', 'file-create')] = _handle_wedrive_file_create

    wedrive_file_delete_parser = wedrive_sub.add_parser(
        'file-delete',
        help='删除文件',
    )
    wedrive_file_delete_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )

    def _handle_wedrive_file_delete(a: argparse.Namespace) -> dict:
        return client.wedrive_file_delete(
            fileid=a.fileid,
        )
    table[('wedrive', 'file-delete')] = _handle_wedrive_file_delete

    wedrive_file_download_parser = wedrive_sub.add_parser(
        'file-download',
        help='下载文件',
    )
    wedrive_file_download_parser.add_argument(
        '--fileid',
        type=str,
        help='文件fileid（只支持下载普通文件，不支持下载文件夹或微文档）',
    )
    wedrive_file_download_parser.add_argument(
        '--selected-ticket',
        type=str,
        help='微盘和文件选择器jsapi返回的selectedTicket。若填此参数，则不需要填fileid。',
    )

    def _handle_wedrive_file_download(a: argparse.Namespace) -> dict:
        return client.wedrive_file_download(
            fileid=a.fileid,
            selected_ticket=a.selected_ticket,
        )
    table[('wedrive', 'file-download')] = _handle_wedrive_file_download

    wedrive_file_info_parser = wedrive_sub.add_parser(
        'file-info',
        help='获取文件信息',
    )
    wedrive_file_info_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )

    def _handle_wedrive_file_info(a: argparse.Namespace) -> dict:
        return client.wedrive_file_info(
            fileid=a.fileid,
        )
    table[('wedrive', 'file-info')] = _handle_wedrive_file_info

    wedrive_file_move_parser = wedrive_sub.add_parser(
        'file-move',
        help='移动文件',
    )
    wedrive_file_move_parser.add_argument(
        '--fatherid',
        type=str,
        required=True,
        help='当前目录的fileid,根目录时为空间spaceid',
    )
    wedrive_file_move_parser.add_argument(
        '--replace',
        help='如果移动到的目标目录与需要移动的文件重名时，是否覆盖。true:重名文件覆盖 false:重名文件进行冲突重命名处理（移动后文件名格式如xxx(1).txt xxx(1).doc等）',
    )
    wedrive_file_move_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )

    def _handle_wedrive_file_move(a: argparse.Namespace) -> dict:
        return client.wedrive_file_move(
            fatherid=a.fatherid,
            replace=a.replace,
            fileid=a.fileid,
        )
    table[('wedrive', 'file-move')] = _handle_wedrive_file_move

    wedrive_file_rename_parser = wedrive_sub.add_parser(
        'file-rename',
        help='重命名文件',
    )
    wedrive_file_rename_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )
    wedrive_file_rename_parser.add_argument(
        '--new-name',
        type=str,
        required=True,
        help='重命名后的文件名 （注意：文件名最多填255个字符, 英文算1个, 汉字算2个）',
    )

    def _handle_wedrive_file_rename(a: argparse.Namespace) -> dict:
        return client.wedrive_file_rename(
            fileid=a.fileid,
            new_name=a.new_name,
        )
    table[('wedrive', 'file-rename')] = _handle_wedrive_file_rename

    wedrive_file_secure_setting_parser = wedrive_sub.add_parser(
        'file-secure-setting',
        help='修改文件安全设置',
    )
    wedrive_file_secure_setting_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )
    wedrive_file_secure_setting_parser.add_argument(
        '--text',
        type=str,
        help='水印文字，此字段不填则保持原样',
    )
    wedrive_file_secure_setting_parser.add_argument(
        '--margin-type',
        type=str,
        help='水印类型。1：低密度水印， 2： 高密度水印，此字段不填则保持原样',
    )
    wedrive_file_secure_setting_parser.add_argument(
        '--show-visitor-name',
        help='是否显示访问人名称，此字段不填则保持原样',
    )
    wedrive_file_secure_setting_parser.add_argument(
        '--show-text',
        help='是否展示水印文本，此字段不填则保持原样',
    )

    def _handle_wedrive_file_secure_setting(a: argparse.Namespace) -> dict:
        return client.wedrive_file_secure_setting(
            fileid=a.fileid,
            text=a.text,
            margin_type=a.margin_type,
            show_visitor_name=a.show_visitor_name,
            show_text=a.show_text,
        )
    table[('wedrive', 'file-secure-setting')] = _handle_wedrive_file_secure_setting

    wedrive_file_setting_parser = wedrive_sub.add_parser(
        'file-setting',
        help='分享设置',
    )
    wedrive_file_setting_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )
    wedrive_file_setting_parser.add_argument(
        '--auth-scope',
        type=str,
        required=True,
        help='权限范围：1:指定人 2:企业内 3:企业外 4: 企业内需管理员审批（仅有管理员时可设置） 5: 企业外需管理员审批（仅有管理员时可设置）',
    )
    wedrive_file_setting_parser.add_argument(
        '--auth',
        type=str,
        help='权限信息 普通文档： 1:仅浏览（可下载) 4:仅预览（仅专业版企业可设置）；如果不填充此字段为保持原有状态 微文档： 1:仅浏览（可下载）；如果不填充此字段为保持原有状态',
    )

    def _handle_wedrive_file_setting(a: argparse.Namespace) -> dict:
        return client.wedrive_file_setting(
            fileid=a.fileid,
            auth_scope=a.auth_scope,
            auth=a.auth,
        )
    table[('wedrive', 'file-setting')] = _handle_wedrive_file_setting

    wedrive_file_share_parser = wedrive_sub.add_parser(
        'file-share',
        help='获取分享链接',
    )
    wedrive_file_share_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )

    def _handle_wedrive_file_share(a: argparse.Namespace) -> dict:
        return client.wedrive_file_share(
            fileid=a.fileid,
        )
    table[('wedrive', 'file-share')] = _handle_wedrive_file_share

    wedrive_file_upload_parser = wedrive_sub.add_parser(
        'file-upload',
        help='上传文件',
    )
    wedrive_file_upload_parser.add_argument(
        '--spaceid',
        type=str,
        help='空间spaceid',
    )
    wedrive_file_upload_parser.add_argument(
        '--fatherid',
        type=str,
        help='父目录fileid, 在根目录时为空间spaceid',
    )
    wedrive_file_upload_parser.add_argument(
        '--selected-ticket',
        type=str,
        help='微盘和文件选择器jsapi返回的selectedTicket。若填此参数，则不需要填spaceid/fatherid。',
    )
    wedrive_file_upload_parser.add_argument(
        '--file-name',
        type=str,
        required=True,
        help='文件名字（注意：文件名最多填255个字符, 英文算1个, 汉字算2个）',
    )
    wedrive_file_upload_parser.add_argument(
        '--file-base64-content',
        type=str,
        required=True,
        help='文件内容base64（注意：只需要填入文件内容的Base64，不需要添加任何如："data:application/x-javascript;base64" 的数据类型描述信息），文件大小上限为10M。大于10M文件，可使用文件分块上传接口',
    )

    def _handle_wedrive_file_upload(a: argparse.Namespace) -> dict:
        return client.wedrive_file_upload(
            spaceid=a.spaceid,
            fatherid=a.fatherid,
            selected_ticket=a.selected_ticket,
            file_name=a.file_name,
            file_base64_content=a.file_base64_content,
        )
    table[('wedrive', 'file-upload')] = _handle_wedrive_file_upload

    wedrive_file_upload_init_parser = wedrive_sub.add_parser(
        'file-upload-init',
        help='文件分块上传',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--spaceid',
        type=str,
        help='空间spaceid',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--fatherid',
        type=str,
        help='当前目录的fileid，根目录时为空间spaceid',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--selected-ticket',
        type=str,
        help='微盘和文件选择器jsapi返回的selectedTicket。若填此参数，则不需要填spaceid/fatherid。',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--file-name',
        type=str,
        required=True,
        help='文件名字',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--size',
        type=str,
        required=True,
        help='文件大小。最大支持20G',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--block-sha',
        type=str,
        required=True,
        help='文件分块累积sha值，按分块顺序填入数组。参考附录-分块累积sha说明',
    )
    wedrive_file_upload_init_parser.add_argument(
        '--skip-push-card',
        help='文件创建完成时是否推送企业微信卡片。默认false，即默认推送卡片',
    )

    def _handle_wedrive_file_upload_init(a: argparse.Namespace) -> dict:
        return client.wedrive_file_upload_init(
            spaceid=a.spaceid,
            fatherid=a.fatherid,
            selected_ticket=a.selected_ticket,
            file_name=a.file_name,
            size=a.size,
            block_sha=a.block_sha,
            skip_push_card=a.skip_push_card,
        )
    table[('wedrive', 'file-upload-init')] = _handle_wedrive_file_upload_init

    wedrive_get_file_permission_parser = wedrive_sub.add_parser(
        'get-file-permission',
        help='获取文件权限信息',
    )
    wedrive_get_file_permission_parser.add_argument(
        '--fileid',
        type=str,
        required=True,
        help='文件fileid',
    )

    def _handle_wedrive_get_file_permission(a: argparse.Namespace) -> dict:
        return client.wedrive_get_file_permission(
            fileid=a.fileid,
        )
    table[('wedrive', 'get-file-permission')] = _handle_wedrive_get_file_permission

    wedrive_sub.add_parser(
        'mng-pro-info',
        help='版本和容量管理',
    )

    def _handle_wedrive_mng_pro_info(a: argparse.Namespace) -> dict:
        return client.wedrive_mng_pro_info()
    table[('wedrive', 'mng-pro-info')] = _handle_wedrive_mng_pro_info

    wedrive_new_space_info_parser = wedrive_sub.add_parser(
        'new-space-info',
        help='获取空间信息',
    )
    wedrive_new_space_info_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )

    def _handle_wedrive_new_space_info(a: argparse.Namespace) -> dict:
        return client.wedrive_new_space_info(
            spaceid=a.spaceid,
        )
    table[('wedrive', 'new-space-info')] = _handle_wedrive_new_space_info

    wedrive_space_acl_del_parser = wedrive_sub.add_parser(
        'space-acl-del',
        help='移除成员/部门',
    )
    wedrive_space_acl_del_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )
    wedrive_space_acl_del_parser.add_argument(
        '--auth-info',
        type=str,
        required=True,
        help='被移除的空间成员信息',
    )
    wedrive_space_acl_del_parser.add_argument(
        '--type',
        type=str,
        required=True,
        help='成员类型 1:个人 2:部门',
    )
    wedrive_space_acl_del_parser.add_argument(
        '--userid',
        type=str,
        required=True,
        help='成员userid,字符串 (type为1时填写)',
    )
    wedrive_space_acl_del_parser.add_argument(
        '--departmentid',
        type=str,
        required=True,
        help='部门departmentid, 32位整型范围是[0, 2^32) (type为2时填写)',
    )

    def _handle_wedrive_space_acl_del(a: argparse.Namespace) -> dict:
        return client.wedrive_space_acl_del(
            spaceid=a.spaceid,
            auth_info=a.auth_info,
            type=a.type,
            userid=a.userid,
            departmentid=a.departmentid,
        )
    table[('wedrive', 'space-acl-del')] = _handle_wedrive_space_acl_del

    wedrive_space_dismiss_parser = wedrive_sub.add_parser(
        'space-dismiss',
        help='解散空间',
    )
    wedrive_space_dismiss_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )

    def _handle_wedrive_space_dismiss(a: argparse.Namespace) -> dict:
        return client.wedrive_space_dismiss(
            spaceid=a.spaceid,
        )
    table[('wedrive', 'space-dismiss')] = _handle_wedrive_space_dismiss

    wedrive_space_info_parser = wedrive_sub.add_parser(
        'space-info',
        help='获取空间信息',
    )
    wedrive_space_info_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )

    def _handle_wedrive_space_info(a: argparse.Namespace) -> dict:
        return client.wedrive_space_info(
            spaceid=a.spaceid,
        )
    table[('wedrive', 'space-info')] = _handle_wedrive_space_info

    wedrive_space_rename_parser = wedrive_sub.add_parser(
        'space-rename',
        help='重命名空间',
    )
    wedrive_space_rename_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )
    wedrive_space_rename_parser.add_argument(
        '--space-name',
        type=str,
        required=True,
        help='重命名后的空间名',
    )

    def _handle_wedrive_space_rename(a: argparse.Namespace) -> dict:
        return client.wedrive_space_rename(
            spaceid=a.spaceid,
            space_name=a.space_name,
        )
    table[('wedrive', 'space-rename')] = _handle_wedrive_space_rename

    wedrive_space_setting_parser = wedrive_sub.add_parser(
        'space-setting',
        help='安全设置',
    )
    wedrive_space_setting_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )
    wedrive_space_setting_parser.add_argument(
        '--enable-watermark',
        help='（本字段仅专业版企业可设置）启用水印。false:关 true:开 ;如果不填充此字段为保持原有状态',
    )
    wedrive_space_setting_parser.add_argument(
        '--enable-confidential-mode',
        help='是否开启保密模式。false:关 true:开 如果不填充此字段为保持原有状态',
    )
    wedrive_space_setting_parser.add_argument(
        '--share-url-no-approve',
        help='通过链接加入空间无需审批。false:关； true:开； 如果不填充此字段为保持原有状态',
    )
    wedrive_space_setting_parser.add_argument(
        '--share-url-no-approve-default-auth',
        type=str,
        help='邀请链接默认权限。1:仅下载 2:可编辑 4:仅预览 5:可上传下载 200:自定义权限；如果不填充此字段为保持原有状态',
    )
    wedrive_space_setting_parser.add_argument(
        '--default-file-scope',
        type=str,
        help='文件默认可查看范围。1:仅成员；2:企业内。如果不填充此字段为保持原有状态',
    )
    wedrive_space_setting_parser.add_argument(
        '--ban-share-external',
        help='是否禁止文件分享到企业外｜false:关 true:开 如果不填充此字段为保持原有状态',
    )

    def _handle_wedrive_space_setting(a: argparse.Namespace) -> dict:
        return client.wedrive_space_setting(
            spaceid=a.spaceid,
            enable_watermark=a.enable_watermark,
            enable_confidential_mode=a.enable_confidential_mode,
            share_url_no_approve=a.share_url_no_approve,
            share_url_no_approve_default_auth=a.share_url_no_approve_default_auth,
            default_file_scope=a.default_file_scope,
            ban_share_external=a.ban_share_external,
        )
    table[('wedrive', 'space-setting')] = _handle_wedrive_space_setting

    wedrive_space_share_parser = wedrive_sub.add_parser(
        'space-share',
        help='获取邀请链接',
    )
    wedrive_space_share_parser.add_argument(
        '--spaceid',
        type=str,
        required=True,
        help='空间spaceid',
    )

    def _handle_wedrive_space_share(a: argparse.Namespace) -> dict:
        return client.wedrive_space_share(
            spaceid=a.spaceid,
        )
    table[('wedrive', 'space-share')] = _handle_wedrive_space_share

    wedrive_vip_batch_add_parser = wedrive_sub.add_parser(
        'vip-batch-add',
        help='分配高级功能账号',
    )
    wedrive_vip_batch_add_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要分配高级功能的企业成员userid列表，单次操作最大限制100个',
    )

    def _handle_wedrive_vip_batch_add(a: argparse.Namespace) -> dict:
        return client.wedrive_vip_batch_add(
            userid_list=a.userid_list,
        )
    table[('wedrive', 'vip-batch-add')] = _handle_wedrive_vip_batch_add

    wedrive_vip_batch_del_parser = wedrive_sub.add_parser(
        'vip-batch-del',
        help='取消高级功能账号',
    )
    wedrive_vip_batch_del_parser.add_argument(
        '--userid-list',
        type=str,
        required=True,
        help='要撤销分配高级功能的企业成员userid列表，单次操作最多限制100个',
    )

    def _handle_wedrive_vip_batch_del(a: argparse.Namespace) -> dict:
        return client.wedrive_vip_batch_del(
            userid_list=a.userid_list,
        )
    table[('wedrive', 'vip-batch-del')] = _handle_wedrive_vip_batch_del

    wedrive_vip_list_parser = wedrive_sub.add_parser(
        'vip-list',
        help='获取高级功能账号列表',
    )
    wedrive_vip_list_parser.add_argument(
        '--cursor',
        type=str,
        help='用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填',
    )
    wedrive_vip_list_parser.add_argument(
        '--limit',
        type=int,
        help='用于分页查询，每次请求返回的数据上限。默认100，最大200 注意：不保证每次返回的数据刚好为指定limit，必须用返回的has_more判断是否继续请求',
    )

    def _handle_wedrive_vip_list(a: argparse.Namespace) -> dict:
        return client.wedrive_vip_list(
            cursor=a.cursor,
            limit=a.limit,
        )
    table[('wedrive', 'vip-list')] = _handle_wedrive_vip_list

    return table
