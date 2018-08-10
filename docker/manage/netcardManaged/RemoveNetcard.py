# encoding=utf-8
import configparser
from docker.config.VarConfig import netcardRemoveConfigPath

class RemoveNetcard():
    """删除网卡"""
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(netcardRemoveConfigPath, encoding='utf-8')
        self.section_remove = "remove"
        self.option_mac_net_container = ".".join((self.section_remove, "mac_net_container"))

    def mac_net_container_obj(self):
        """获取删除mac_net_container网卡的参数"""
        try:
            manage_options = self.cf.get(self.section_remove, self.option_mac_net_container)
            return manage_options
        except Exception as e:
            raise e

if __name__ == '__main__':
    print RemoveNetcard().option_mac_net_container
    print RemoveNetcard().mac_net_container_obj()