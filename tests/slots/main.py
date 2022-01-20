from colours import COL_BLUE, COL_GREEN
from coordinates import CoordinatesGenerator


def main():
    image_file = "images/kimathi4.png"
    if image_file is not None:
        generator = CoordinatesGenerator(image_file, 'Slots', COL_BLUE)
        generator.generate()


if __name__ == "__main__":
    main()
