# encoding=utf-8
import configparser
from docker.config.VarConfig import imageRenameConfigPath

class RenameImage():
    """重命名镜像"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(imageRenameConfigPath, encoding='utf-8')
        self.section_rename = "rename"
        self.option_nodejsnew = ".".join((self.section_rename, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取重命名nodejsnew镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_rename, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print RenameImage().option_nodejsnew
    print RenameImage().nodejsnew_obj()