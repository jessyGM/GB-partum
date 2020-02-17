import pyzbar.pyzbar as pyzbar
import cv2 as cv
import data_display as display
import database_manager as db

def show_webcam(mirror=False):
    database=db.database('data.txt')
    cam = cv.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv.flip(img, 1)
        cv.imshow('my webcam', img)
        for obj in pyzbar.decode(img):
          display.openWindow(obj,database)
        if cv.waitKey(1) == 27:
            db.savefile('prueba.txt',database)
            break  # esc to quit
    cv.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
