"""
File: my_drawing.py
Name: Lydia
----------------------
Draw Kaonashi(No-Face), a character in Spirited Away
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(1000, 1000)

# global variables
SIZE = 50  # the diameter of circle
circle = GOval(SIZE, SIZE)  # create a circle at radius of SIZE


def main():
    """
    Title: No-Face
    No-Face symbolizes those human beings who have ever been lost in their life.
    """
    left_eyebrow = GOval(20, 35, x=330, y=150)
    left_eyebrow.filled = True
    left_eyebrow.color = 'purple'
    left_eyebrow.fill_color = 'purple'
    left_eye = GOval(60, 40, x=310, y=190)
    left_eye.filled = True
    left_eye.color = 'black'
    left_eye.fill_color = 'black'
    right_eye = GOval(60, 40, x=430, y=190)
    right_eye.filled = True
    right_eye.color = 'black'
    right_eye.fill_color = 'black'
    right_eyebrow = GOval(20, 35, x=452, y=150)
    right_eyebrow.filled = True
    right_eyebrow.color = 'purple'
    right_eyebrow.fill_color = 'purple'
    right_darkcircle = GOval(40, 6, x=440, y=235)
    right_darkcircle.filled = True
    right_darkcircle.color = 'black'
    right_darkcircle.fill_color = 'black'
    left_darkcircle = GOval(40, 6, x=320, y=235)
    left_darkcircle.filled = True
    left_darkcircle.color = 'black'
    left_darkcircle.fill_color = 'black'
    left_cheek = GRect(13, 48, x=333, y=250)
    left_cheek.filled = True
    left_cheek.color = 'purple'
    left_cheek.fill_color = 'purple'
    right_cheek = GRect(13, 48, x=455, y=250)
    right_cheek.filled = True
    right_cheek.color = 'purple'
    right_cheek.fill_color = 'purple'
    mouth = GOval(70, 20, x=365, y=305)
    mouth.filled = True
    mouth.color = 'black'
    mouth.fill_color = 'black'
    jaw = GOval(30, 6, x=385, y=330)
    jaw.filled = True
    jaw.color = 'purple'
    jaw.fill_color = 'purple'
    body = GOval(350, 1000, x=225, y=60)
    body.filled = True
    body.color = 'black'
    body.fill_color = 'black'
    window.add(body)
    face = GOval(200, 250, x=300, y=100)
    face.filled = True
    face.color = 'white'
    face.fill_color = 'white'
    window.add(face)
    window.add(left_eye)
    window.add(right_eye)
    window.add(right_darkcircle)
    window.add(left_darkcircle)
    window.add(mouth)
    window.add(jaw)
    window.add(left_eyebrow)
    window.add(right_eyebrow)
    window.add(left_cheek)
    window.add(right_cheek)

    board = GRect(200, 100, x=300, y=400)
    board.filled = True
    board.color = 'black'
    board.fill_color = 'white'
    window.add(board)
    number = GLabel('SC101-0717', x=335, y=440)
    number.font = '-20'
    window.add(number)
    name = GLabel('No-Face', x=340, y=490)
    name.font = '-30'
    window.add(name)

    line2 = GLine(580, 330, 690, 200)
    window.add(line2)
    label = GLabel('不可以吃太胖，否則會被殺掉喔！', x=590, y=190)
    label.font = '-20'
    window.add(label)
    onmouseclicked(draw_circle)


def draw_circle(mouse):
    """
    This function draws a circle on the canva and the center of circle is the place of mouse click
    """
    circle.color = 'gold'
    circle.filled = True
    circle.fill_color = 'gold'
    window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)  # a circle added to the canva
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    This draws a line  from the place of mouse click to the circle
    """
    line = GLine(mouse.x, mouse.y, circle.x+SIZE/2, circle.y+SIZE/2)
    line.color = 'gold'
    window.add(line)  # a line added to the canva


if __name__ == '__main__':
    main()
