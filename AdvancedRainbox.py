from time import sleep
from sense_hat import SenseHat
from ReflectionCurve import *
from IlluminantData import *
from CurveCreator import *
from NumberMatrix import *

# initialize
sense = SenseHat()
d65 = IlluminantData()
matrix = np.array([
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
])

# looping over wavelengths
i = 0
started = False

print("generating all colors of the rainbow. Press Ctrl-C to exit")
try:
    while True:
        index = i
        if (index > 7) | started:
            started = True
            index = 7
            for j in range(7):
                matrix[j] = matrix[j + 1]

        for j in range(8):
            # increasing the band width in every row
            curve = create_curve(d65.count, i, j * 3)
            xyz = ReflectionCurve(curve).get_xyz()
            rgb = xyz.get_rgb()
            matrix[index, j, 0] = rgb.r_norm
            matrix[index, j, 1] = rgb.g_norm
            matrix[index, j, 2] = rgb.b_norm

        print_matrix(matrix)
        pixels = create_pixels(matrix)
        sense.set_pixels(pixels)

        sleep(0.1)
        i += 1
        if i >= 60:
            i = 0

except KeyboardInterrupt:
    off = [0, 0, 0]
    pixels_off = [
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off]
    sense.set_pixels(pixels_off)
    print("Advanced rainbow demo stopped")