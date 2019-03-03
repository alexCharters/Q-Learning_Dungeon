from enums import *
import random

class Gambler:
	def __init__(self, learning_rate=.1, discount=.95, exploration_rate=1.0, iterations=10000):
		self.learning_rate = learning_rate
		self.discount=discount
		self.exploration_rate=exploration_rate
		self.exploration_delta = 1.0/iterations;
		self.q_table=[[0,0,0,0,0],[0,0,0,0,0]]

	def get_next_action(self, state):
		if random.random() > self.exploration_rate:
			return self.greedy_action(state);
		else:
			return self.random_action();

	def greedy_action(self, state):
		if self.q_table[FORWARD][state]>self.q_table[BACKWARD][state]:
			return FORWARD
		elif self.q_table[BACKWARD][state] > self.q_table[FORWARD][state]:
			return BACKWARD
		
		return self.random_action();

	def random_action(self):
		return FORWARD if random.random() > .5 else BACKWARD

	def update(self, old_state, new_state, action, reward):
		old_value = self.q_table[action][old_state]

		future_action = self.greedy_action(new_state);

		future_reward = self.q_table[future_action][new_state];

		new_value = old_value + self.learning_rate * (reward + self.discount*future_reward - old_value)
		self.q_table[action][old_state] = new_value

		if self.exploartion_rate > 0:
			self.exploration_rate -= self.exploration_delta
