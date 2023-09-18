import pygame

class InGame:
    def __init__(self,window):
        self.window = window
        pygame.display.set_caption("In Game")

    def draw(self,window):
        window.ctx.clear(color=(0.08, 0.16, 0.9))

    def handle_event(self, event):
    	"""
    	# handle_eventndle the event, like button clicks, etc.
    	if event.type == pygame.KEYDOWN: #
	        if event.key == pygame.K_SPACE:
	            self.window.event_manager.dispatch(self.window.event_manager.SWITCH_HUD_EVENT, {'new_hud': self.window.UI_MainMenu})
		"""

		
    def update(self):
        ...