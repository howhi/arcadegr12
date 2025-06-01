import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

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
        self.sprite_list.append(self.ball)
        self.reset_ball()

        self.score = 0

        #Track keys pressed
        self.keys_held = set()

    def reset_ball(self):
        self.ball.center_x = random.randint(0, SCREEN_WIDTH)
        self.ball.center_y = random.randint(0, SCREEN_HEIGHT)

        speed = 2
        self.ball.change_x = speed * random.choice([-1, 1])
        self.ball.change_y = speed * random.choice([-1, 1])

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        arcade.draw_text(f"{self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        self.keys_held.add(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_held:
            self.keys_held.remove(key)
    
    def on_update(self, delta_time):
        self.ball.center_x += self.ball.change_x
        self.ball.center_y += self.ball.change_y

        if self.ball.left < 0 or self.ball.right > SCREEN_WIDTH:
            self.ball.change_x *= -1
        
        if self.ball.bottom < 0 or self.ball.top > SCREEN_HEIGHT:
            self.ball.change_y *= -1

        self.animation_timer += delta_time
        if self.animation_timer > 0.2:
            self.animation_timer = 0
            self.current_texture_index = (self.current_texture_index + 1) % 2
            self.pacman.texture = self.pacman.textures[self.current_texture_index]
        
        if self.pacman:
            if arcade.key.UP in self.keys_held:
                self.pacman.center_y += MOVEMENT_SPEED
                #Check top boundary
                if self.pacman.top > SCREEN_HEIGHT:
                    self.pacman.top = SCREEN_HEIGHT
            elif arcade.key.DOWN in self.keys_held:
                self.pacman.center_y -= MOVEMENT_SPEED
                #Check bottom boundary
                if self.pacman.bottom < 0:
                    self.pacman.bottom = 0
            elif arcade.key.LEFT in self.keys_held:
                self.pacman.center_x -= MOVEMENT_SPEED
                #Check left boundary
                if self.pacman.left < 0:
                    self.pacman.left = 0
            elif arcade.key.RIGHT in self.keys_held:
                self.pacman.center_x += MOVEMENT_SPEED
                #Check right boundary
                if self.pacman.right > SCREEN_WIDTH:
                    self.pacman.right = SCREEN_WIDTH

        if arcade.check_for_collision(self.pacman, self.ball):
            self.score += 1
            self.reset_ball()

def main():
    window = PacWindow()
    arcade.run()


if __name__ == "__main__":
    main()