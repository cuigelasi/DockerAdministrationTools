# encoding=utf-8
import configparser
from docker.config.VarConfig import networkCreateConfigPath

class CreateNetwork():
    """创建网络"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(networkCreateConfigPath, encoding='utf-8')
        self.section_create = "create"
        self.option_mac_net_container = ".".join((self.section_create, "mac_net_container"))

    def mac_net_container_obj(self):
        """获取创建mac_net_container网络的参数"""
        try:
            manage_options = self.cf.get(self.section_create, self.option_mac_net_container)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print CreateNetwork().option_mac_net_container
    print CreateNetwork().mac_net_container_obj()