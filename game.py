import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10

class PacWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Collision Sprite Test")
        self.sprite_list = arcade.SpriteList()

        #Initialize Pacman sprite image
        self.pacman = arcade.Sprite("Pacman_Open_OG-removebg-preview.png", scale = 0.5)
        self.pacman.center_x = SCREEN_WIDTH // 2
        self.pacman.center_y = SCREEN_HEIGHT // 2

        #Load both textures for animation
        self.pacman.textures.append(arcade.load_texture("Pac_Closed-removebg-preview.png"))
        self.pacman.textures.append(arcade.load_texture("Pacman_Open_OG-removebg-preview.png"))
        
        self.current_texture_index = 0
        self.animation_timer = 0

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
        self.animation_timer += delta_time
        if self.animation_timer > 0.2:
            self.animation_timer = 0
            self.current_texture_index = (self.current_texture_index + 1) % 2
            self.pacman.texture = self.pacman.textures[self.current_texture_index]

        if arcade.check_for_collision(self.pacman, self.ball):
            self.score += 1
            self.reset_ball()

def main():
    window = PacWindow()
    arcade.run()


if __name__ == "__main__":
    main()