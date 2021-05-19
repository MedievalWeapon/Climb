from tkinter import * 
import keyboard

root = Tk()
root.title('SquareGame')
roomSize = 500

class Box:
	def __init__(self):
		self.x = 15
		self.y = 15
		self.dy = 0
		self.g = -0.1
		self.jump = 5
		self.step = 2
		self.width = 10
		self.height = 10
		self.box = room.create_rectangle(10, 10, 10 + self.width, 10 + self.height, fill='blue')
		room.after(10, self.loop)
		
	def loop(self):
		xStep = (keyboard.is_pressed('right') - keyboard.is_pressed('left')) * self.step
		##yStep = (keyboard.is_pressed('down') - keyboard.is_pressed('up')) * self.step
		self.dy -= self.g
		if(keyboard.is_pressed('up')):
			self.dy = -self.jump
		self.x += xStep
		self.y += self.dy
		room.move(self.box, xStep, self.dy)
		self.bounding()
		room.after(10, self.loop)
			
	def bounding(self):
		if self.y + (self.height / 2) > roomSize:
			yStep = (self.y + (self.height / 2)) - roomSize
			self.y -= yStep
			print(self.y)
			self.dy = 0
			room.move(self.box, 0, -yStep)
			


room = Canvas(root, height=roomSize, width=roomSize)
room = Canvas(root, height=roomSize, width=roomSize)

b = Box()


room.pack()
root.mainloop()
