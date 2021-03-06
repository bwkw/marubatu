import numpy as np
import random

train_images = np.zeros((60000, 28, 28), dtype=np.float64)
train_labels = np.zeros(60000, dtype=np.uint8)

def circle(img):
    r = random.randint(5, 12)
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    for ix in range(28):
        for iy in range(28):
            x = ix - 14 + dx
            y = iy - 14 + dy
            r_2 = x**2 + y**2
            if (r_2 > r**2) and (r_2 < (r+2)**2):
                img[ix][iy] = 1
    return img

def cross(img):
    r = random.randint(5,12)
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    ce_x = 14 + dx
    ce_y = 14 + dy
    x = ce_x - r
    xx = ce_x + r
    y = ce_y - r
    for i in range(2*r+1):
        x1 = x + i
        y1 = y + i
        x2 = xx - i
        y2 = y + i
        if (x1 < 28) and (y1 <28):
            img[x1][y1] = 1
        if (x2 < 28) and (y2 <28):
            img[x2][y2] = 1
    return img

for i in range(60000):
    tr_label = random.randint(0, 1)
    train_labels[i] = tr_label
    if tr_label == 0:
        circle(train_images[i])
    else:
        cross(train_images[i])

test_images = np.zeros((10000, 28, 28), dtype=np.float64)
test_labels = np.zeros(10000, dtype=np.uint8)

for i in range(10000):
    te_label = random.randint(0, 1)
    test_labels[i] = te_label
    if te_label == 0:
        circle(test_images[i])
    else:
        cross(test_images[i])


np.save('train_images',train_images)
np.save('train_labels',train_labels)
np.save('test_images',test_images)
np.save('test_labels',test_labels)
