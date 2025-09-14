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
        self.state_index = {state: i for i, state in enumerate(states)}
        n = len(states)
        matrix = np.zeros((n,n), dtype=float)

        # count transitions from state to another
        for i in range(len(sequence)- 1):
            curr_state = sequence[i]
            next_state = sequence[i + 1]
            if curr_state in self.state_index and next_state in self.state_index:
                matrix[self.state_index[curr_state], self.state_index[next_state]] += 1

        # normalize rows to probabilities
        for i in range(n):
            row_sum = np.sum(matrix[i])
            if row_sum > 0:
                matrix[i] /= row_sum
        
        self.transition_matrix = matrix

        return self.transition_matrix
    
    def generate_samples(self, first_state, seed, length):

        if self.transition_matrix is None:
            raise ValueError("Transition matrix has not been generated yet.")
        
        random.seed(seed)
        sequence = [first_state]

        for _ in range(length):
            curr_state = sequence[-1]
            if curr_state not in self.state_index:
                raise ValueError(f"State '{curr_state}' not found in state list.")
            row = self.transition_matrix[self.state_index[curr_state]]

            r = random.random()
            cumulative = 0.0
            for i, p in enumerate(row):
                cumulative += p
                if r < cumulative:
                    sequence.append(self.states[i])
                    break

        return sequence
    
    def stationary_distribution(self):

        if self.transition_matrix is None:
            raise ValueError("Transition matrix has not been generated yet.")

        # Eigen decomposition of transpose
        eigvals, eigvecs = np.linalg.eig(self.transition_matrix.T)

        # Find eigenvector corresponding to eigenvalue 1
        idx = np.argmin(np.abs(eigvals - 1.0))
        stationary = np.real(eigvecs[:, idx])

        # Normalize to sum to 1
        stationary = stationary / np.sum(stationary)
        stationary = stationary.real  # in case of tiny imaginary parts

        return stationary