"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

To create a Breakout clone game from class Breakoutgraphics
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20       # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    count = 0  # to count how many times ball died
    # Add the animation loop here!
    while True:
        if graphics.start:  # drop the ball when mouse clicks
            graphics.set_ball_velocity()
            while count < NUM_LIVES and graphics.start:
                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                pause(FRAME_RATE)
                # when ball bumped into bricks
                graphics.remove_brick()
                # when ball bumped into walls
                graphics.bounce_from_wall()
                # when ball bumped into paddle
                graphics.bounce_from_paddle()
                # when all bricks are gone
                if graphics.brick_count():
                    break
                # when ball falls underneath the bottom
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.window.remove(graphics.ball)
                    count += 1
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball_radius) / 2,
                                        y=(graphics.window.height - graphics.ball_radius) / 2)
                    graphics.start = False
                    break
        if graphics.brick_count():
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
