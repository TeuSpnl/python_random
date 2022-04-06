from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
    )
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0) #Sets the initial velocity to x axis
    velocity_y = NumericProperty(0) #Sets the initial velocity to y axis

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    
    # Gives a initial movement to the ball
    def serve_ball(self):
        self.ball.center = self.center # The ball starts in the center of the game
        self.ball.velocity = Vector(4,0).rotate(randint(0, 360)) #Tha ball moves to a random angle

    def update(self, dt):
        self.ball.move()

        # Bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Bounce off right and left
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
            
        #To hook it up, we need to give the child an id and git the ball property to this id on the kv file
        
        def on_touch_move(self, touch):
            if touch.x < self.width/3:
                self.player1.center_y = touch.y
            if touch.x > self.width - self.width/3:
                self.player2.center_y = touch.y
                
class PongPaddle(Widget):
    score = NumericProperty(0)
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vy, vx = ball.velocity
            speedup = 1.1
            offset = 0.02 * Vector(0, ball.center_y - self.center_y)
            ball.velocity = speedup * (offset - ball.velocity)


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)  # Sets the FPS to 60

        return game


if __name__ == '__main__':
    PongApp().run()
