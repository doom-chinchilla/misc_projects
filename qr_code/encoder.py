import qrcode 

text = "Join my Spotify jam!"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(text)

qr.make(fit=True)
img = qr.make_image(fill_color = 'green', back_color = 'white')

#img.save()