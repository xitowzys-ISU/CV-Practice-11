import matplotlib.pyplot as plt
import numpy as np
from skimage import color

def det_color(hsv):
    # means = {}
    # for i in np.unique(hsv[:, :, 0]):
    #     tmp = hsv[np.where(hsv[:, :, 0] == i)]
    #     means[i] = (np.mean(tmp[:, :, 1]), np.mean(tmp[:, :, 2]))

    unique_color = np.unique(hsv[:, :, 0])
    colors = []
    prev_color = -1
    a = []

    for i in unique_color:
        if prev_color == -1:
            a.append(i)
        elif np.abs(i - prev_color) >= 0.02:
            colors.append(np.mean(a))
            a = [i]
        else:
            a.append(i)
        prev_color = i

    colors.append(np.mean(a))

    return colors

image = plt.imread("./data/balls.png")

image = color.rgb2hsv(image)

print(det_color(image))

plt.figure()
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.plot(np.unique(image[:, :, 0]), 'o')
plt.show()
