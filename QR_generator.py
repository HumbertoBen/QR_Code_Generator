import pyqrcode
from pyqrcode import QRCode

# init the string that will represent the QR Code
s = "https://delbravoapps.com/trafico/login"

# Now we generate the QR Code
url = pyqrcode.create(s)

# Now we create and save the png file with a name "myqr.png"
url.svg("myqr.svg", scale=8)
