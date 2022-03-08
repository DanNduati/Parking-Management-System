import yaml
from colours import COL_BLUE
from coordinates_generator import CoordinatesGenerator
from car_detector import CarDetector


def main():
    image_file = "images/kimathi4.png"
    cord_file = "data/coordinates.yml"
    video_file = "videos/kimathi4.mp4"

    if image_file is not None:
        with open(cord_file, "w+") as cord:
            generator = CoordinatesGenerator(
                image_file, 'Slots', cord, COL_BLUE)
            generator.generate()
    with open(cord_file, "r") as data:
        points = yaml.load(data)
        detector = CarDetector(video_file, points)
        detector.detect_car()


if __name__ == "__main__":
    main()
