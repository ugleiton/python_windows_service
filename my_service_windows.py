#resolver erro ModuleNotFoundError: No module named 'win32serviceutil' 
#https://stackoverflow.com/a/70625723/9930021
import os
import sys
import site

service_directory = os.path.dirname(__file__)
source_directory = os.path.abspath(service_directory)
os.chdir(source_directory)
venv_base = os.path.abspath(os.path.join(source_directory, "venv"))
sys.path.append(".")
old_os_path = os.environ['PATH']
os.environ['PATH'] = os.path.join(venv_base, "Scripts") + os.pathsep + old_os_path
site_packages = os.path.join(venv_base, "Lib", "site-packages")
prev_sys_path = list(sys.path)
site.addsitedir(site_packages)
sys.real_prefix = sys.prefix
sys.prefix = venv_base

new_sys_path = list()
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[: 0] = new_sys_path

import time
import random
from pathlib import Path
from SMWinservice import SMWinservice

class MyServicePython(SMWinservice):
    _svc_name_ = "MyServicePython"
    _svc_display_name_ = "My Service Python"
    _svc_description_ = "Simple service in python for windows"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:{x}.txt').touch()
            time.sleep(5)

if __name__ == '__main__':
    MyServicePython.parse_command_line()
