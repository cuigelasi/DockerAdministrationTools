# encoding=utf-8
import configparser
from docker.config.VarConfig import networkCheckConfigPath

class CheckNetwork():
    """检查网络"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(networkCheckConfigPath, encoding='utf-8')
        self.section_check = "check"
        self.option_mac_net_container = ".".join((self.section_check, "mac_net_container"))

    def mac_net_container_obj(self):
        """获取创建mac_net_container网络的参数"""
        try:
            manage_options = self.cf.get(self.section_check, self.option_mac_net_container)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print CheckNetwork().option_mac_net_container
    print CheckNetwork().mac_net_container_obj()