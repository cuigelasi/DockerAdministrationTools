# encoding=utf-8
import configparser
from docker.config.VarConfig import containerStartConfigPath

class StartContainer():
    """启动容器"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(containerStartConfigPath, encoding='utf-8')
        self.section_start = "start"
        self.option_nodejsnew = ".".join((self.section_start, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取启动nodejsnew容器的参数"""
        try:
            manage_options = self.cf.get(self.section_start, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print StartContainer().option_nodejsnew
    print StartContainer().nodejsnew_obj()