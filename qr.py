import qrcode

data = "python/images.jpg"
qr = qrcode.make(data)
qr.save("sample_qr_code.png")
print("QR code generated and saved as 'sample_qr_code.png'.")