import qrcode

feats = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=40, 
    border=3
    )
user_input = input("https://nathan-austin.github.io/")

feats.add_data(user_input)

feats.make(fit=True)

img = feats.make_image(
    fill_color="black", 
    back_color="white"
    )

img.save("./qrcodes/portfolio.png")

