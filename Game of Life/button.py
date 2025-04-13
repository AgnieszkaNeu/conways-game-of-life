import pygame

class ButtonImage:
    def __init__ (self,image, left, top, scale, state = ""):
        self.left = left
        self.top = top
        self.state = state
        self.scale = scale
        self.set_image(image)


    def draw_button(self,screen):
        screen.blit(self.image, (self.left, self.top))


    def set_image(self,image):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.x += self.left
        self.rect.y += self.top


    def set_state(self, state, image=None):
        self.state = state
        if image: self.set_image(image)
