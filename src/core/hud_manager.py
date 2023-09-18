import pygame

class HUDManager:
    def __init__(self, window):
        self.window = window
        self.event_manager = window.event_manager
        self.current_hud = None
        self.event_manager.register_listener(pygame.QUIT, self.window.close)
        self.event_manager.register_listener(self.event_manager.SWITCH_HUD_EVENT, self.switch_hud)

    def switch_hud(self, event_data):
        """Switch to a new HUD based on the event data."""
        new_hud_class = event_data.get('new_hud')
        if new_hud_class:
            self.set_hud(new_hud_class)

    def set_hud(self, hud):
        self.current_hud = hud(self.window)
    
    def handle_events(self):
        for event in pygame.event.get():
            print(f"Event detected: {event.type}")  # TODO Remove this line
            self.event_manager.dispatch(event.type, event)  # Dispatch the event
            if self.current_hud:
                self.current_hud.handle_event(event)


    def update(self):
        if self.current_hud:
            self.current_hud.update()

    def draw(self):
        if self.current_hud:
            self.current_hud.draw(self.window)

