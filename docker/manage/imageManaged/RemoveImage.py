# encoding=utf-8
import configparser
from docker.config.VarConfig import imageRemoveConfigPath

class RemoveImage():
    """删除镜像"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(imageRemoveConfigPath, encoding='utf-8')
        self.section_remove = "remove"
        self.option_nodejsnew = ".".join((self.section_remove, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取删除nodejsnew镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_remove, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print RemoveImage().option_nodejsnew
    print RemoveImage().nodejsnew_obj()