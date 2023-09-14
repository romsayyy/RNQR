import qrcode

# URL de redirection vers votre serveur local
url = "http://10.0.220.130:5000/qr-scanned"

# Générer le QR code avec l'URL de redirection
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("redirect_to_server.png")  # Sauvegarder l'image du QR code
