from .platform import OS
from .windows.win import winPass
from .linUni.linUni import linUniPass
from .manager import Manager
import inquirer


class wifiPass:
    def __init__(self) -> None:
        self.platform = OS().getOS
        select = [
                inquirer.List(
                        'auto',
                        message = "Select your choice >>>",
                        choices = [
                            'Generate for the current network',
                            'Generate for a new network'
                        ],
                    ),
                ]
        
        if inquirer.prompt(select)['auto'] == 'Generate for the current network':
            self.auto = True
        else:
            self.auto = False

    def __getSSID(self) -> str:
        if not self.auto:
            return input("Enter SSID >>> ")

        if self.platform == 'windows':
            return winPass().getSSID()
        else:
            return linUniPass().getSSID()

    def __getPW(self) -> str:
        if not self.auto:
            return input("Enter Password >>> ")

        if self.platform == 'windows':
            return winPass().getPW()
        else:
            return linUniPass().getPW()

    def generateQR(self) -> None:
        Manager().generateQR(ssid=self.__getSSID(), pw=self.__getPW())

def main():
    print("""
 __          ___        ______ _   _____                                    _ 
 \ \        / (_)      |  ____(_) |  __ \                                  | |
  \ \  /\  / / _ ______| |__   _  | |__) |_ _ ___ _____      _____  _ __ __| |
   \ \/  \/ / | |______|  __| | | |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
    \  /\  /  | |      | |    | | | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |
     \/  \/   |_|      |_|    |_| |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|

Welcome to Wi-Fi Password.
    """)
    wifiPass().generateQR()


if  __name__ == "__main__":
    main()
