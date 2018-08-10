# encoding=utf-8
import configparser
from docker.config.VarConfig import containerCreateConfigPath

class CreateContainer():
    """创建容器"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(containerCreateConfigPath, encoding='utf-8')
        self.section_create = "create"
        self.option_nodejsnew = ".".join((self.section_create, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取创建nodejsnew容器的参数"""
        try:
            manage_options = self.cf.get(self.section_create, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print CreateContainer().option_nodejsnew
    print CreateContainer().nodejsnew_obj()