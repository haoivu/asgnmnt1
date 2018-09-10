#!/usr/bin/python

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas


class Tsetlin:
    def __init__(self, n):
        # n is the number of states per action
        self.n = n

        # Initial state selected randomly
        self.state = random.choice([self.n, self.n + 1])

    def reward(self):
        if self.n >= self.state > 1:
            self.state -= 1
        elif self.n < self.state < 2 * self.n:
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


state_arr = [1, 3, 5, 10, 20]
run_count = 100

# Arrays to hold data for various states
all_action_count = []
all_yes_progression = []
all_avg_progression = []
all_avg_progression_mod = []

for state_count in state_arr:

    las = [Tsetlin(state_count), Tsetlin(state_count), Tsetlin(state_count), Tsetlin(state_count), Tsetlin(state_count)]

    # Keeps track of total actions for whole run of given state_count
    total_action_count = [0, 0]
    # Keeps track of how many yes' there are for each round throughout the a run
    yes_progression = []
    # Keeps track of yes/no ratio throughout run
    ratio_progression = []

    for i in range(0, run_count):
        yes_no_count = [0, 0]
        for la in las:
            action = la.makeDecision()

            yes_no_count[action - 1] += 1
            total_action_count[action - 1] += 1

        # Do stuff with yes count information
        yes = yes_no_count[0]
        yes_progression.append(yes)
        ratio_progression.append(float(total_action_count[0])/(total_action_count[1]+total_action_count[0]))

        if yes < 4:
            reward_probability = yes * 0.2
        else:
            reward_probability = 0.6 - (yes - 3) * 0.2

        reward_count = 0
        for index, la in enumerate(las):
            if random.random() <= reward_probability:
                reward_count += 1
                la.reward()
            else:
                la.penalize()

    print("Number of states: " + str(state_count))
    print("{} yeses and {} no's".format(total_action_count[0], total_action_count[1]))
    print("Average amount of yeses after {} rounds: {}".format(
        run_count, 5*(float(total_action_count[0])/(total_action_count[1]+total_action_count[0]))))
    print('\n')

    # Append to global arrays for diffent states sizes
    all_action_count.append(total_action_count)
    all_yes_progression.append(yes_progression)
    all_avg_progression.append(ratio_progression)

# Average multiplied by 5
all_avg_progression_mod = [map(lambda x: x * 5, it) for it in all_avg_progression]
# Shortcut
o = all_avg_progression


def printdata(arr):
    for a in arr:
        print(a)


def printall(data):
    for i in range(0, run_count):
        print("\t".join([str(data[0][i]), str(data[1][i]), str(data[2][i]), str(data[3][i]), str(data[4][i])]))


"""
Action 1 = Yes
Action 2 = No

If random() is less than c_n then penalize (true). I.E. c_n is chance of penalty, 1 - c_n is chance of reward
"""
