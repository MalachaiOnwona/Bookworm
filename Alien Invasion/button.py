import pygame.font

class Button():

    def __init__(self, settings, window, message):
        self.window = window
        self.window_rectangle = window.get_rect()
        
        self.width, self.height = 200,50
        self.color = (255, 0, 0)
        self.message_color = (255,255,255)
        self.message_font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.window_rectangle.center

        self.prep_message(message)

    def prep_message(self, message):
        self.image = self.message_font.render(message, True, self.message_color, self.color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center
    
    def draw_button(self):
        self.window.fill(self.color, self.rect)
        self.window.blit(self.image, self.image_rect)