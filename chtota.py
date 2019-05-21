import pygame,random,time
bullets=[]
enemys=[]
time=0
tneed=400
FPS = 60
jp=17
lol='n'
hp=3
grav=1
x=300
y=200
velx=0
vely=0
naprav='r'
W = 600
H = 400 
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RED = (255, 0, 0)
pygame.init()
YELLOW = (255,255,0)
class bullet:
    def __init__(self,x,y,nap):
        self.x=x
        self.y=y
        self.col=YELLOW
        self.nap=nap
    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.col, (self.x, self.y,  5,   5))
        if self.nap =='l':
            self.x-=5
        if self.nap =='r':
            self.x+=5
        #с врагом столкновения
class enemy:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.hp=2
        self.kd=0
    def draw(self):
        global x,y,hp
        pygame.draw.rect(DISPLAYSURF, RED, (self.x, self.y,  30,   30))
        if self.y < 370:
            self.y+=3
        else:
            if self.x-15 < x-15:
                self.x+=2.5
            if self.x-15 > x-15:
                self.x-=2.5
        if self.kd<=0:  
            if x+30>self.x and self.x<x+30:
                hp-=1
                self.kd=300
        else:
            self.kd-=1
        #с персонажем столкновения
DISPLAYSURF = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
while True:
    if hp < 1:
        exit()
    clock.tick(FPS)
    time+=1
    DISPLAYSURF.fill(BLUE)
    pygame.draw.rect(DISPLAYSURF, WHITE, (x, y,  30,   30))
    for b in bullets:
        b.draw()
        if b.x+5 < 0 or b.x > 595:
            bullets.remove(b)
        for e in enemys:
            if b.x+5>=e.x and b.x>=e.x-30:
                e.hp-=1
                bullets.remove(b)
            if e.hp < 1:
                enemys.remove(e)
    for e in enemys:
        e.draw()
    if time == tneed:
        
        ene = enemy(0,0)
        enemys.append(ene)
        time=0
        if tneed > 80:
            tneed-=30
    pygame.display.set_caption('hp: '+str(hp))
    pygame.display.update()
    vely+=grav
    if y >= 370:
        vely=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velx=-3
            elif event.key == pygame.K_RIGHT:
                velx=3
            elif event.key == pygame.K_UP:
                if vely <= 0:
                    vely-=jp
            elif event.key == pygame.K_SPACE:
                if naprav == 'l':
                    bul=bullet(x,y+11,naprav)
                    bullets.append(bul)
                if naprav == 'r':
                    bul=bullet(x+30,y+11,naprav)
                    bullets.append(bul)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velx=0
            elif event.key == pygame.K_RIGHT:
                velx=0
    if velx < 0:
        naprav='l'
    if velx > 0:
        naprav='r'
    if x < 0:
        if velx < 0:
            velx=0
    if x > 568:
        if velx > 0:
            velx=0
    x+=velx
    y+=vely
    
