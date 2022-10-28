"""
File: bouncing_ball.py
Name: Lydia
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
DELAY = 25
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0  # to count how many times the ball bounces far than window.width


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(fall)


def fall(mouse):
    global GRAVITY, count
    ball.dy = 0  # initial vertical velocity
    while True:
        onmouseclicked(no_action)  # when ball is bouncing, make mouse click no effect
        ball.dy += GRAVITY  # vertical velocity gets faster after each bounce
        ball.move(VX, ball.dy)
        if ball.y+SIZE >= window.height:  # when ball bounces, vertical velocity has only 90% left at each bounce
            if ball.dy > 0:
                ball.dy *= -REDUCE
        if ball.x > window.width:  # when ball bounces far than window.width, it gets back to the initial place.
            count += 1  # to count how many times the ball bounces far than window.width
            window.add(ball, x=START_X, y=START_Y)
            break
        pause(DELAY)
    onmouseclicked(fall)  # ball starts to fall again when mouse clicks
    if count == 3:  # to check if ball bounces far than window.width for 3 times
        onmouseclicked(no_action)  # if so, make mouse click no effect and unable to make ball fall


def no_action(mouse):
    pass


if __name__ == "__main__":
    main()
