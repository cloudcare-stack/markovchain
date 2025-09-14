# test_a1.py
import numpy as np
from a1 import A1

def main():
    # Example states and sequence
    states = ["sunny", "cloudy", "rainy"]
    sequence = ["sunny", "sunny", "cloudy", "rainy", "sunny", "cloudy", "cloudy", "rainy"]

    # Initialize class
    model = A1()

    # Generate Markov chain (transition matrix)
    P = model.generate_markov_chain(states, sequence)
    print("Transition Matrix:")
    print(P)

    # Generate sample sequence
    generated_seq = model.generate_samples("sunny", seed=42, length=9)
    print("\nGenerated Sequence (length 10):")
    print(generated_seq)

    # Compute stationary distribution
    pi = model.stationary_distribution()
    print("\nStationary Distribution:")
    print(pi)
    print("Sum of stationary distribution (should be 1):", np.sum(pi))

if __name__ == "__main__":
    main()
