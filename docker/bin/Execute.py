# encoding=utf-8
from docker.manage.hostManaged.ContainerHost import ContainerHost
from docker.manage.hostManaged.Host import Host

from docker.manage.networkManaged.CreateNetwork import CreateNetwork
from docker.manage.networkManaged.CheckNetwork import CheckNetwork
from docker.manage.networkManaged.RemoveNetwork import RemoveNetwork

from docker.manage.imageManaged.CheckImage import CheckImage
from docker.manage.imageManaged.RemoveImage import RemoveImage
from docker.manage.imageManaged.RenameImage import RenameImage
from docker.manage.imageManaged.LoadImage import LoadImage

from docker.manage.containerManaged.CreateContainer import CreateContainer
from docker.manage.containerManaged.CheckContainer import CheckContainer
from docker.manage.containerManaged.RemoveContainer import RemoveContainer
from docker.manage.containerManaged.StopContainer import StopContainer
from docker.manage.containerManaged.StartContainer import StartContainer

from docker.manage.netcardManaged.AppendNetcard import AppendNetcard
from docker.manage.netcardManaged.RemoveNetcard import RemoveNetcard

from docker.common.ExecuteAction import ExecuteAction

class Execute(object):
    """执行操作"""

    @staticmethod
    def create_network_obj(hostname,network_name):
        """创建网络"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            create_command = eval('CreateNetwork().' + network_name + '_obj()')
            check_command = eval('CheckNetwork().' + network_name + '_obj()')
            network_status = ExecuteAction.check_obj(execute_host, check_command, 'network','status')
            if network_status == 'inexistence':
                ExecuteAction.create_obj(execute_host,create_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'),create_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command, "network")
        except Exception as e:
            raise e

    @staticmethod
    def remove_network_obj(hostname, network_name):
        """删除网络"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            remove_command = eval('RemoveNetwork().' + network_name + '_obj()')
            check_command = eval('CheckNetwork().' + network_name + '_obj()')
            network_status = ExecuteAction.check_obj(execute_host, check_command, 'network', 'status')
            if network_status == 'exist':
                ExecuteAction.create_obj(execute_host, remove_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'), remove_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command, "network")
        except Exception as e:
            raise e

    @staticmethod
    def load_image_obj(hostname, image_name):
        """载入镜像"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            load_command = eval('LoadImage().' + image_name + '_obj()')
            check_command = eval('CheckImage().' + image_name + '_obj()')
            image_status = ExecuteAction.check_obj(execute_host, check_command, 'image', 'status')
            if image_status == 'inexistence':
                ExecuteAction.common_obj(execute_host, load_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'), load_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command, "image")
        except Exception as e:
            raise e


    @staticmethod
    def remove_image_obj(hostname, image_name):
        """删除镜像"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            remove_command = eval('RemoveImage().' + image_name + '_obj()')
            check_command = eval('CheckImage().' + image_name + '_obj()')
            image_status = ExecuteAction.check_obj(execute_host, check_command, 'image', 'status')
            if image_status == 'exist':
                ExecuteAction.remove_obj(execute_host, remove_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'), remove_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command, "image")
        except Exception as e:
            raise e

    @staticmethod
    def rename_image_obj(hostname, image_name, new_image_name):
        """更改镜像名字"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            rename_command = eval('RenameImage().' + image_name + '_obj()')
            rename_command = rename_command.replace('new_image_name', new_image_name)
            check_command = eval('CheckImage().' + image_name + '_obj()')
            image_status = ExecuteAction.check_obj(execute_host, check_command, 'image', 'status')
            if image_status == 'exist':
                ExecuteAction.common_obj(execute_host, rename_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'), rename_command.encode('utf-8'))
                check_command = CheckImage().common_obj()
                check_command = check_command.replace('new_image_name', new_image_name)
                ExecuteAction.check_obj(execute_host,check_command,"image",status=None,tag="tag")
        except Exception as e:
            raise e


    @staticmethod
    def create_container_obj(hostname,container_name):
        """创建容器"""
        try:
            # execute_host = ContainerHost().nodejsnew_obj()
            # create_command = CreateContainer().nodejsnew_obj()
            # execute_host = eval('ContainerHost().' + container_name + '_obj()')

            execute_host = eval("Host('" + hostname + "').host_obj()")
            create_command = eval('CreateContainer().' + container_name + '_obj()')
            check_command = eval('CheckContainer().' + container_name + '_obj()')
            container_status = ExecuteAction.check_obj(execute_host, check_command, 'container','status')
            if container_status == 'clear':
                ExecuteAction.create_obj(execute_host,create_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'),create_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command, 'container')
        except Exception as e:
            raise e

    @staticmethod
    def remove_container_obj(hostname,container_name):
        """删除容器"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            remove_command = eval('RemoveContainer().' + container_name + '_obj()')
            check_command = eval('CheckContainer().' + container_name + '_obj()')
            container_status = ExecuteAction.check_obj(execute_host, check_command, 'container', 'status')
            if container_status == 'start' or container_status == 'stop':
                ExecuteAction.remove_obj(execute_host,remove_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'),remove_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command ,'container')
        except Exception as e:
            raise e

    @staticmethod
    def stop_container_obj(hostname,container_name):
        """停止容器"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            stop_command = eval('StopContainer().' + container_name + '_obj()')
            check_command = eval('CheckContainer().' + container_name + '_obj()')
            container_status = ExecuteAction.check_obj(execute_host, check_command, 'container', 'status')
            if container_status == 'start':
                ExecuteAction.common_obj(execute_host,stop_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'),stop_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command ,'container')
        except Exception as e:
            raise e

    @staticmethod
    def start_container_obj(hostname,container_name):
        """启动容器"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            start_command = eval('StartContainer().' + container_name + '_obj()')
            check_command = eval('CheckContainer().' + container_name + '_obj()')
            container_status = ExecuteAction.check_obj(execute_host, check_command, 'container', 'status')
            if container_status == 'stop':
                ExecuteAction.common_obj(execute_host,start_command)
                print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'),start_command.encode('utf-8'))
                ExecuteAction.check_obj(execute_host, check_command ,'container')
        except Exception as e:
            raise e

    @staticmethod
    def append_netcard_obj(hostname,network_name,container_name):
        """添加网卡"""
        try:
            execute_host = eval("Host('" + hostname + "').host_obj()")
            append_command = eval('AppendNetcard().' + network_name + '_obj()')
            print execute_host
            print append_command
            # check_command = eval('CheckNetcard().' + container_name + '_obj()')
            # netcard_status = ExecuteAction.check_obj(execute_host, check_command, 'netcard', 'status')
            # if netcard_status == 'stop':
            #     ExecuteAction.common_obj(execute_host,append_command)
            #     print "在宿主机 %s 上执行: %s" % (execute_host.encode('utf-8'),append_command.encode('utf-8'))
            #     ExecuteAction.check_obj(execute_host, check_command ,'netcard')
        except Exception as e:
            raise e


if __name__ == '__main__':
    # Execute.create_network_obj('docker1','mac_net_container')
    # Execute.remove_network_obj('docker1','mac_net_container')
    #
    # Execute.load_image_obj('docker1','nodejsnew')
    # Execute.remove_image_obj('docker1','nodejsnew')
    # Execute.rename_image_obj('docker1','nodejsnew','nodejsnew')
    #
    # Execute.create_container_obj('docker2','nodejsnew')
    # Execute.stop_container_obj('docker2','nodejsnew')
    # Execute.start_container_obj('docker2','nodejsnew')
    # Execute.remove_container_obj('docker2','nodejsnew')

    Execute.append_netcard_obj('docker2','mac_net_container','nodejsnew')






