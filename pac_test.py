import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10

class PacWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Collision Sprite Test")
        self.sprite_list = arcade.SpriteList()

        self.pacman = arcade.Sprite("Pacman_OG-removebg-preview.png", scale = 0.5)
        self.pacman.center_x = SCREEN_WIDTH // 2
        self.pacman.center_y = SCREEN_HEIGHT // 2
        self.sprite_list.append(self.pacman)

        self.ball = arcade.Sprite("ball.png", scale = 0.15)
        self.reset_ball()
        self.sprite_list.append(self.ball)

        self.score = 0

    def reset_ball(self):
        self.ball.center_x = random.randint(0, SCREEN_WIDTH)
        self.ball.center_y = random.randint(0, SCREEN_HEIGHT)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        arcade.draw_text(f"{self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
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
        if arcade.check_for_collision(self.pacman, self.ball):
            self.score += 1
            self.reset_ball()

def main():
    window = PacWindow()
    arcade.run()


if __name__ == "__main__":
    main()