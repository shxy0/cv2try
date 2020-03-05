#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：lowkeyway time:8/1/2019

import sys
import cv2 as cv
import numpy as np

def main_func(argv):
    
    cap = cv.VideoCapture(0)
    
    while (cap.isOpened()):
        ret, frame = cap.read()

        cv.namedWindow("frame", cv.WINDOW_NORMAL)
        cv.imshow("frame", frame)

        key = cv.waitKey(1)
        if key == 27:
            break;
    
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main_func(sys.argv)
    