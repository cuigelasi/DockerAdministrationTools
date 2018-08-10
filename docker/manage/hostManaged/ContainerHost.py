# encoding=utf-8
import configparser
from docker.config.VarConfig import hostContainerConfigPath

class ContainerHost():
    """读取容器启动所在宿主机ip"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(hostContainerConfigPath, encoding='utf-8')
        self.section_host = "host"
        self.option_nodejsnew = ".".join((self.section_host, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取nodejsnew容器启动的所在宿主机ip"""
        try:
            manage_options = self.cf.get(self.section_host, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print ContainerHost().option_nodejsnew
    print ContainerHost().nodejsnew_obj()