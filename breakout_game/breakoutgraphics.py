"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

To write a class to create a Breakout clone game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.count = 0  # to count how many bricks have been removed

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width-paddle_width)/2, y=self.window.height-paddle_offset)
        self.paddle_offset = paddle_offset
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(width=ball_radius, height=ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width - ball_radius) / 2, y=(self.window.height - ball_radius) / 2)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmouseclicked(self.drop)
        self.start = False  # to be a switch for game start, onmouseclicked will be invalid after start became True
        onmousemoved(self.moving)

        # Draw bricks
        self.brick_offset = brick_offset
        lst = ['red', 'orange', 'yellow', 'green', 'blue']  # for brick colors
        for i in range(brick_cols):
            self.new_y = self.brick_offset + (brick_height + brick_spacing)*i
            self.new_x = 0
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                self.brick.fill_color = lst[i//2]
                self.window.add(self.brick, x=self.new_x, y=self.new_y)
                self.new_x += (brick_width+brick_spacing)

    def moving(self, event):  # for paddle movement
        if event.x+self.paddle.width/2 > self.window.width:  # when mouse goes outside the window at right
            self.paddle.x = self.window.width-self.paddle.width
        elif event.x - self.paddle.width/2 < 0:  # when mouse goes outside the window at left
            self.paddle.x = 0
        else:  # event.x is at the center of paddle
            self.paddle.y = self.window.height-self.paddle_offset
            self.paddle.x = event.x - self.paddle.width / 2

    def drop(self, event):  # ball falls when mouse clicks
        self.start = True

    def get_dx(self):  # getter function for speed dx
        return self.__dx

    def get_dy(self):  # getter function for speed dy
        return self.__dy

    def bounce_from_wall(self):  # when ball bumped into walls
        if self.ball.x <= 0 or self.ball.x+self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def bounce_from_paddle(self):  # when ball bumped into paddle
        if self.ball.y+self.ball.height >= self.paddle.y:
            if self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not None:
                if self.__dy > 0:
                    self.__dy = -self.__dy

    def remove_brick(self):  # when ball bumped into bricks
        if self.ball.y < self.window.height / 2:
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                self.bounce_from_brick()
                self.count += 1  # to count how many bricks have been removed

            elif self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y))
                self.bounce_from_brick()
                self.count += 1

            elif self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius))
                self.bounce_from_brick()
                self.count += 1

            elif self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius))
                self.bounce_from_brick()
                self.count += 1

    def bounce_from_brick(self):  # when ball bumped into walls
        self.__dy = -self.__dy

    def brick_count(self):  # to check if all bricks are removed, if so, the game ends
        if self.count == (self.brick_cols*self.brick_rows):
            win = GLabel('You won!!', x=self.window.width / 2-25,
                         y=self.window.height / 2)
            self.window.add(win)
            return True
        else:
            return False

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED



