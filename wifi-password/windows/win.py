from ..manager import Manager
import subprocess
import os
import re


class winPass:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getSSID() -> str:
        ssid = list(
            filter(
                None,
                map(
                    lambda x: x.strip(),
                    re.split(
                        ":|\n",
                        Manager.command("netsh wlan show interfaces")
                    )
                )
            )
        )
        ssid.pop(0)

        return Manager.getDict(ssid)["Profile"]

    @staticmethod
    def __pwCommand() -> None:
        subprocess.call([rf"{os.getcwd()}\wifi-password\windows\get.bat"])

    def getPW(self) -> str:
        if not os.path.isfile(rf"{os.getcwd()}\wifi-password\windows\passwords\_pass.txt"):
            self.__pwCommand()

            while True:
                try:
                    with open(rf"{os.getcwd()}\wifi-password\windows\passwords\_pass.txt", "r") as file:
                        pw = Manager.getDict(list(
                            filter(
                                None,
                                map(
                                    lambda x: x.strip(),
                                    re.split(
                                        ":|\n",
                                        file.read()
                                    )
                                )
                            )
                        ))[self.getSSID()]
                    return pw
                except:
                    continue
        else:
            try:
                with open(rf"{os.getcwd()}\wifi-password\windows\passwords\_pass.txt", "r") as file:
                    pw = Manager.getDict(list(
                        filter(
                            None,
                            map(
                                lambda x: x.strip(),
                                re.split(
                                    ":|\n",
                                    file.read()
                                )
                            )
                        )
                    ))[self.getSSID()]
                return pw
            except:
                with open(rf"{os.getcwd()}\wifi-password\windows\passwords\_pass.txt", "w") as file:
                    file.write("")

                self.__pwCommand()

                while True:
                    try:
                        with open(rf"{os.getcwd()}\wifi-password\windows\passwords\_pass.txt", "r") as file:
                            pw = Manager.getDict(list(
                                filter(
                                    None,
                                    map(
                                        lambda x: x.strip(),
                                        re.split(
                                            ":|\n",
                                            file.read()
                                        )
                                    )
                                )
                            ))[self.getSSID()]
                        return pw
                    except:
                        continue
