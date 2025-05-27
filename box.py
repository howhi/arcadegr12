import arcade

# Screen & box constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BOX_SIZE = 50
MOVEMENT_SPEED = 10

#Main Window class
class BoxWindow(arcade.Window):
    def __init__(self):
        #Initialize the window with size and title
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Move the Box")
        #Set initial box position at centre of screen
        self.box_x = SCREEN_WIDTH // 2
        self.box_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        #Clear screen and draw box
        self.clear()
        arcade.draw_lrbt_rectangle_filled(
            left = self.box_x - BOX_SIZE / 2,
            right = self.box_x + BOX_SIZE / 2,
            bottom = self.box_y - BOX_SIZE / 2,
            top = self.box_y + BOX_SIZE / 2,
            color = arcade.color.BLUE
        )

    def on_key_press(self, key, modifiers):
        #Move box according to arrow keys pressed
        if key == arcade.key.UP:
            self.box_y += MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.box_y -= MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.box_x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.box_x += MOVEMENT_SPEED

#Launch window and run main loop
def main():
    window = BoxWindow()
    arcade.run()

#Run program
if __name__ == "__main__":
    main()