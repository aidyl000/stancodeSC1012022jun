"""
File: draw_line.py
Name: Lydia
-------------------------
This program creates lines on GWindow class. At odd times of user's click,  it draws a circle.
At even times of user's click, the circle disappears and a line appears.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# global variables
SIZE = 10  # the diameter of circle
window = GWindow(width=850, height=550)  # create a canva
circle = GOval(SIZE, SIZE)  # create a circle at radius of SIZE


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_circle)


def draw_circle(mouse):
    """
    This function draws a circle on the canva and the center of circle is the place of mouse click
    """
    window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)  # a circle added to the canva
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    This computes to remove the circle and draw a line.
    """
    window.remove(circle)  # the circle will disappear
    # draws a line from the center of circle to the place of mouse click
    line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, mouse.x, mouse.y)
    window.add(line)  # a line added to the canva
    onmouseclicked(draw_circle)  # draws a circle again when the mouse clicks


if __name__ == "__main__":
    main()
