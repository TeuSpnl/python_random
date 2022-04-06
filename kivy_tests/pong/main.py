from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
import random


class PongGame(Widget):
    ball = ObjectProperty(None)
    p1 = ObjectProperty(None)
    p2 = ObjectProperty(None)

    # Gives a initial movement to the ball
    def serve_ball(self):
        self.ball.center = self.center  # The ball starts in the center of the game
        self.ball.velocity = Vector(randint(5, 10), 0).rotate(
            random.uniform(1, 360))  # The ball moves to a random angle between 0.1 and 360.0

    def update(self, dt):
        self.ball.move()

        # Bounce of paddles
        self.p1.bounce_ball(self.ball)
        self.p2.bounce_ball(self.ball)

        # Bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Score points
        if self.ball.x < self.x - 20:
            self.p2.score += 1
            self.serve_ball()
        if self.ball.right > self.width + 20:
            self.p1.score += 1
            self.serve_ball()

        # To hook it up, we need to give the child an id and give the ball property to this id on the kv file

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.p1.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.p2.center_y = touch.y


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vel_y, vel_x = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vel_x, vel_y)
            vel = bounced
            vel.x = bounced.x * round(random.uniform(0.8, 1.5), 2) # Change the velicity using a range between 0.80 and 1.50
            
            # Limits the ball velocity
            if vel.x > 10:
                vel.x = 10

            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)  # Sets the initial velocity to x axis
    velocity_y = NumericProperty(0)  # Sets the initial velocity to y axis

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)  # Sets the FPS to 60

        return game


if __name__ == '__main__':
    PongApp().run()

# SDG
