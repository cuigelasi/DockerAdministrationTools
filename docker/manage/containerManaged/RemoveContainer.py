# encoding=utf-8
import configparser
from docker.config.VarConfig import containerRemoveConfigPath

class RemoveContainer():
    """删除容器"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(containerRemoveConfigPath, encoding='utf-8')
        self.section_remove = "remove"
        self.option_nodejsnew = ".".join((self.section_remove, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取删除nodejsnew容器的参数"""
        try:
            manage_options = self.cf.get(self.section_remove, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print RemoveContainer().option_nodejsnew
    print RemoveContainer().nodejsnew_obj()