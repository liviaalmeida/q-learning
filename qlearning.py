from numpy import argmax, array
from copy import deepcopy
from random import randint, uniform
from sys import argv

class node (object):
	def __init__(self,char):
		self.char = char
		if char=='-':
			self.q = {'up':0,'down':0,'left':0,'right':0}
		elif char!='#':
			self.q = 0

class agent (object):
	def __init__(self,x,y,alpha,gamma):
		self.position = [x,y]
		self.alpha = alpha
		self.gamma = gamma
		self.epsilon = 0.3
		self.moves = {'up':[-1,0],'down':[1,0],'left':[0,-1],'right':[0,1]}
		self.rewards = {'-':-1,'0':10,'&':-10}

	def update_pos(self,maze):
		maxq = lambda nxt: max(nxt.q.values()) if type(nxt.q)==dict else nxt.q
		maxes = lambda crt: [index for index,item in enumerate(crt.q.values()) if item==max(crt.q.values())]
		#node agent is right now
		current = maze[self.position[0]][self.position[1]]
		#which direction will he go?
		if uniform(0,1) < self.epsilon:
			successors = range(0,len(current.q))
		else:
			successors = maxes(current)
		direction = current.q.keys()[successors[randint(0,len(successors)-1)]]
		#what is the coordinate to new possible place?
		newc = map(int,array(self.position)+array(self.moves[direction]))
		#check out next node
		next = maze[newc[0]][newc[1]]
		#update q value
		if current.char == '-':
			current.q[direction] = (1-self.alpha)*current.q[direction] + self.alpha*(self.rewards[next.char] + self.gamma*maxq(next) - current.q[direction]) if next.char!='#' else (1-self.alpha)*current.q[direction] + self.alpha*(self.rewards[current.char] + self.gamma*maxq(current) - current.q[direction])
		else:
			current.q = (1-self.alpha)*current.q + self.alpha*(self.rewards[next.char] + self.gamma*maxq(next) - current.q) if next.char!='#' else (1-self.alpha)*current.q + self.alpha*(self.rewards[current.char] + self.gamma*maxq(current) - current.q)
		#update position, if next position is not a wall
		if next.char != '#':
			self.position = deepcopy(newc)

def GetMaze (arqStr):
	arq = open(arqStr,"r")
	arq.readline()
	maze = []
	for line in arq:
		maze.append([node(item) for item in line.strip()])
	return maze

def Policy (maze):
	outpi = open("pi.txt","w")
	update = {'up':'^','down':'v','left':'<','right':'>'}
	for line in maze:
		for item in line:
			if item.char=='-':
				item.char = update[item.q.keys()[argmax(item.q.values())]]
			outpi.write(item.char)
		outpi.write('\n')
	outpi.close()

def Q (maze):
	outq = open("q.txt","w")
	for m,line in enumerate(maze):
		for n,item in enumerate(line):
			if item.char=='-':
				for key in item.q:
					line = str(m)+','+str(n)+','+str(key)+','+str(item.q[key])+'\n'
					outq.write(line)
	outq.close()

def Q_Learning (arqStr,alpha,gamma,maxit):
	maze = GetMaze(arqStr)
	for i in range(0,maxit):
		for m,line in enumerate(maze):
			for n,item in enumerate(line):
				if item.char=='-':
					pacman = agent(m,n,alpha,gamma)
					#while pacman does not reach terminal state
					while maze[pacman.position[0]][pacman.position[1]].char=='-':
						pacman.update_pos(maze)
	Q(maze)
	Policy(maze)

if __name__ == '__main__':
	Q_Learning(argv[1],float(argv[2]),float(argv[3]),int(argv[4]))