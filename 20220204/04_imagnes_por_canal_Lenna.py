#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import cv2 as cv
import numpy as np

img = cv.imread("lenna.jpg")

# Separar los canales en RGB
b,g,r = cv.split(img)
zeros = np.zeros(b.shape, dtype=np.uint8)

cv.imshow("Lenna", img)
cv.imshow("Zeros", zeros)
cv.imshow("Rojo", r)
cv.imshow("Verde", g)
cv.imshow("Azul", b)

while True:
    k = cv.waitKey(0)
    if k == 27: # 27 es el escape (ESC)
        break
cv.destroyAllWindows()
