import pygame
from text import Text

class Nfloor_square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((5, 5, 5))
        self.rect=self.image.get_rect(center=(935,810))
        self.text=Text()

    def player_in(self,player,display,button_press):
        if self.rect.right>player.rect.centerx>self.rect.left :
            if self.rect.bottom>player.rect.centery>self.rect.top:
                display_xy=display.get_size()
                self.text.render(display,(f"press space to move to next floor"),display_xy[0],display_xy[1]/8,20,(30,30,30))
                if button_press==pygame.K_SPACE:
                    return True