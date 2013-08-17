from Tkinter import *

class Interface:

	def __init__(self):
		self.tk = Tk()
		self.tk.title = 'simple calculator'
		self.window = Frame(self.tk, bg = '#a1a1a1')
		self.window.grid()

	def input(self):
		self.console = Entry(self.window, justify = RIGHT, fg = '#999999', width = 30)
		self.console.grid(row= 0, column = 0, columnspan = 5, padx = 5, pady = 5)
		self.console.insert(0, '0')
		return self.console


class calculator:

	def __init__(self):
		pass

	def key_press(self):
		pass


def button(text, row, column, command = None, operator = None ):
	button = Button(window, text = text)
	button['command'] = command
	button.grid(row = row, column = column, pady = 3)
	return button



interface = Interface()
window = interface.window

#get display console
console = interface.input()

#start numberic button
#note a better version of this is to write a function
#to generate all this buttons

button('1', 1, 0)
button('2', 1, 1)
button('3', 1, 2)

button('4', 2, 0)
button('5', 2, 1)
button('6', 2, 2)

button('7', 3, 0)
button('8', 3, 1)
button('9', 3, 2)

button('0', 4, 1)
# end button

#start operation buttons
divide = button('/', 1, 3)
multiply = button('*', 2, 3)
sub = button('-', 3, 3)
add = button('+', 4, 3) 

equal = button('=', 4, 2)
cancel = button('C', 4, 0)



if __name__ == '__main__':
	interface.tk.mainloop()