# encoding=utf-8
import configparser
from docker.config.VarConfig import imageDownloadConfigPath

class DownloadImage():
    """下载镜像"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(imageDownloadConfigPath, encoding='utf-8')
        self.section_download = "download"
        self.option_nodejsnew = ".".join((self.section_download, "nodejsnew"))

    def nodejsnew_obj(self):
        """获取下载nodejsnew镜像的参数"""
        try:
            manage_options = self.cf.get(self.section_download, self.option_nodejsnew)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print DownloadImage().option_nodejsnew
    print DownloadImage().nodejsnew_obj()