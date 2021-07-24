import subprocess
import qrcode


class Manager:
    def __init__(self) -> None:
        pass

    @staticmethod
    def command(command) -> str:
        output, _ = subprocess.Popen(
                        command,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.DEVNULL,
                        shell = True
                    ).communicate()

        return output.decode("utf-8").rstrip('\r\n')
    
    @staticmethod
    def getDict(lst) -> dict:
        return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

    def generateQR(self, ssid, pw) -> None:
        data = f"WIFI:T:WPA;S:{ssid};P:{pw};;"
        qr = qrcode.QRCode(
                version = 1,
                error_correction = qrcode.constants.ERROR_CORRECT_L,
                box_size = 5,
                border = 2
            )
        qr.add_data(data)
        qr.make()
        qr.print_tty()
