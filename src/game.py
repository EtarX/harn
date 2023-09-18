import pygame
import moderngl as mgl
import sys

from settings import FPS
from core.audio_manager import AudioManager
from core.event_manager import EventManager
from core.hud_manager import HUDManager

from ui.main_menu import MainMenu
from ui.in_game import InGame

class Window:
	def __init__(self, title='Window', win_size=(1600, 1200)):
		self.win_size = win_size

		pygame.init()
		pygame.display.set_caption(title)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
		
		self.screen = pygame.display.set_mode(self.win_size, flags=pygame.OPENGL | pygame.DOUBLEBUF)

		self.ctx = mgl.create_context()
		self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

		self.clock = pygame.time.Clock()

		# UI HUDS
		self.UI_MainMenu = MainMenu
		self.UI_In_Game = InGame

		# Initialize EventManager, AudioManager, and HUDManager
		self.event_manager = EventManager()
		self.audio_manager = AudioManager()
		self.hud_manager = HUDManager(self)

	def start(self):
		# TODO change back to MainMenu
		self.hud_manager.set_hud(self.UI_In_Game)  # Set the initial HUD outside the loop
		while True:
		    self.hud_manager.handle_events()  # Handle events
		    self.hud_manager.update()         # Update the active HUD
		    self.hud_manager.draw()           # Draw the active HUD
		    pygame.display.flip()
		    self.clock.tick(FPS)

	def close(self,*a):

		# Release resources from AudioManager
		self.audio_manager.release()
		pygame.quit()
		sys.exit()

if __name__ == "__main__":
	window = Window(title="My Game")
	window.start()
