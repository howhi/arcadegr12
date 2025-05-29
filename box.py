import arcade

# Screen & box constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BOX_SIZE = 50
MOVEMENT_SPEED = 10

#Main Window class
class BoxWindow(arcade.Window):
    #Initialize the window with size and title
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Move the Box")
        #Set initial box position at centre of screen
        self.box_x = SCREEN_WIDTH // 2
        self.box_y = SCREEN_HEIGHT // 2

    #Draw everything
    def on_draw(self):
        #Clear screen
        self.clear()
        #Draw box using size and color values using draw function from arcade package
        arcade.draw_lrbt_rectangle_filled(
            left = self.box_x - BOX_SIZE / 2,
            right = self.box_x + BOX_SIZE / 2,
            bottom = self.box_y - BOX_SIZE / 2,
            top = self.box_y + BOX_SIZE / 2,
            color = arcade.color.BLUE
        )

    def on_key_press(self, key, modifiers):
        #Method to move pacman sprite using arrow keys
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
    #Launch a game window from the PacWindow class
    window = BoxWindow()
    #Start Arcade game loop
    arcade.run()

#Run program
if __name__ == "__main__":
    main()