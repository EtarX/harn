import pygame
class MainMenu:
    def __init__(self, window):
        self.window = window
        pygame.display.set_caption("Main Menu")

    def draw(self, window):
        # Draw the main menu on the window
        window.ctx.clear(color=(0.08, 0.16, 0.18))

    def handle_event(self, event):
        # Handle the event, like button clicks, etc.
        if event.type == pygame.KEYDOWN: # Add this line
            if event.key == pygame.K_SPACE:
                # Dispatch the SWITCH_HUD_EVENT to switch to InGame HUD
                self.window.event_manager.dispatch(self.window.event_manager.SWITCH_HUD_EVENT, {'new_hud': self.window.UI_In_Game})
    def update(self):
    	...