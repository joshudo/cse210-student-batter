import random
from game import constants
from game.action import Action
from game.point import Point
import sys

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        
        self.score = 0


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        # marquee.set_text("")
        for brick in bricks:
            new_velocity = ball.get_velocity()
            if ball.get_position().equals(brick.get_position()):

                if brick.get_text() != ' ':
                    ball.set_velocity(new_velocity.reverse())
                    brick.set_text(' ')
                    self.score += 1
               
        x = paddle.get_position().get_x()
        y = paddle.get_position().get_y()
        for _ in range(11):
            new_position = Point(x, y)
            if ball.get_position().equals(new_position):
                ball.set_velocity(new_velocity.reverse())
            x += 1

       
        for i in range(constants.MAX_Y):
            left = Point(constants.MAX_X - 1,i)
            right = Point(1,i)

            if ball.get_position().equals(right) or ball.get_position().equals(left):
                ball.set_velocity(new_velocity.reverse(True))

         
        for i in range(constants.MAX_X):
            top = Point(i,1)
            bottom = Point(i,constants.MAX_Y - 1)
            if ball.get_position().equals(top):
                ball.set_velocity(new_velocity.reverse())
            elif ball.get_position().equals(bottom):
                self.score = str(self.score)
                
                sys.exit(f'Game Over \nScore: {self.score}')

