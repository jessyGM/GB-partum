import qr_reader as reader
import cv2 as cv
import data_display as display

def show_webcam(mirror=False):
    cam = cv.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv.flip(img, 1)
        cv.imshow('my webcam', img)
        for obj in reader.decode(img):
          display.openWindow(obj)
        if cv.waitKey(1) == 27:
            break  # esc to quit
    cv.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
