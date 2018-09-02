import random

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
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2*self.n:
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

yes = 0
reward_prob = yes * 0.2
reward_prob_1 = 0.6 - (yes - 3) * 0.2
env = Environment(reward_prob, reward_prob_1)
learning_automata = Tsetlin(5)

def goore_game():
    for i in range(5):
        yes_no_count = [0, 0]
        action_count = [0, 0]
        count = 0
        states = 10
        la = []
        la.append(Tsetlin(states))

        for n in range(10):
            count += 1
            for m in la:
                action = m.makeDecision()
                action_count[action - 1] += 1
                yes_no_count[action - 1] += 1

            yes = yes_no_count[0]

            if yes < 4:
                reward_prob = yes * 0.2
            else:
                reward_prob = 0.6 - (yes - 3) * 0.2

            print "#{} - {}".format(n, action_count)
        print "#Yes: {}".format(yes)

goore_game()
