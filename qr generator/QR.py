import pyqrcode

url="https://vasanthabalaji.netlify.app/"
process=pyqrcode.create(url)
process.png("qrcode1.png", scale = 8)
print("QR generated")
