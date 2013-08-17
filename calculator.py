from Tkinter import *

class Calculator(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		self.createNumbers()

	def createWidgets(self):
		self.quitButton = Button(self, text = "Quit", command = self.quit)
		self.quitButton.grid()

	def createNumbers(self):

		self.numberButton = Button(self, text = "1").grid()
		
		

app = Calculator()
app.master.title("Simple Calc")
app.mainloop()
	