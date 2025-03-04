import qrcode
from  PIL import Image
qr=qrcode.QRCode(version=1,
                 error_corection=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=4)
qr.add_data("www.linkedin.com/in/sachin-rajpoot-86547b251")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("Qrcode.png")
