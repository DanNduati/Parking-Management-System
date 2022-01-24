from colours import COL_BLUE
from coordinates import CoordinatesGenerator


def main():
    image_file = "images/kimathi4.png"
    cord_file = "tests/slots/data/coordinates.json"
    if image_file is not None:
        generator = CoordinatesGenerator(
            image_file, 'Slots', cord_file, COL_BLUE)
        generator.generate()


if __name__ == "__main__":
    main()
