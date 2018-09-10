import random
from collections import Counter

class Tsetlin:
    def __init__(self, n):
        # n is the number of states per action
        self.n = n

        # Initial state selected randomly
        self.state = random.choice([self.n, self.n+1])

    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2*self.n:
            self.state += 1

    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        elif self.state > self.n:
            self.state -= 1

    def make_decision(self):
        if self.state <= self.n:
            return 1
        else:
            return 2

action_count = [0, 0]
# states = [1,2,3,5,10,50]
states = 50
runs = 50
automaton = 5
yaas = []
las = []
for i in range(automaton):
    las.append(Tsetlin(states))

def learning_automaton():
    for n in range(runs):
        yay_nay = [0, 0]
        for la in las:
            action = la.make_decision()
            yay_nay[action - 1] += 1
            action_count[action - 1] += 1

        yes = yay_nay[0]
        yaas.append(yes)
        counts = Counter(yaas)
        print '#{} - {}'.format(n+1,yay_nay)
        if yes < 4:
            reward_probability = yes * 0.2
        else:
            reward_probability = 0.6 - (yes - 3) * 0.2

        reward_count = 0
        for m, la in enumerate(las):
            if random.random() <= reward_probability:
                reward_count += 1
                la.reward()
            else:
                la.penalize()
    print '#0:', counts[0]
    print '#1:', counts[1]
    print '#2:', counts[2]
    print '#3:', counts[3]
    print '#4:', counts[4]
    print '#5:', counts[5]
    print '#Yes: {} - #No: {}'.format(action_count[0], action_count[1])
    result = float(action_count[1]) / float(action_count[0])
    print result
learning_automaton()
