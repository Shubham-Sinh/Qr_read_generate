import qrcode

data = "A hello from Shubham 🚀"

qr = qrcode.QRCode(
    version=1,  # controls size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("custom_qr.png")
