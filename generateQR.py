import qrcode

def generateQR(data):
    img = qrcode.make(data)
    img.save("qr.png")
