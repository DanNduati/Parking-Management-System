from cProfile import label
import cv2
from colours import COL_BLUE


def draw_contours(image, coordinates, label, font_color, b_color=COL_BLUE, line_thickness=2, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5):
    cv2.drawContours(image, [coordinates], contourIdx=-1,
                     color=b_color, thickness=2, lineType=cv2.LINE_8)

    # *Todo*: get center of parking slot rectangle and add slot labels
    M = cv2.moments(coordinates)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    # label at center of the rectangle
    cv2.putText(image, label, center, font, font_scale,
                font_color, line_thickness, cv2.LINE_AA)
