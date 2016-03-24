# q-learning
Implementation of Q-Learning algorithm to search a maze

Q-Learning is a reinforcement learning algorithm. Given an environment and an agent, the latter explores the former with no prior knowledge. It receives a reward for a right action and a penalty for wrong ones. The execution uses a learning rate for the agent (usually set to small values. We suggest 0.1) and a discount factor (tradeoff between imediate and long-term rewards. It can be set to 0.9).

# execution
__$ bash qlearning.sh input\_file learning\_rate discount\_factor iterations__
