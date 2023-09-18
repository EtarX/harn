import pygame
import numpy as np

# going to be a parent for almost every child widget
class Widget:
    def __init__(self, position):
        self.position = position
        self.visible = True

    def draw(self, window):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

