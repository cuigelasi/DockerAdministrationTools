# encoding=utf-8
import configparser
from docker.config.VarConfig import hostConfigPath

class Host():
    """读取所在宿主机ip"""
    def __init__(self,hostname):
        self.cf = configparser.ConfigParser()
        self.cf.read(hostConfigPath, encoding='utf-8')
        self.section_host = 'docker'
        self.option_hostname = ".".join((self.section_host, hostname))

    def host_obj(self):
        """获取网络创建的所在宿主机ip"""
        try:
            manage_options = self.cf.get(self.section_host, self.option_hostname)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print Host('docker1').option_hostname
    print Host('docker1').host_obj()