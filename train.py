import random
import json
import argparse
import time
from drunkard_agent import Drunkard
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

	dungeon = DungeonSimulator()
	dungeon.reset()
	total_reward = 0


	for step in range(FLAGS.iterations):
		old_state = dungeon.state
		action = agent.get_next_action(old_state);
		new_state, reward = dungeon.take_action(action)
		agent.update(old_state, new_state, action, reward)

		total_reward += reward
		if step % 250 == 0:
			print(json.dumps({'step':step, 'total_reward': total_reward}))

		time.sleep(.0001)

	print("Final Q-table" agent.q-table)

if __name__ == "__main__":
    main()
	
