import platform
import sys

class OS:
    def __init__(self) -> None:
        self.platform = platform.system().lower()
        self.arch = '64' if sys.maxsize > 2**32 else '32'

    @property
    def getOS(self) -> str:
        if self.platform == 'windows':
            return 'windows'
        else:
            return 'unix'

    @property
    def getArch(self) -> str:
        if self.arch == '64':
            return '64'
        else:
            return '32'