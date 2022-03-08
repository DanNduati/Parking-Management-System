import json
import cv2
import numpy as np
from colours import COL_WHITE
from drawing_utils import draw_contours


class CoordinatesGenerator:
    KEY_QUIT = ord("q")

    def __init__(self, image, caption, output_file, color):
        self.caption = caption
        self.output_file = output_file
        self.color = color
        self.image = cv2.imread(image).copy()
        self.click_count = 0
        self.ids = 0
        self.coordinates = []
        self.coordinates_ = []
        cv2.namedWindow(self.caption, cv2.WINDOW_GUI_EXPANDED)
        cv2.setMouseCallback(self.caption, self.handle_mouse)

    def generate(self):
        while True:
            cv2.imshow(self.caption, self.image)
            key = cv2.waitKey(0)
            if key == self.KEY_QUIT:
                # store coordinates to file
                # self.store_slots(self.coordinates_, self.output_file)
                #cv2.imwrite(f"tests/slots/images/slots.jpg", self.image)
                break
        cv2.destroyAllWindows()
        return self.coordinates_

    # mouse callback function
    def handle_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.coordinates.append([x, y])
            self.click_count += 1
            if self.click_count >= 4:
                self.handle_done()
            elif self.click_count > 1:
                self.handle_click_progressing()
        cv2.imshow(self.caption, self.image)

    def handle_click_progressing(self):
        # draw line for last 2 coordinate entries
        cv2.line(self.image, self.coordinates[-2],
                 self.coordinates[-1], self.color, 2)

    def handle_done(self) -> list:
        # draw lines from the third(index 2) coordinate to the last(index 3) and from the first(index 0) to the last(index 3)
        cv2.line(self.image, self.coordinates[2],
                 self.coordinates[3], self.color, 2)
        cv2.line(self.image, self.coordinates[3],
                 self.coordinates[0], self.color, 2)
        # reset click count
        self.click_count = 0
        coordinates = np.array(self.coordinates)
        self.output_file.write("-\n          id: " + str(self.ids) + "\n          coordinates: [" +
                               "[" + str(self.coordinates[0][0]) + "," + str(self.coordinates[0][1]) + "]," +
                               "[" + str(self.coordinates[1][0]) + "," + str(self.coordinates[1][1]) + "]," +
                               "[" + str(self.coordinates[2][0]) + "," + str(self.coordinates[2][1]) + "]," +
                               "[" + str(self.coordinates[3][0]) + "," + str(self.coordinates[3][1]) + "]]\n")
        # append coordinates to the coordinates_ list
        self.coordinates_.append(coordinates.tolist())
        draw_contours(self.image, coordinates, f"SLOT{self.ids}", COL_WHITE)
        # reset coordinates
        for i in range(len(self.coordinates)):
            self.coordinates.pop()
        self.ids += 1


"""
    def store_slots(self, coordinates, file_):
        '''
        # json template of how i want to store slot data
        slots = {
            1: {
                "id": "slot1",
                "coordinates": [[], [], [], []]
            },
            2: {
                "id": "slot2",
                "coordinates": [[], [], [], []]
            }
        }
        '''
        slots = dict()
        for i, cord in enumerate(coordinates):
            slots[i] = {
                "id": i,
                "coordinates": cord
            }

        with open(file_, 'w') as f:
            json.dump(slots, f)
        file_.close()
"""
