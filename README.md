# q-learning
Implementation of Q-Learning algorithm to search a maze

Q-Learning is a reinforcement learning algorithm. Given an environment and an agent, the latter explores the former with no prior knowledge. It receives a reward for a right action and a penalty for wrong ones. The execution uses a learning rate for the agent (usually set to small values. We suggest 0.1) and a discount factor (tradeoff between imediate and long-term rewards. It can be set to 0.9). The maze is a txt file where \# are walls, \& are traps, \- are empty spots, and 0 is the objective.

The execution outputs two files:
* pi.txt shows the action for each spot of the maze
* q.txt outputs, for each coordinate (x,y), the preferred action for the agent and its value

# execution
__$ bash qlearning.sh input\_file learning\_rate discount\_factor iterations__
