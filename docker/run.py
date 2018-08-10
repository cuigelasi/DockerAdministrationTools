# encoding=utf-8
from docker.bin.Execute import Execute
hostname = raw_input("请输入执行命令的宿主机名：")
operation = raw_input("请输入执行的操作：")
if operation == "create_container":
    containername = raw_input("请输入容器名：")
    Execute.create_container_obj(hostname,containername)
elif operation == "stop_container":
    containername = raw_input("请输入容器名：")
    Execute.stop_container_obj(hostname,containername)
elif operation == "start_container":
    containername = raw_input("请输入容器名：")
    Execute.start_container_obj(hostname,containername)
elif operation == "remove_container":
    containername = raw_input("请输入容器名：")
    Execute.remove_container_obj(hostname,containername)
elif operation == "create_network":
    networkname = raw_input("请输入网络名：")
    Execute.create_network_obj(hostname,networkname)
elif operation == "remove_network":
    networkname = raw_input("请输入网络名：")
    Execute.remove_network_obj(hostname,networkname)
elif operation == "load_image":
    imagename = raw_input("请输入镜像名：")
    Execute.load_image_obj(hostname,imagename)
elif operation == "remove_image":
    imagename = raw_input("请输入镜像名：")
    Execute.remove_image_obj(hostname,imagename)
elif operation == "rename_image":
    imagename = raw_input("请输入镜像名：")
    newimagename = raw_input("请输入新的镜像名：")
    Execute.rename_image_obj(hostname,imagename,newimagename)


