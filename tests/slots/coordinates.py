import cv2
import numpy as np
from colours import COL_BLUE, COL_WHITE
from drawing_utils import draw_contours


class CoordinatesGenerator:
    KEY_QUIT = ord("q")

    def __init__(self, image, caption, color) -> None:

        self.caption = caption
        self.color = color

        self.image = cv2.imread(image).copy()
        self.click_count = 0
        self.ids = 0
        self.coordinates = []
        cv2.namedWindow(self.caption, cv2.WINDOW_GUI_EXPANDED)
        cv2.setMouseCallback(self.caption, self.__mouse_callback)

    def generate(self) -> None:
        while True:
            cv2.imshow(self.caption, self.image)
            key = cv2.waitKey(0)
            if key == CoordinatesGenerator.KEY_QUIT:
                break
        cv2.destroyAllWindows()

    def __mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.coordinates.append((x, y))
            self.click_count += 1

            if self.click_count >= 4:
                # handle done
                self.__handle_done()
            elif self.click_count > 1:
                # handle slot space drawing progress
                self.__handle_click_progress()
        cv2.imshow(self.caption, self.image)

    def __handle_click_progress(self):
        # draw line for last 2 cordinate entries
        cv2.line(self.image, self.coordinates[-2],
                 self.coordinates[-1], COL_BLUE, 1)

    def __handle_done(self):
        # draw lines from the third(index 2) cordinate to the last(index 3) and from the first(index 0) to the last(index 3)
        cv2.line(self.image, self.coordinates[2],
                 self.coordinates[3], self.color, 2)
        cv2.line(self.image, self.coordinates[3],
                 self.coordinates[0], self.color, 2)
        # reset click count
        self.click_count = 0
        coordinates = np.array(self.coordinates)
        print(coordinates)

        draw_contours(self.image, coordinates)
        # reset coordinates
        for i in range(len(self.coordinates)):
            self.coordinates.pop()
