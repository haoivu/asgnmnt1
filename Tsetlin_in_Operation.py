
import random
#import matplotlib.pyplot
#import pandas


class Environment:
    def __init__(self, c_1, c_2):
        self.c_1 = c_1
        self.c_2 = c_2

    def penalty(self, action):
        if action == 1:
            if random.random() <= self.c_1:
                return True
            else:
                return False
        elif action == 2:
            if random.random() <= self.c_2:
                return True
            else:
                return False


class Tsetlin:
    def __init__(self, n):
        # n is the number of states per action
        self.n = n

        # Initial state selected randomly
        self.state = random.choice([self.n, self.n+1])

    def reward(self):
        if self.n >= self.state > 1:
            self.state -= 1
        elif self.n < self.state < 2*self.n:
            self.state += 1

    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        elif self.state > self.n:
            self.state -= 1

    def makeDecision(self):
        if self.state <= self.n:
            return 1
        else:
            return 2


env = Environment(0.1, 0.3)
action_count = [0, 0]
progression = []

states = 10
las = [Tsetlin(states), Tsetlin(states), Tsetlin(states), Tsetlin(states), Tsetlin(states)]

for i in range(100):
    print('Run #{}'.format(i))
    yes_no_count = [0, 0]
    for la in las:
        action = la.makeDecision()

        yes_no_count[action - 1] += 1
        action_count[action - 1] += 1
        progression.append(action_count[0])

    yes = yes_no_count[0]

    #print('{} yes\'s and {} no\'s'.format(yes, yes_no_count[1]))

    if yes < 4:
        reward_probability = yes * 0.2
    else:
        reward_probability = 0.6 - (yes - 3) * 0.2

    reward_count = 0
    for index, la in enumerate(las):
        if random.random() <= reward_probability:
            # print('Tsetlin {} rewarded'.format(index + 1))
            reward_count += 1
            la.reward()
        else:
            # print('Tsetlin {} penalized'.format(index + 1))
            la.penalize()
    # print('{}/{} rewarded'.format(reward_count, len(las)))
    # print('\n')
print(progression)
print(action_count)
count_0 = float(action_count[0])
count_1 = float(action_count[1])
final = count_1 / count_0
print(final)
#print(progression)
"""
Action 1 = Yes
Action 2 = No

If random() is less than c_n then penalize (true). I.E. c_n is chance of penalty, 1 - c_n is chance of reward
"""
