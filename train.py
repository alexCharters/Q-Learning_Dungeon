import random
import json
import argparse
import time
from drunkard_agent import Drunkard
from accountant_agent import Accountant
from gambler_agent import Gambler
from dungeon import DungeonSimulator

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--agent', type=str, default='DRUNKARD', help='Which agent to use')
	parser.add_argument('--learning_rate', type=float, default=.1, help="How quickly the algorithm tries to learn")
	parser.add_argument('--discount', type=float, default=.95, help="Discount for estimated future action")
	parser.add_argument('--iterations', type=int, default=2000, help="Iteration count")

	FLAGS, unparsed = parser.parse_known_args()

	if FLAGS.agent == 'DRUNKARD':
		agent = Drunkard()
	if FLAGS.agent == 'ACCOUNTANT':
		agent = Accountant()
	if FLAGS.agent == 'GAMBLER':
		agent = Gambler(FLAGS.learning_rate, FLAGS.discount, 1.0, FLAGS.iterations)

	dungeon = DungeonSimulator()
	dungeon.reset()
	total_reward = 0


	for step in range(FLAGS.iterations):
		old_state = dungeon.state
		action = agent.get_next_action(old_state);
		new_state, reward = dungeon.take_action(action)
		agent.update(old_state, new_state, action, reward)
		if FLAGS.agent == "GAMBLER":
			dungeon.draw(agent.exploration_rate)
		else:
			dungeon.draw()

		total_reward += reward

		print(json.dumps({'step':step, 'total_reward': total_reward}))

	print("Final Q-table", agent.q_table)

if __name__ == "__main__":
    main()
	
