""" 
Program: FivestarvideoGUI2.py
Author: cathryn 11-21-21

*** Note: the file breezypythongui.py and purchase.wav MUST be in the same directory as the file in order for the application to work.***
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import math
import pygame

class FivestarVideo(EasyFrame):
	"""Converts a input string to uppercase and displays the result"""

	def __init__(self):
		"""Sets up the window and the widgets."""

		EasyFrame.__init__(self, title = "Five Star Video", width = 500, height = 260, background = "blue")
		titleFont = Font(family = "Cambria", size = 26, weight = "bold")
		self.titleLabel = self.addLabel(text = "Five Star Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", font = titleFont, background = "blue", foreground = "yellow")

		# Input
		videoFont = Font(family = "Arial", size = 11, weight = "bold")
		self.addLabel(text = "No. of OLD Videos being rented at $2.00 per video:", row = 1, column = 0, font = videoFont, background = "blue", foreground = "yellow")
		self.inputField1 = self.addIntegerField(value = 0, row = 1, column = 1)
		self.addLabel(text = "No. of NEW Videos being rented at $3.00 per video:", row = 2, column = 0, font = videoFont, background = "blue", foreground = "yellow")
		self.inputField2 = self.addIntegerField(value = 0, row = 2, column = 1)

		# The command button
		self.addButton(text = "Calculate!", row = 4, column = 0, columnspan = 2, command = self.compute)

		# The output
		self.addLabel(text = "Total Cost:", row = 3, column = 0, font = videoFont, background = "blue", foreground = "yellow")
		self.outputField = self.addFloatField(value = 0.0, row = 3, column = 1, state = "readonly")

	# Event handling method
	def compute(self):

		#soundbites 
		pygame.mixer.init()
		register = pygame.mixer.Sound("purchase.wav")

		""" Establishes variables and calculates the results, handles user error"""
		try:			
			num1 = self.inputField1.getNumber()
			num2 = self.inputField2.getNumber()
			oldCost = float(2.00)
			newCost = float(3.00)
			calcTotal = (num1 * oldCost) + (num2 * newCost)
			result = "$" + ("%10.2f" % calcTotal)
			self.outputField.setValue(result)
			register.play()


		except ValueError:
			self.messageBox(title = "ERROR", message = "Input must be an integer greater than or equal to zero!")


#definition of the main()function for program entry
def main():
	"""Instantiation and pops up the window."""
	FivestarVideo().mainloop()

# global call to trigger the main()function
if __name__	== "__main__":
	main()

