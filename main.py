import argparse
import yaml
import logging
from coordinates_generator import CoordinatesGenerator
from car_detector import MotionDetector
from colours import *


def main():
    logging.basicConfig(level=logging.INFO)
    image_file = "images/kimathi3.png"
    data_file = "data/coordinates.yml"
    start_frame = 0
    video_file = "videos/kimathi3.mp4"  # videos/kimathi1.mp4

    if image_file is not None:
        with open(data_file, "w+") as points:
            generator = CoordinatesGenerator(image_file, points, COLOR_BLUE)
            generator.generate()

    with open(data_file, "r") as data:
        points = yaml.load(data)
        print(points)
        detector = MotionDetector(video_file, points, int(start_frame))
        detector.detect_motion()


def parse_args():
    parser = argparse.ArgumentParser(description='Generates Coordinates File')

    parser.add_argument("--image",
                        dest="image_file",
                        required=False,
                        help="Image file to generate coordinates on")

    parser.add_argument("--video",
                        dest="video_file",
                        required=True,
                        help="Video file to detect motion on")

    parser.add_argument("--data",
                        dest="data_file",
                        required=True,
                        help="Data file to be used with OpenCV")

    parser.add_argument("--start-frame",
                        dest="start_frame",
                        required=False,
                        default=1,
                        help="Starting frame on the video")

    return parser.parse_args()


if __name__ == '__main__':
    main()
