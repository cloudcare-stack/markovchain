'''
Author: Colin McAteer
Assignment: Markov Chains
Date Due: September 14
'''

import numpy as np
import random

'''
# Example of creating and manipulating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # Output: [ 2  4  6  8 10]
'''

# print(random.random())

class A1:
    
    def _init_(self):
        #initialize the object's attributes, self parameter refers to the instance to the class itself
        self.states = [] # Initialize an empty list as an instance attribute
        self.state_index = {} # Initialize an empty dictionary for each instance
        self.transition_matrix = None # Initialize an instance attribute to None

    def generate_markov_chain(self, states, sequence):
        
        self.states = states
        #count all states
        self.state_index = {state: i for i, state in enumerate(states)}
        #set a variable for a length of an array of states
        x = len(states)
        #use NumPy library to create a new array with all elements initialized to zero.
        matrix = np.zeros((x,x), dtype=float)

        # count transitions from state to another
        for i in range(len(sequence)- 1):
            curr_state = sequence[i]
            next_state = sequence[i + 1]
            if curr_state in self.state_index and next_state in self.state_index:
                matrix[self.state_index[curr_state], self.state_index[next_state]] += 1

        # normalize rows to probabilities
        for i in range(x):
            #each row calculate the sum of elements wihtin NumPy arrays
            row_sum = np.sum(matrix[i])
            if row_sum > 0:
                matrix[i] /= row_sum
        
        self.transition_matrix = matrix

        return self.transition_matrix
    
    def generate_samples(self, first_state, num, length):

    def stationary_distribution(self):

    