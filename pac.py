import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10

class PacWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Collision Sprite Test")
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.pacman = arcade.Sprite("Pacman OG.png", scale = 0.5)
        self.pacman.center_x = 100
        self.pacman.center_y = 300

    def on_draw(self):
        self.clear()
        if self.pacman:
            self.pacman.draw()

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

def main():
    window = PacWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()