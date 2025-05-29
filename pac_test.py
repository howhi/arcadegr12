import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10

class PacWindow(arcade.Window):
    #Initialize window
    def __init__(self):

        #Initialize window settings and sprite list
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Collision Sprite Test")
        self.sprite_list = arcade.SpriteList()

        #Create open-mouth Pacman sprite
        self.pacman = arcade.Sprite("Pacman_OG-removebg-preview.png", scale = 0.5)
        
        #Place pacman at centre of screen
        self.pacman.center_x = SCREEN_WIDTH // 2
        self.pacman.center_y = SCREEN_HEIGHT // 2

        #Add pacman sprite to sprite list
        self.sprite_list.append(self.pacman)

        #Create ball for Pacman to eat
        self.ball = arcade.Sprite("ball.png", scale = 0.15)
        
        #Reset ball
        self.reset_ball()

        #Add ball sprite to sprite list
        self.sprite_list.append(self.ball)

        #Initialize score to 0
        self.score = 0

    #Place ball in random position on screen
    def reset_ball(self):
        self.ball.center_x = random.randint(0, SCREEN_WIDTH)
        self.ball.center_y = random.randint(0, SCREEN_HEIGHT)

    #Draw everything
    def on_draw(self):
        
        #Clear screen
        self.clear()

        #Draw all sprites in sprite list
        self.sprite_list.draw()

        #Place score value in top left corner of screen
        arcade.draw_text(f"{self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        #Method to move pacman sprite
        if self.pacman:
            if key == arcade.key.UP:
                self.pacman.center_y += MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.pacman.center_y -= MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.pacman.center_x -= MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.pacman.center_x += MOVEMENT_SPEED
    

    def on_update(self, delta_time):
        #Check for collision test
        if arcade.check_for_collision(self.pacman, self.ball):
            #Increment score if collision happens
            self.score += 1
            #Reset ball
            self.reset_ball()


def main():
    #Create a game window from the PacWindow class
    window = PacWindow()

    #Start Arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()