from typing import TypedDict

import pygame

from ._types import _Coord

class ObjectData(TypedDict):
    name: str
    pos: pygame.Vector2
    size: _Coord
    active: bool

class GameObject:
    __slots__ = ["name", "pos", "rect", "active"]
    def __init__(self, _data: ObjectData, *args, **kwargs) -> None:
        self.name = _data["name"]
        self.pos = _data["pos"]
        self.rect = pygame.Rect(_data["pos"].x, _data["pos"].y, *_data["size"])
        self.active = _data["active"]

    def get_data(self) -> ObjectData:
        data: ObjectData = {
            "name": self.name,
            "pos": self.pos,
            "size": self.rect.size,
            "active": self.active
        }
        return data

    def draw_debug_rect(self, target: pygame.Surface) -> None:
        pygame.draw.rect(target, (255, 0, 0), self.rect, 3)

    def collidepoint(self, pos: _Coord) -> bool:
        return self.rect.collidepoint(pos)

    def colliderect(self, rect: pygame.Rect):
        return self.rect.colliderect(rect)

    def set_active(self, active: bool):
        self.active = active