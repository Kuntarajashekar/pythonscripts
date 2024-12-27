import qrcode

data = "https://www.github.com/Kuntarajashekar"

qr = qrcode.make(data)

qr.save("python_qr.png")

print("qr code is generated successfully")
