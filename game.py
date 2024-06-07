import  time , pygame # vazw vivliothiki

pygame.init() # arxikopoiei tis rithmiseis tis vivliothikis
screen = pygame.display.set_mode((1000, 700)) # ftiaxnw parathuri me diastaseis 400x300
done = True # voithitiki metavliti
x = 50
y = 50





image = pygame.image.load("pac man.png") #fortwnw eikona
resized = pygame.transform.scale(image, (50, 50)) #allazw megethos eikonas
lap = 0
start = time.time()
while done:
    for event in pygame.event.get(): # events = pliktra apo keyboard h mouseclicks
        if event.type == pygame.QUIT:
            done = False

    file = open("highscore.txt","r")
    highscore = file.read()
    file.close()


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= 1
    if pressed[pygame.K_s]:
        y += 1
    if pressed[pygame.K_d]:
        x += 1
    if pressed[pygame.K_a]:
        x -= 1

    screen.fill((0,0,0))
    player =  pygame.draw.rect(screen,(255,255,255),pygame.Rect(x, y, 50, 50))
    #player = pygame.draw.circle(screen, (255,0,0), (100,100),50)
    topB = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 1300, 10))
    botB = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 685, 1300, 10))
    lb = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 10, 1000))
    rb = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(990, 0, 10, 1000))
    finish=pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(950, 650, 50, 50))
    w1 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 150, 300, 10))
    w2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(290, 150, 10,300))
    w3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(360, 12, 10, 280))
    w4 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(360, 360, 100, 100))
    w5 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, 530, 350, 10))
    w6 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(360, 440, 10, 100))
    w7 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 530, 10,80))
    w8 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(70, 450, 10, 150))
    w9 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(70, 450, 230, 10))
    w10 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(70, 600, 440, 10))
    w11 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(360, 360, 400, 10))
    w12 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(360, 290, 400, 10))
    w13  = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(750, 12, 10, 280))
    w14 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(830, 12, 10, 610))
    w15 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(830, 620, 240, 10))
    w16 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(750, 500, 10, 500))


    screen.blit(resized, player)

    if player.colliderect(topB):
        y += 3
    if player.colliderect(botB):
        y -= 3
    if player.colliderect(rb):
        x -= 3
    if player.colliderect(lb):
        x += 3

    if player.colliderect(finish):
        x = 50
        y = 50


        end = time.time()
        lap = round(end - start,1)
        highcore = round(end - start,1)
        print(lap)
        print(highscore)

        start = end
        if float(lap) < float(highscore): #τα μετατρεπω σε δεκαδικα
            file = open("highscore.txt","w")
            file.write(str(lap))
            file.close()


    if player.colliderect(w2) or player.colliderect(w1) or player.colliderect(w3) or player.colliderect(w4) or player.colliderect(w5) or player.colliderect(w6) or player.colliderect(w7) or player.colliderect(w8) or player.colliderect(w9) or player.colliderect(w10) or player.colliderect(w11) or player.colliderect(w12) or player.colliderect(w13) or player.colliderect(w14) or player.colliderect(w15) or player.colliderect(w16) :
        if pressed[pygame.K_w]:
            y += 3
        if pressed[pygame.K_s]:
            y -= 3
        if pressed[pygame.K_d]:
            x -= 3
        if pressed[pygame.K_a]:
            x += 3

    font = pygame.font.SysFont('arial',20,True,True)
    time1 = font.render("Time : "+str(lap),True,(225,0,0))
    screen.blit(time1,(900,100))

    font = pygame.font.SysFont('arial', 20, True, True)
    highscore = font.render("highscore : " + str(highscore), True, (245, 0, 0))
    screen.blit(highscore, (870, 150))



    pygame.display.flip() # refresh tin othoni