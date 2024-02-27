import pygame
import random
from text import Text
import time
class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.potion=Potion()
        self.potion_stock=random.randint(1,2)
        self.dmg_potion=Dmg_potion()
        self.dmg_potion_stock=random.randint(1,3)
        self.random_potion=Random_potion()
        self.random_potion_stock=1
        self.door=Door_out()
        self.text=Text()
        
    def draw_to_surface(self,draw_surface):
            draw_surface.blit(self.potion.image,(self.potion.rect.x,self.potion.rect.y))
            draw_surface.blit(self.dmg_potion.image,(self.dmg_potion.rect.x,self.dmg_potion.rect.y))
            draw_surface.blit(self.random_potion.image,(self.random_potion.rect.x,self.random_potion.rect.y))
            draw_surface.blit(self.door.image,(self.door.rect.x,self.door.rect.y))
        #if game+loop_return==buff_choose then buff screen will take palce
    def player_in_door(self,player,display,button_press):
        if self.door.rect.right>player.rect.centerx>self.door.rect.left :
            if self.door.rect.bottom>player.rect.centery>self.door.rect.top:
                display_xy=display.get_size()
                self.text.render(display,(f"press space to leave shop"),display_xy[0],display_xy[1]/8,20,(30,30,30))
                if button_press==pygame.K_SPACE:
                    return True
    def player_in_items(self,player,display,button_press,gold):
        if self.player_in_item(player,display,button_press,self.potion,self.potion.info+":stock "+str(self.potion_stock)) and self.potion_stock>0 and gold>self.potion.cost:
            self.potion_stock-=1
            time.sleep(0.5)
            return self.potion.code
        elif self.player_in_item(player,display,button_press,self.dmg_potion,self.dmg_potion.info+":stock "+str(self.dmg_potion_stock)) and self.dmg_potion_stock>0 and gold>self.dmg_potion.cost:
            self.dmg_potion_stock-=1
            time.sleep(0.5)
            return self.dmg_potion.code
        elif self.player_in_item(player,display,button_press,self.random_potion,self.random_potion.info+":stock "+str(self.random_potion_stock)) and self.random_potion_stock>0 and gold>self.random_potion.cost:
            self.random_potion_stock-=1
            time.sleep(0.5)
            return self.random_potion.code
    
    def player_in_item(self,player,display,button_press,item,info):
        if item.rect.right>player.rect.centerx>item.rect.left :
            if item.rect.bottom>player.rect.centery>item.rect.top:
                display_xy=display.get_size()
                self.text.render(display,(info),display_xy[0],display_xy[1]/8,20,(30,30,30))
                if button_press==pygame.K_SPACE:
                    return True
        
class Shop_item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((90, 255, 90))
        self.rect=self.image.get_rect(center=(935,1010))
        self.text=Text()

class Door_out(Shop_item):
    def __init__(self):
        super().__init__()
        self.rect=self.image.get_rect(center=(935,510))
        self.image.fill((87,12,42))
class Potion(Shop_item):
    def __init__(self):
        super().__init__()
        self.rect=self.image.get_rect(center=(935-100,1010))
        self.code="player.hp_bar.current_hp+=50\nplayer.gold-=40"
        self.info="hp potion:increase hp by 50:cost 40:press space to buy"
        self.cost=40
        self.image.fill((240,50,50))
class Dmg_potion(Shop_item):
    def __init__(self):
        super().__init__()
        self.rect=self.image.get_rect(center=(935,1010))
        self.code="player.damage+=1\nplayer.gold-=30"
        self.info="hp potion:increase dmg by 1:cost 30:press space to buy"
        self.cost=30
        self.image.fill((150,50,150))
class Random_potion(Shop_item):
    def __init__(self):
        super().__init__()
        self.rect=self.image.get_rect(center=(935+100,1010))
        self.code="buff"
        self.info="hp potion:random buff:cost 50:press space to buy"
        self.cost=50
        self.image.fill((10,10,10))
