import pyqrcode
import hashlib

def createQR(direccion,datos,formato):
    img=pyqrcode.create(datos)
    if formato:
        img.png(direccion)
    else:
        img.svg(direccion)
    return

def hash2(str):
    h=hashlib.md5()
    h.update(str.encode('utf-8'))
    return h.hexdigest()

createQR('img.png',hash2('Esta es una prueba'),True)
