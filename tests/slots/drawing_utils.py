import cv2
from colours import COL_BLUE


def draw_contours(image, coordinates, b_color=COL_BLUE, line_thickness=2, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5):
    cv2.drawContours(image, [coordinates], contourIdx=-1,
                     color=b_color, thickness=2, lineType=cv2.LINE_8)

    # *Todo*: get center of parking slot rectangle and add slot labels
