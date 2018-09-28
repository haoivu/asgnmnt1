import pandas as pd
import numpy as np
import random
from random import randint

class node():
    def __init__(self, prob_name_1=None, prob_name_2=None, prob_1=None):
        self.children = []
        self.parents = []
        self.probs = None
        self.state = None
        self.states = None

    def add_child(self, node):
        self.children.append(node)

    def add_parent(self, node):
        self.parents.append(node)

    def prob_table(self, data):
        print("#DE BOUGIE") #DE BOUGIE
        self.probs = pd.DataFrame(data=data[1:, 1:],
                                  index=data[1:, 0],
                                  columns=data[0, 1:])
        print(self.probs)
        self.states = data[0, 1:]
        self.state = self.states[0]
        for state in data[0, 1:]:
          my_dict[state] = 0

    def get_probability(self, state=None):
        if self.parents:
            index = ''
            for parent in self.parents:
                index += parent.state
        else:
            index = 'row'

        if state is None:
            state = self.state
        return self.probs.loc[index, state]

    def markov_blanket(self):
        markov_blanket = []
        markov_blanket += self.parents
        for child in self.children:
            markov_blanket += child.parents
            markov_blanket.append(child)
        markov_blanket = filter(lambda x: x is not self, markov_blanket)
        return markov_blanket

    def calculate_markov_blanket(self):
        mb = self.markov_blanket()
        trueValue = self.get_probability(self.states[0])
        for node in mb:
            trueValue *= node.get_probability()

        mb = self.markov_blanket()
        falseValue = self.get_probability(self.states[1])
        for node in mb:
            falseValue *= node.get_probability()

        calculate_true = (trueValue/(trueValue+falseValue))
        calculate_false = (falseValue/(trueValue+falseValue))

        rn = random.random() #random tall mellom 0 og 1
        if rn < calculate_true:
        	self.state = self.states[0]
        else:
          	self.state = self.states[1]
        my_dict[self.state] = my_dict[self.state] + 1
        return calculate_true, calculate_false


def pc(parent, child):
    parent.add_child(child)
    child.add_parent(parent)

my_dict = {}

sprinkler = node()
sprinkler.prob_table(data=np.array([[None, 'Sprinkler', 'NotSprinkler'],
                           ['row', 0.3, 0.7]]))
rain = node()
rain.prob_table(data=np.array([[None, 'Rain', 'NotRain'],
                      ['row', 0.2, 0.8]]))

watson_is_wet = node()
watson_is_wet.prob_table(data=np.array([[None, 'WatsonGrassWet', 'WatsonGrassNotWet'],
                               ['Rain', 0.7, 0.3],
                               ['NotRain', 0.12, 0.88]]))

sherlock_is_wet = node()
sherlock_is_wet.prob_table(data=np.array([[None, 'SherlockGrassWet', 'SherlockGrassNotWet'],
                                 ['RainSprinkler', 0.8, 0.2], ['SprinklerRain', 0.8, 0.2],
                                 ['RainNotSprinkler', 0.6, 0.4], ['NotSprinklerRain', 0.6, 0.4],
                                 ['NotRainSprinkler', 0.7, 0.3], ['SprinklerNotRain', 0.7, 0.3],
                                 ['NotRainNotSprinkler', 0.1, 0.9], ['NotSprinklerNotRain', 0.1, 0.9]]))

pc(rain, watson_is_wet)
pc(rain, sherlock_is_wet)
pc(sprinkler, sherlock_is_wet)
#rain.markov_blanket()

print(sherlock_is_wet.probs.index[0])
print(sherlock_is_wet.probs.loc['RainSprinkler', 'SherlockGrassWet'])
# print(sherlock_is_wet.calculate_markov_blanket())

not_lock = [rain, sprinkler]
for _ in range(0, 10000):
  select = randint(0, len(not_lock)-1)
  node = not_lock[select]
  node.calculate_markov_blanket()

print(my_dict)

#
