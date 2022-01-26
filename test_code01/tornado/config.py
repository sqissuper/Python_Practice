async def get_qci_task_detail_info(task_id):
    """
    查询大房间详情信息
    :param task_id:任务id
    :return:
    """
    context = {}
    session = Session()
    try:
        rows = session.query(BigRoomDetailInfo).filter(BigRoomDetailInfo.task_id == task_id).all()
        big_room_detail_list = []
        for row in rows:
            ret_info = {
                "task_id": str(row.task_id),
                "user_id": str(row.user_id),
                "env_name": str(row.env_name),
                "account_id": str(row.account_id),
                "meeting_code": str(row.meeting_code),
                "meeting_id": str(row.meeting_id),
                "room_id": str(row.room_id),
                "tiny_id": str(row.tiny_id),
                "join_time": str(row.join_time),
                "end_time": str(row.end_time),
            }
            # 获取举手类型
            task_id_user_id_role_type = task_id + '_' + row.user_id + '_user_role_type'
            rsp_role_type = await query_big_room_task_user_role_type(task_id_user_id_role_type)

            # 获取角色类型
            task_id_user_id_hands_type = task_id + '_' + row.user_id + '_hands_type'
            rsp_hands_type = await query_big_room_task_hands_type(task_id_user_id_hands_type)
            ret_info["user_role_type"] = rsp_role_type.get("user_role_type")
            ret_info["hands_type"] = rsp_hands_type.get("hands_type")
            big_room_detail_list.append(ret_info)
        context = {'big_room_detail_info': big_room_detail_list}
        session.close()
        return context
    except (DatabaseError, OperationalError) as err:
        logger.error("query_qci_task_detail_info failed err:{}".format(err))
        context["message"] = "get_qci_task_detail_info failed err:{}".format(err)
        session.rollback()
        session.close()
        return context