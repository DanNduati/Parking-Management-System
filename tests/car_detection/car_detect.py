import os
import cv2
import numpy as np
from os.path import join, dirname

# Trained XML car classifier that describes some features of cars which we want to detect
cascade_file = join(dirname(__file__), "haarcascade_car.xml")
cars_cascade = cv2.CascadeClassifier(cascade_file)
videos_directory = join(os.getcwd(), "videos")
video_file = "cars.mp4"
writer = cv2.VideoWriter_fourcc(*'MJPG')


def main():
    video = cv2.VideoCapture(f"{join(videos_directory,video_file)}")
    # create vi
    out_file = join(videos_directory, "output.avi")
    out = cv2.VideoWriter(out_file, writer,
                          30, (1280, 720))
    while video.isOpened():
        ret, frame = video.read()
        '''
        # get the frame dimensions to use in the VideoWriter object
        fshape = frame.shape
        fheight = fshape[0]
        fwidth = fshape[1]
        print(fwidth, fheight)
        '''
        controlkey = cv2.waitKey(1)
        if ret:
            cars = cars_cascade.detectMultiScale(frame, 1.25, 4)
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h),
                              color=(0, 255, 0), thickness=2)
            out.write(frame)
            cv2.imshow('frame', frame)
        else:
            break

        if controlkey == ord('q'):
            break
    video.release()
    out.release()
    cv2.destroyAllWindows()


def test():
    # test video saving
    writer = cv2.VideoWriter("output.avi",
                             cv2.VideoWriter_fourcc(*"MJPG"), 30, (640, 480))
    for frame in range(1000):
        writer.write(np.random.randint(0, 255, (480, 640, 3)).astype('uint8'))
    writer.release()


if __name__ == "__main__":
    main()
