# Biblioteca PyGame
from pdb import post_mortem
from tracemalloc import stop
import pygame
# Biblioteca para geracao de numeros pseudoaleatorios
import random
# Modulo da biblioteca PyGame que permite o acesso as teclas utilizadas
from pygame.locals import *
pontos = 0
# Classe que representar o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('spacecraft1.png')
        self.rect = self.surf.get_rect()

    # Determina acao de movimento conforme teclas pressionadas
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)

        # Mantem o jogador nos limites da tela do jogo
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


# Classe que representa os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self, v1, v2):
        super(Enemy, self).__init__()
        self.surf= pygame.image.load('asteroid1.png') #Preenche com cor branca (RGB)
        self.rect = self.surf.get_rect( #Coloca na extrema direita (entre 820 e 900) e sorteia sua posicao em relacao a coordenada y (entre 0 e 600)
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = random.uniform(v1, v2) #Sorteia sua velocidade, entre 1 e 15
        

    # Funcao que atualiza a posiçao do inimigo em funcao da sua velocidade e termina com ele quando ele atinge o limite esquerdo da tela (x < 0)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            global pontos
            pontos +=1
            self.kill()
            
        

def inicio():
 global pontos
# Inicializa pygame
 pygame.init()
 gaming = pygame.mixer.Sound('mortea.ogg')
 morte = pygame.mixer.Sound('p.ogg')
 levelup = pygame.mixer.Sound('up.mp3')
# Cria a tela com resolução 800x600px
 screen = pygame.display.set_mode((800, 600))

# Cria um evento para adicao de inimigos
 ADDENEMY = pygame.USEREVENT + 1
 pygame.time.set_timer(ADDENEMY, 1000) #Define um intervalo para a criacao de cada inimigo (milisegundos)
# Cria o jogador (nosso retangulo)
 player = Player()
# Define o plano de fundo, com a cor preta (RGB)
 fundo = pygame.image.load('fundo2.jpg')

#screen.blit(fundo,(0,0))
#screen.blit(texto, texto2)

 enemies = pygame.sprite.Group() #Cria o grupo de inimigos
 all_sprites = pygame.sprite.Group() #Cria o grupo de todos os Sprites
 all_sprites.add(player) #Adicionar o player no grupo de todos os Sprites
 running = True #Flag para controle do jogo
 contador = 0
 velocidade1 = 1
 velocidade2 = 2

 while running:
     
    

    
    #Laco para verificacao do evento que ocorreu
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #Verifica se a tecla ESC foi pressionada
                running = False
        elif event.type == QUIT: #Verifica se a janela foi fechada
            running = False
        elif(event.type == ADDENEMY): #Verifica se e o evento de criar um inimigo
            if contador%10 == 1 and velocidade2 < 16:
                pygame.mixer.Sound.play(levelup)
                velocidade1 +=1
                velocidade2 +=1
            new_enemy = Enemy(velocidade1, velocidade2) #Cria um novo inimigo
            contador+=1
            enemies.add(new_enemy) #Adiciona o inimigo no grupo de inimigos
            all_sprites.add(new_enemy) #Adiciona o inimigo no grupo de todos os Sprites
    screen.blit(fundo, (0, 0)) #Atualiza a exibicao do plano de fundo do jogo (neste caso nao surte efeito)
    pressed_keys = pygame.key.get_pressed() #Captura as as teclas pressionadas
    player.update(pressed_keys) #Atualiza a posicao do player conforme teclas usadas
    enemies.update() #Atualiza posicao dos inimigos
    
    if player.alive():

        fonte = pygame.font.SysFont('times_new_roman', 30)
        texto = fonte.render("Score: ",True, (248,248,255))
        texto2 = texto.get_rect()
        texto2.center = (65,50) 
        texto = fonte.render("Score: "+str(pontos),True, (248,248,255))
        screen.blit(texto, texto2)
        pygame.mixer.Sound.play(morte)
    else:
        pygame.mixer.Sound.stop(morte)
        pygame.mixer.Sound.play(gaming)
        fim = fonte.render("Final Score: "+str(pontofinal), True, (255,255,255))
        screen.blit(fim, (300, 255))
        for event in pygame.event.get():
             if event.type == pygame.quit: 
              running = False
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    running = False
                    pontos = 0
                    pygame.mixer.Sound.stop(gaming)
                    inicio()    
                if event.key == pygame.K_ESCAPE:
                    running = False
        

   
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect) #Atualiza a exibicao de todos os Sprites

    pygame.display.flip() #Atualiza a projecao do jogo


    if pygame.sprite.spritecollideany(player, enemies): #Verifica se ocorreu a colisao do player com um dos inimigos
        player.kill() #Se ocorrer a colisao, encerra o player
        pontofinal = pontos
        fundo = pygame.image.load('g2.jpg')
        ADDENEMY = 0
        



      
     



inicio()       
    


        
