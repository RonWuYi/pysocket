
import time
from pynput.mouse import Button, Controller
# from pynput.keyboard import Keyboard

mouse = Controller()
while True:
    try:
        # Read pointer position
        print 'The current pointer position is {0}'.format(mouse.position)
        mouse.click(Button.left, 2)
        time.sleep(2)
        # # Press and release
        mouse.press(Button.left)
        mouse.release(Button.left)
    except KeyboardInterrupt:
        print('The keyboard interrupt')
        break

# # Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# # Move pointer relative to current position
# mouse.move(5, -5)

# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)

# # Scroll two steps down
# mouse.scroll(0, 2)