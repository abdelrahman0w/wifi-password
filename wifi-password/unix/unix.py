from ..manager import Manager
import os
import sys


class unixPass:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getSSID() -> str:
        try:
            ssid = Manager.command(
                                    "nmcli -t -f active,ssid dev wifi | grep '^yes:' | sed 's/^yes://'"
                                )
        except:
            print("Error! Please check your Network Manager")
            sys.exit(1)

        return ssid

    def getPW(self) -> str:
        command = f"nmcli -s -g 802-11-wireless-security.psk connection show {self.getSSID()}"

        if os.getegid() != 0:
            password = Manager.command(f"{command}")
        else:
            Manager.command(command)

        if password == "":
            print("Error! password not found")
            sys.exit(1)

        return password
