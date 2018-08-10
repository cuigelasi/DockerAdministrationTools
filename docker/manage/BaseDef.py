# encoding=utf-8
import configparser
from docker.config.VarConfig import containerCreateConfigPath
from docker.config.VarConfig import containerStartConfigPath
from docker.config.VarConfig import containerStopConfigPath
from docker.config.VarConfig import containerRemoveConfigPath

from docker.config.VarConfig import imageDownloadConfigPath
from docker.config.VarConfig import imageUploadConfigPath
from docker.config.VarConfig import imageRenameConfigPath
from docker.config.VarConfig import imageRemoveConfigPath

from docker.config.VarConfig import networkCreateConfigPath
from docker.config.VarConfig import networkRemoveConfigPath

from docker.config.VarConfig import netcardAppendConfigPath
from docker.config.VarConfig import netcardRemoveConfigPath

class BaseContainerCreate(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(containerCreateConfigPath, encoding='utf-8')

    def getOptionValue(self, sectionName, optionName):
        """获取指定section下的指定option的值"""
        value = self.cf.get(sectionName, optionName)
        return value

class BaseContainerStart(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(containerStartConfigPath, encoding='utf-8')

class BaseContainerStop(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(containerStopConfigPath, encoding='utf-8')

class BaseContainerRemove(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(containerRemoveConfigPath, encoding='utf-8')



class BaseImageDownload(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(imageDownloadConfigPath, encoding='utf-8')

class BaseImageUpload(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(imageUploadConfigPath, encoding='utf-8')

class BaseImageRename(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(imageRenameConfigPath, encoding='utf-8')

class BaseImageRemove(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(imageRemoveConfigPath, encoding='utf-8')



class BaseNetworkCreate(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(networkCreateConfigPath, encoding='utf-8')

class BaseNetworkRemove(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(networkRemoveConfigPath, encoding='utf-8')



class BaseNetcardAppend(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(netcardAppendConfigPath, encoding='utf-8')

class BaseNetcardRemove(object):
    '''基础页面类，可以设置公共的方法和属性'''
    def __init__(self):
        '''类初始化时读取配置文件'''
        self.cf = configparser.ConfigParser()
        self.cf.read(netcardRemoveConfigPath, encoding='utf-8')