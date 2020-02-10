import pyqrcode
import hashlib

def createQR(direccion,datos,formato):
    h=hashlib.md5()
    h.update(datos.encode('utf-8'))
    img=pyqrcode.create(h.hexdigest())
    if formato:
        img.png(direccion)
    else:
        img.svg(direccion)
    return

createQR('img.png','esta es una prueba',True)
