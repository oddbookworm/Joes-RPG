from .GameObject import *

class GameCharacter(GameObject):
    __slots__ = GameObject.__slots__ + ["img"]
    def __init__(self, _data: ObjectData) -> None :
        super().__init__(_data)

    def load_from_file(self, filename: str, transparency: bool=False) -> None:
        if transparency:
            img = pygame.image.load(filename).convert_alpha()
        else:
            img = pygame.image.load(filename).convert()

        self.img = pygame.transform.scale(img, self.rect.size)

    def draw(self, dest_surf: pygame.Surface) -> None:
        dest_surf.blit(self.img, self.rect)