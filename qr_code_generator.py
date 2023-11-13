# install all the libraries needed
# create a function that collects a text and converts it to a qrcode
# save the qrcode as an image
# create a function that takes the image and converts it to a text
# run the function

import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10 ,
        border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black" , black_color="white")
    img.save("qrimg001.png")
    
url = input("Please enter your url :")
generate_qrcode(url)