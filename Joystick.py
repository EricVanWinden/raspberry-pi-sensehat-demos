from sense_hat import SenseHat

# initialize
sense = SenseHat()
x = 4
y = 4
color = [255, 255, 255]
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
sense.set_pixel(x, y, color)

print("Use joystick to move the dot. Press Ctrl-C to exit")
try:
    while True:
        for event in sense.stick.get_events():
            if (event.action == 'pressed') | (event.action == 'held'):
                if event.direction == 'up':
                    if y > 0:
                        y -= 1
                        color = [0, 255, 0]
                    else:
                        color = [255, 0, 0]

                if event.direction == 'down':
                    if y < 7:
                        y += 1
                        color = [0, 255, 0]
                    else:
                        color = [255, 0, 0]

                if event.direction == 'left':
                    if x > 0:
                        x -= 1
                        color = [0, 255, 0]
                    else:
                        color = [255, 0, 0]

                if event.direction == 'right':
                    if x < 7:
                        x += 1
                        color = [0, 255, 0]
                    else:
                        color = [255, 0, 0]

            if event.action == 'released':
                color = [255, 255, 255]

            print(str(event.action) + " " + str(event.direction) + " " + str(x) + " " + str(y))
            sense.set_pixels(pixels_off)
            sense.set_pixel(x, y, color)

except KeyboardInterrupt:
    sense.set_pixels(pixels_off)
    print("Joystick demo stopped")
