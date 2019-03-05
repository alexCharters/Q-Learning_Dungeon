from enums import *
import turtle
import random
import time

class DungeonSimulator:
	MISSING = object()

	def __init__(self, length=5, slip=.1, small=2, large=10):
		self.length = length
		self.slip = slip
		self.small = small
		self.large = large
		self.state = 0

	def take_action(self, action):
		if random.random() < self.slip:
			action = not action
		if action == BACKWARD:
			reward = self.small
			self.state = 0;
		elif action == FORWARD:
			if self.state < self.length-1:
				self.state += 1;
				reward = 0;
			else:
				reward = self.large
		return self.state, reward

	def reset(self):
		self.state = 0
		return self.state

	def draw(self, exp_rate):
		turtle.tracer(0, 0)
		self.__draw_dungeon()
		self.__draw_agent(exp_rate)
		turtle.update()
		turtle.clearscreen()

	def draw(self, exp_rate=None):
		turtle.tracer(0, 0)
		self.__draw_dungeon()
		self.__draw_agent(exp_rate)
		turtle.update()
		turtle.clearscreen()

	def __draw_dungeon(self):
		t = turtle.Pen()
		t.forward(250)
		t.left(90)
		t.forward(50)
		t.left(90)
		t.forward(250)
		t.left(90)
		t.forward(50)
		for i in range(5):
			t.up()
			t.left(90)
			t.forward(50)
			t.left(90)
			t.down()
			t.forward(50)
			t.up()
			t.left(180)
			t.forward(50)
		

	def __draw_agent(self, exp_rate=None):
		t = turtle.Pen()
		if exp_rate != None:
			t.right(90)
			t.forward(20)
			t.write(exp_rate)
			t.left(180)
			t.forward(20)
			t.right(90)
		t.up()
		t.forward(25+(50 * self.state))
		t.down()
		t.circle(20)
