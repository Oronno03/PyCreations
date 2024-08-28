import qrcode


class QrCode:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def generate(self, file: str, bg: str, fg: str):
        user_input = input("Enter text to turn into a qr code: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image()
            qr_image.save(file)

            print("Successfully created qr code")
        except Exception as e:
            print("Error")
            print(e)


def main():
    myqr = QrCode(size=50, padding=1)
    myqr.generate("qrcode.png", "black", "white")


main()