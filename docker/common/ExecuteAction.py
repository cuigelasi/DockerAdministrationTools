# encoding=utf-8
import os
from time import sleep
class ExecuteAction(object):
    """执行命令行操作"""
    @staticmethod
    def create_obj(execute_host,execute_command):
        """创建操作"""
        try:

            execute_action = os.popen('ssh %s "%s"' % (execute_host, execute_command)).read()
            print execute_action
        except Exception as e:
            raise e

    @staticmethod
    def check_obj(execute_host,execute_command,type,status=None,tag=None):
        """检查操作"""
        try:
            execute_action = os.popen('ssh %s "%s"' % (execute_host, execute_command)).read()
            sleep(3)
            execute_action_num = len(execute_action.split( ))
            # print execute_action_num
            # print execute_action
            if type == "container":
                if execute_action_num == 0:
                    container_status = 'clear'
                    if status is None:
                        print "容器已清除。"
                    return container_status
                elif execute_action_num == 10:
                    container_status = 'start'
                    if status is None:
                        print "容器 %s 已创建。" % execute_action.split()[-1]
                    return container_status
                elif execute_action_num == 12 and execute_action.split()[6] == "Up":
                    container_status = 'start'
                    if status is None:
                        print "容器 %s 已创建,现在处于运行状态。" % execute_action.split()[-1]
                    return container_status
                elif execute_action_num == 12 and execute_action.split()[6] == "Exited":
                    container_status = 'stop'
                    if status is None:
                        print "容器 %s 已创建,但现在处于关闭状态。" % execute_action.split()[-1]
                    return container_status
                else:
                    container_status = 'error'
                    if status is None:
                        print "容器创建异常，请人工排查。"
                    return container_status
            elif type == "network":
                if execute_action_num == 0:
                    network_status = 'inexistence'
                    if status is None:
                        print "网络已删除。"
                    return network_status
                elif execute_action_num == 4:
                    network_status = 'exist'
                    if status is None:
                        print "网络已创建。"
                    return network_status
            elif type == "image":
                if execute_action_num == 0:
                    image_status = 'inexistence'
                    if status is None:
                        print "镜像已删除。"
                    return image_status
                elif execute_action_num == 8:
                    image_status = 'exist'
                    if status is None:
                        print "镜像已创建。"
                    return image_status
                elif execute_action_num % 8 == 0 and tag is not None:
                    image_status = 'tag_exist'
                    if status is None:
                        print "镜像名已修改。"
                    return image_status
        except Exception as e:
            raise e

    @staticmethod
    def remove_obj(execute_host,execute_command):
        """删除操作"""
        try:
            execute_action = os.popen('ssh %s "%s"' % (execute_host, execute_command)).read()
            print execute_action
        except Exception as e:
            raise e

    @staticmethod
    def common_obj(execute_host,execute_command):
        """通用操作"""
        try:
            execute_action = os.popen('ssh %s "%s"' % (execute_host, execute_command)).read()
            print execute_action
        except Exception as e:
            raise e
