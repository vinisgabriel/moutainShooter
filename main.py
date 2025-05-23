import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup End")

print("Loop Start")
while True:
   #checar por todos eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()#fechar janela
            quit() #encerrar pygame
