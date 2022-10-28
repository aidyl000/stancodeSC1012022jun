"""
File: sierpinski.py
Name: Lydia
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY = 30

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	To create the Sierpinski triangle on GWindow.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: Controls the order of Sierpinski Triangle, how many loops it needs to run
	:param length: The length of the first triangle(order 1 Sierpinski Triangle)
	:param upper_left_x: The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of order 1 Sierpinski Triangle
	:return: nothing
	"""
	if order == 0: # base case
		pass
	else:
		# draw lines
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)  # upper side of triangle
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + length * 1 / 2, upper_left_y + length * 0.866)  # left side of triangle
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 1 / 2, upper_left_y + length * 0.866)  # right side of triangle

		window.add(line1)
		window.add(line2)
		window.add(line3)
		pause(DELAY)

		# recursive, to create triangles in a recursive way
		sierpinski_triangle(order - 1, length*1/2, upper_left_x, upper_left_y)  # left
		sierpinski_triangle(order - 1, length * 1 / 2, upper_left_x + length * 1 / 2, upper_left_y)  # right
		sierpinski_triangle(order - 1, length * 1 / 2, upper_left_x + length * 1 / 4, upper_left_y+ length * 0.866*1/2)  # bottom


if __name__ == '__main__':
	main()