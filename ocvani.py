import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)


def f(cap):
    ret, frame = cap.read()
    return frame

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
cap = cv2.VideoCapture(r'bowling 013.avi')
ims = []

for i in range(60):
    im = ax2.imshow(f(cap), animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat = False)
                                #repeat_delay=1000)

#ani.save('dynamic_images.mp4')


plt.show()
cap.release()
