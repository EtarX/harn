import pygame

class EventManager:
    SWITCH_HUD_EVENT = pygame.USEREVENT + 1
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unregister_listener(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def dispatch(self, event_type, event_data=None):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(event_data)
