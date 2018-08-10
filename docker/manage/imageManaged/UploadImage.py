# encoding=utf-8
import configparser
from docker.config.VarConfig import imageUploadConfigPath

class UploadImage():
    """上传镜像"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(imageUploadConfigPath, encoding='utf-8')
        self.section_upload = "upload"
        self.option_nodejsnew = ".".join((self.section_upload, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取上传nodejsnew镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_upload, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print UploadImage().option_nodejsnew
    print UploadImage().nodejsnew_obj()