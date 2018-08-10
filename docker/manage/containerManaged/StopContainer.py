# encoding=utf-8
import configparser
from docker.config.VarConfig import containerStopConfigPath

class StopContainer():
    """关闭容器"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(containerStopConfigPath, encoding='utf-8')
        self.section_stop = "stop"
        self.option_nodejsnew = ".".join((self.section_stop, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取关闭nodejsnew容器的参数"""
        try:
            manage_options = self.cf.get(self.section_stop, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print StopContainer().option_nodejsnew
    print StopContainer().nodejsnew_obj()