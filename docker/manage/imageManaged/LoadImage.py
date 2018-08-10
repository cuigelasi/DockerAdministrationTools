# encoding=utf-8
import configparser
from docker.config.VarConfig import imageLoadConfigPath

class LoadImage():
    """载入镜像"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(imageLoadConfigPath, encoding='utf-8')
        self.section_load = "load"
        self.option_nodejsnew = ".".join((self.section_load, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取载入nodejsnew镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_load, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print LoadImage().option_nodejsnew
    print LoadImage().nodejsnew_obj()