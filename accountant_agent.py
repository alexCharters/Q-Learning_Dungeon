from enums import *
import random

class Accountant:
	def __init__(self):
		self.q_table = [[0,0,0,0,0],[0,0,0,0,0]]

	def get_next_action(self, state):
		if self.q_table[FORWARD][state] > self.q_table[BACKWARD][state]:
			return FORWARD
		elif self.q_table[BACKWARD][state] < self.q_table[FORWARD][state]:
			return BACKWARD
		return FORWARD if random.random() > .5 else BACKWARD

	def update(self, old_state, new_state, action, reward):
		self.q_table[action][old_state] += reward
