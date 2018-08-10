# encoding=utf-8
from docker.bin.Execute import Execute

Execute.create_container_obj('docker2', 'nodejsnew')
Execute.stop_container_obj('docker2', 'nodejsnew')
Execute.start_container_obj('docker2', 'nodejsnew')
Execute.remove_container_obj('docker2', 'nodejsnew')

Execute.create_network_obj('docker1','mac_net_container')
Execute.remove_network_obj('docker1','mac_net_container')

Execute.load_image_obj('docker1','nodejsnew')
Execute.remove_image_obj('docker1','nodejsnew')
Execute.rename_image_obj('docker1','nodejsnew','nodejsnew')