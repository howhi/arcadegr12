import arcade
import random

#Screen size and movement speed constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

#Main Window Class
class PacWindow(arcade.Window):
    #Initialize window
    def __init__(self):

        #Initialize window settings and sprite list
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Connor Ho's Pacman")
        self.sprite_list = arcade.SpriteList()

        #Initialize Pacman sprite image with open-mouth png
        self.pacman = arcade.Sprite("Pacman_Open_OG-removebg-preview.png", scale = 0.5)
        
        #Place pacman at centre of screen
        self.pacman.center_x = SCREEN_WIDTH // 2
        self.pacman.center_y = SCREEN_HEIGHT // 2

        #Load both textures/images for pacman animation
        self.pacman.textures.append(arcade.load_texture("Pac_Closed-removebg-preview.png"))
        self.pacman.textures.append(arcade.load_texture("Pacman_Open_OG-removebg-preview.png"))
        
        #Start pacman texture at first picture (index = 0)
        self.pac_current_texture_index = 0

        #Initialize timer to control animation of pacman
        self.animation_timer = 0

        #Add pacman sprite to sprite list
        self.sprite_list.append(self.pacman)

        #Initialize ball sprite image and ball speed, append to sprite list and reset ball
        self.ball = arcade.Sprite("ball.png", scale = 0.15)
        self.ball_speed = 2
        self.sprite_list.append(self.ball)
        self.reset_ball()

        #Initialize ghost sprite
        self.ghost = arcade.Sprite("Red_Ghost-removebg-preview (1).png", scale = 0.5)

        #Load textures textures/images for ghost animation
        self.ghost.textures.append(arcade.load_texture("Red_Ghost-removebg-preview (2).png"))
        self.ghost.textures.append(arcade.load_texture("Red_Ghost-removebg-preview (3).png"))
        self.ghost.textures.append(arcade.load_texture("Red_Ghost-removebg-preview (4).png"))
        self.ghost.textures.append(arcade.load_texture("Red_Ghost-removebg-preview (1).png"))
        
        #Start ghost texture at first picture (index = 0)
        self.ghost_current_texture_index = 0

        #Add ghost to sprite list
        self.sprite_list.append(self.ghost)
        
        #Spawn ghost with a speed of 1
        self.spawn_ghost()
        self.ghost_speed = 1

        #Initialize score and level to 0
        self.score = 0
        self.last_level = 0

        #Track keys pressed
        self.keys_held = set()

    
    def spawn_ghost(self):
        #Place ghost randomly on screen but not at the same place as Pacman
        while True:
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)

            self.ghost.center_x = x
            self.ghost.center_y = y

            if not arcade.check_for_collision(self.pacman, self.ghost):
                break

    def reset_ball(self):
        #Place ball randomly and give it a random direction
        self.ball.center_x = random.randint(0, SCREEN_WIDTH)
        self.ball.center_y = random.randint(0, SCREEN_HEIGHT)

        self.ball.change_x = self.ball_speed * random.choice([-1, 1])
        self.ball.change_y = self.ball_speed * random.choice([-1, 1])

    def on_draw(self):
        #Clear screen and draw all sprites and score
        self.clear()
        self.sprite_list.draw()
        arcade.draw_text(f"{self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        #Add pressed key to set of held keys
        self.keys_held.add(key)

    def on_key_release(self, key, modifiers):
        #Remove pressed key to set of held keys
        if key in self.keys_held:
            self.keys_held.remove(key)
    
    def on_update(self, delta_time):
        #Update ball movement
        self.ball.center_x += self.ball.change_x
        self.ball.center_y += self.ball.change_y

        #Bounce ball off walls
        if self.ball.left < 0 or self.ball.right > SCREEN_WIDTH:
            self.ball.change_x *= -1
        if self.ball.bottom < 0 or self.ball.top > SCREEN_HEIGHT:
            self.ball.change_y *= -1

        #Add time since last frame to animation timer
        self.animation_timer += delta_time

        #Update animations every 0.2 seconds (change to next index)
        if self.animation_timer > 0.2:
            self.animation_timer = 0
            self.pac_current_texture_index = (self.pac_current_texture_index + 1) % 2
            self.pacman.texture = self.pacman.textures[self.pac_current_texture_index]
            self.ghost_current_texture_index = (self.ghost_current_texture_index + 1) % 4
            self.ghost.texture = self.ghost.textures[self.ghost_current_texture_index]
        
        #Move Pacman with key presses and ensure screen boundaries
        if self.pacman:
            if arcade.key.UP in self.keys_held:
                self.pacman.center_y += MOVEMENT_SPEED
                #Check top boundary
                if self.pacman.top > SCREEN_HEIGHT:
                    self.pacman.top = SCREEN_HEIGHT
            if arcade.key.DOWN in self.keys_held:
                self.pacman.center_y -= MOVEMENT_SPEED
                #Check bottom boundary
                if self.pacman.bottom < 0:
                    self.pacman.bottom = 0
            if arcade.key.LEFT in self.keys_held:
                self.pacman.center_x -= MOVEMENT_SPEED
                #Check left boundary
                if self.pacman.left < 0:
                    self.pacman.left = 0
            if arcade.key.RIGHT in self.keys_held:
                self.pacman.center_x += MOVEMENT_SPEED
                #Check right boundary
                if self.pacman.right > SCREEN_WIDTH:
                    self.pacman.right = SCREEN_WIDTH
        
        #Move ghost toward Pacman constantly (i.e. "chasing" it)
        dx = self.pacman.center_x - self.ghost.center_x
        dy = self.pacman.center_y - self.ghost.center_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        #Move ghost toward Pacman by normalizing direction vector (dx, dy) and scaling it by ghost speed
        if distance > 0:
            self.ghost.center_x += (dx / distance) * self.ghost_speed
            self.ghost.center_y += (dy / distance) * self.ghost_speed
            
            #Keep ghost within screen boundaries
            if self.ghost.top > SCREEN_HEIGHT:
                self.ghost.top = SCREEN_HEIGHT
            if self.ghost.bottom < 0:
                self.ghost.bottom = 0
            if self.ghost.left < 0:
                self.ghost.left = 0
            if self.ghost.right > SCREEN_WIDTH:
                self.ghost.right = SCREEN_WIDTH

        #Ball collision: increment score and reset ball
        if arcade.check_for_collision(self.pacman, self.ball):
            self.score += 1
            self.reset_ball()

        #Ghost collision: decrement score and respawn ghost
        if arcade.check_for_collision(self.pacman, self.ghost):
            self.score -= 1
            self.spawn_ghost()

        #Level up: increase balla nd ghost speed
        new_level = self.score // 5
        if new_level != self.last_level:
            level_diff = new_level - self.last_level
            self.ball_speed += level_diff
            self.ball_speed = max(1, self.ball_speed)
            self.ghost_speed += 0.2 * level_diff
            self.ghost_speed = max(1, min(self.ghost_speed, 4.8))
            self.last_level = new_level

#Start the game
def main():
    #Launch a game window from the PacWindow class
    window = PacWindow()

    #Start Arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()