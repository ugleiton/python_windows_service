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
