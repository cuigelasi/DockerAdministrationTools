# encoding=utf-8
import configparser
from docker.config.VarConfig import imageCheckConfigPath

class CheckImage():
    """检查镜像"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(imageCheckConfigPath, encoding='utf-8')
        self.section_check = "check"
        self.option_common = ".".join((self.section_check, "common"))
        self.option_nodejsnew = ".".join((self.section_check, "nodejsnew"))

    def common_obj(self):
        """获取检查镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_check, self.option_common)
            return manage_options
        except Exception as e:
            raise e

    def nodejsnew_obj(self):
        """获取检查nodejsnew镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_check, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print CheckImage().option_nodejsnew
    print CheckImage().nodejsnew_obj()
    print CheckImage().common_obj()