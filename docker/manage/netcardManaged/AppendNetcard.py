# encoding=utf-8
import configparser
from docker.config.VarConfig import netcardAppendConfigPath

class AppendNetcard():
    """添加网卡"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(netcardAppendConfigPath, encoding='utf-8')
        self.section_append = "append"
        self.option_mac_net_container = ".".join((self.section_append, "mac_net_container"))

    def mac_net_container_obj(self):
        """获取添加mac_net_container网卡的参数"""
        try:
            manage_options = self.cf.get(self.section_append, self.option_mac_net_container)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print AppendNetcard().option_mac_net_container
    print AppendNetcard().mac_net_container_obj()