import time

import PyQt4.QtGui
import pyautogui


def get_pixel_colour(i_x, i_y):
    global app, long_qdesktop_id
    long_colour = PyQt4.QtGui.QPixmap.grabWindow(long_qdesktop_id, i_x, i_y, 1, 1).toImage().pixel(0, 0)
    i_colour = int(long_colour)
    return ((i_colour >> 16) & 0xff), ((i_colour >> 8) & 0xff), (i_colour & 0xff)


app = PyQt4.QtGui.QApplication([])
long_qdesktop_id = PyQt4.QtGui.QApplication.desktop().winId()
x_start, y_start = 140, 100
last_move = 'right' if str(get_pixel_colour(x_start + 141, y_start + 496)) == '(180, 53, 43)' else 'left'
x_man, y_man = 75 + x_start if last_move == 'left' else 160 + x_start, 445 + y_start
print(last_move)
time.sleep(3)

for _ in range(1000):
    moves = []
    time.sleep(0.18)
    for i in range(0, 251, 50):
        if str(get_pixel_colour(x_man, y_man - i)) == "(153, 204, 102)":
            x_man, last_move = (160 + x_start, 'right') if last_move == 'left' else (75 + x_start, 'left')
        moves.append(last_move)
    set(map(lambda move: pyautogui.press(move, 2, 0.016, 0.0035), moves))
