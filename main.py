import pygame

from src.GameCharacter import GameCharacter, ObjectData

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

player_data: ObjectData = {
    "pos": pygame.Vector2(100, 100),
    "size": (50, 50),
    "name": "player",
    "active": True
}

player = GameCharacter(player_data)
player.load_from_file("cowcar.png", True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)
