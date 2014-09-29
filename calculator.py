from Tkinter import *

class Interface:

	def __init__(self):
		self.tk = Tk()
		self.tk.title = 'simple calculator'
		self.window = Frame(self.tk, bg = '#a1a1a1')
		self.window.grid()

	def input(self):
		self.console = Entry(self.window, justify = RIGHT, fg = '#333333', width = 30)
		self.console.grid(row= 0, column = 0, columnspan = 5, padx = 5, pady = 5)
		self.console.insert(0, '0')
		return self.console

class Calculator:

	def __init__(self):
		self.results = 0
		self.pressed_key = self.operator = ''
		self.equal_press = self.pending_operation = False
		self.key_press = True

	def change_state(self, flag):
		return not flag

	def press_key(self, key):
		self.equal_press = False
		content = console.get()
		key = str(key)
		if self.key_press:
			self.pressed_key = key
			self.key_press = False

		else:
			if key == '.':
				if key in content:
					return
			self.pressed_key = content + key

		self.log(self.pressed_key)

	def compute(self):
		self.equal_press = True
		self.pressed_key = float(self.pressed_key)
		if self.pending_operation:
			self.estimate()
		else:
			self.results = float(console.get())

	def log(self, value):
		console.delete(0, END)
		console.insert(0, value)

	def estimate(self):
		
		value = self.pressed_key

		if self.operator is '/':
			self.results /= value

		if self.operator is '-':
			self.results -= value

		if self.operator is '+':
			self.results += value

		if self.operator is '*':
			self.results *= value

		self.key_press = True
		self.pending_operation = False
		self.log(self.results)

	def operation(self, operator):
		self.pressed_key = float(self.pressed_key)
		if self.pending_operation: 
			self.compute()

		elif not self.equal_press:
			self.results = self.pressed_key
		self.key_press = True
		self.pending_operation = True
		self.operator = operator
		self.equal_press = False

	def clear(self):
		self.equal_press = False
		self.pressed_key = '0'
		self.log(0)
		self.key_press = True


def button(text, row, column, command = None):
	button = Button(window, text = text)
	button['command'] = command
	button.grid(row = row, column = column, pady = 3)
	return button

interface = Interface()
calculator = Calculator()

window = interface.window

#get display console
console = interface.input()

#start numberic button
#note a better version of this is to write a function
#to generate all this buttons

button('1', 1, 0, lambda: calculator.press_key(1))
button('2', 1, 1, lambda: calculator.press_key(2))
button('3', 1, 2, lambda: calculator.press_key(3))

button('4', 2, 0, lambda: calculator.press_key(4))
button('5', 2, 1, lambda: calculator.press_key(5))
button('6', 2, 2, lambda: calculator.press_key(6))

button('7', 3, 0, lambda: calculator.press_key(7))
button('8', 3, 1, lambda: calculator.press_key(8))
button('9', 3, 2, lambda: calculator.press_key(9))

button('0', 4, 1, lambda: calculator.press_key(0))
# end button

#start operation buttons
divide = button('/', 1, 3, lambda: calculator.operation('/'))
multiply = button('*', 2, 3, lambda: calculator.operation('*'))
sub = button('-', 3, 3, lambda: calculator.operation('-'))
add = button('+', 4, 3, lambda: calculator.operation('+')) 

equal = button('=', 4, 2, command = calculator.compute )
cancel = button('C', 4, 0, lambda: calculator.clear())



if __name__ == '__main__':
	interface.tk.mainloop()