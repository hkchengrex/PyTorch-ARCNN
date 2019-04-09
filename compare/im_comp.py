import sys
import cv2

im = cv2.imread(sys.argv[1]).astype(float)
gt = cv2.imread(sys.argv[2]).astype(float)

print('Bias', (im-gt).sum())
print('Mean L1 error', abs(im-gt).mean())
print('Max L1 error', abs(im-gt).max())

