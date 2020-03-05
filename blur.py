#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：lowkeyway time:8/1/2019

import sys
import cv2 as cv


def main_func(argv):
    
    imgOri = cv.imread("desk.png")
    
    cv.namedWindow("imgOri", cv.WINDOW_NORMAL)
    cv.imshow("imgOri", imgOri)


    imgOut = cv.blur(imgOri, (20, 20))
    
    cv.namedWindow("imgOut", cv.WINDOW_NORMAL)
    cv.imshow("imgOut", imgOut)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main_func(sys.argv)
    