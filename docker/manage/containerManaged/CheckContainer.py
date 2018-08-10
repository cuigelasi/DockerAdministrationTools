# encoding=utf-8
import configparser
from docker.config.VarConfig import containerCheckConfigPath

class CheckContainer():
    """检查容器"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(containerCheckConfigPath, encoding='utf-8')
        self.section_check = "check"
        self.option_nodejsnew = ".".join((self.section_check, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取检查nodejsnew容器的参数"""
        try:
            manage_options = self.cf.get(self.section_check, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print CheckContainer().option_nodejsnew
    print CheckContainer().nodejsnew_obj()