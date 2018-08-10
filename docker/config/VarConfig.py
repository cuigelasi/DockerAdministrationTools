# encoding=utf-8
import os

# 获得当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取存放页面元素定位表达式文件的绝对路径
containerCheckConfigPath = parentDirPath + u"/config/container_managed/CheckConfig.ini"
containerCreateConfigPath = parentDirPath + u"/config/container_managed/CreateConfig.ini"
containerStartConfigPath = parentDirPath + u"/config/container_managed/StartConfig.ini"
containerStopConfigPath = parentDirPath + u"/config/container_managed/StopConfig.ini"
containerRemoveConfigPath = parentDirPath + u"/config/container_managed/RemoveConfig.ini"

imageLoadConfigPath = parentDirPath + u"/config/image_managed/LoadConfig.ini"
imageCheckConfigPath = parentDirPath + u"/config/image_managed/CheckConfig.ini"
imageDownloadConfigPath = parentDirPath + u"/config/image_managed/DownloadConfig.ini"
imageUploadConfigPath = parentDirPath + u"/config/image_managed/UploadConfig.ini"
imageRenameConfigPath = parentDirPath + u"/config/image_managed/RenameConfig.ini"
imageRemoveConfigPath = parentDirPath + u"/config/image_managed/RemoveConfig.ini"

networkCreateConfigPath = parentDirPath + u"/config/network_managed/CreateConfig.ini"
networkCheckConfigPath = parentDirPath + u"/config/network_managed/CheckConfig.ini"
networkRemoveConfigPath = parentDirPath + u"/config/network_managed/RemoveConfig.ini"

netcardAppendConfigPath = parentDirPath + u"/config/netcard_managed/AppendConfig.ini"
netcardRemoveConfigPath = parentDirPath + u"/config/netcard_managed/RemoveConfig.ini"

hostContainerConfigPath = parentDirPath + u"/config/host_managed/ContainerConfig.ini"
hostConfigPath = parentDirPath + u"/config/host_managed/HostConfig.ini"