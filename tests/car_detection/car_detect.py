import os
import cv2
import numpy as np
from os.path import join, dirname

# Trained XML car classifier that describes some features of cars which we want to detect
cascade_file = join(dirname(__file__), "haarcascade_car.xml")
cars_cascade = cv2.CascadeClassifier(cascade_file)
videos_directory = join(os.getcwd(), "videos")
video_file = "cars.mp4"


def main():
    video = cv2.VideoCapture(f"{join(videos_directory,video_file)}")
    while video.isOpened():
        ret, frame = video.read()
        controlkey = cv2.waitKey(1)
        if ret:
            cars = cars_cascade.detectMultiScale(frame, 1.25, 4)
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h),
                              color=(0, 255, 0), thickness=2)
            cv2.imshow('frame', frame)
        else:
            break

        if controlkey == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
