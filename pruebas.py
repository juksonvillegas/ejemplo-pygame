import os, sys, pygame, random

class Proyectil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/proyectil.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y += 70
        self.movimiento = 68

    def update(self):
        self.rect.x += 10


class SonicSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/shooter.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.movimiento = 68

    def moveUp(self):
        if self.rect.y > 0:
            self.rect.y -= self.movimiento
        else:
            self.rect.y = 0
    
    def moveDown(self):
        if self.rect.y < 612:
            self.rect.y += self.movimiento
        else:
            self.rect.y = 612
            
    def udpate(self):
        pass

class EnemySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/robot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 1200
        self.movimiento = 68

    def update(self):
        self.rect.x -= 1

def main():
    pygame.init()
    # Cargando el fondo
    bg = pygame.image.load("assets/asphalt.png")
    bg_size = bg.get_size()
    bg_rect = bg.get_rect()
    # tamano y titulo de la ventana
    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size, 0)
    pygame.display.set_caption('Easy Shoot')
    #Sonic como sprite
    sonicSprite = SonicSprite()

    #agregamos un sprite group()
    lista_de_todos_los_sprites = pygame.sprite.Group()
    lista_de_todos_los_sprites.add(sonicSprite)

    #agregamos lista de enemigos
    lista_de_todos_los_enemigos = pygame.sprite.Group()

    for i in range(100):
        enemigo = EnemySprite()
        enemigo.rect.y = (random.randrange(10))*68
        enemigo.rect.x = (random.randrange(20)*68) + 1024
        lista_de_todos_los_enemigos.add(enemigo)
        lista_de_todos_los_sprites.add(enemigo)

    #agregamos lista de proyectiles
    lista_de_todos_los_proyectiles = pygame.sprite.Group()

    #Pintamos el fonto
    pygame.display.flip()

    #puntuacion
    puntuacion = 0
    myFont = pygame.font.SysFont('Comic Sans MS', 40)
    while 1:
        screen.blit(bg, bg_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                if len(lista_de_todos_los_proyectiles.sprites()) < 20:
                    proyectil = Proyectil()
                    proyectil.rect.x = sonicSprite.rect.x
                    proyectil.rect.y = sonicSprite.rect.y
                    lista_de_todos_los_sprites.add(proyectil)
                    lista_de_todos_los_proyectiles.add(proyectil)
            if key[pygame.K_DOWN]:
                sonicSprite.moveDown()
            if key[pygame.K_UP]:
                sonicSprite.moveUp()
        for proyectil in lista_de_todos_los_proyectiles:
            lista_enemigos_alcanzados = pygame.sprite.spritecollide(proyectil, lista_de_todos_los_enemigos, True)

            for enemigo in lista_enemigos_alcanzados:
                lista_de_todos_los_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)
                puntuacion += 10
            if proyectil.rect.x > 760:
                lista_de_todos_los_proyectiles.remove(proyectil)

        if len(lista_de_todos_los_enemigos.sprites()) > 0:
            lista_de_todos_los_sprites.draw(screen)
            lista_de_todos_los_sprites.update()
        else:
            ganaste = myFont.render('Ganaste Pintoquin',False, (0,0,0))
            screen.blit(ganaste, (400,300))

        pygame.display.flip()
        pygame.time.delay(40)

if __name__ == '__main__':
    main()