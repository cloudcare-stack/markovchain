# test_a1.py
import numpy as np
from a1 import A1

def main():
    states = ["sunny", "cloudy", "rainy"]
    sequence = ["sunny", "sunny", "cloudy", "rainy", "sunny", "cloudy", "cloudy", "rainy"]

    model = A1()

    # --- Test transition matrix ---
    P = model.generate_markov_chain(states, sequence)
    print("Transition Matrix:")
    print(P)

    # Each row should sum to 1 (within floating-point tolerance)
    row_sums = np.sum(P, axis=1)
    for i, s in enumerate(states):
        if np.sum(P[i]) > 0:  # only check rows with transitions
            assert np.isclose(row_sums[i], 1.0), f"Row {i} of transition matrix does not sum to 1"

    # --- Test generated samples ---
    generated_seq = model.generate_samples("sunny", seed=42, length=9)
    print("\nGenerated Sequence (length 10):")
    print(generated_seq)

    assert len(generated_seq) == 10, "Generated sequence should have length 10 (length+1)."
    assert generated_seq[0] == "sunny", "Generated sequence must start with the first state."

    # --- Test stationary distribution ---
    pi = model.stationary_distribution()
    print("\nStationary Distribution:")
    print(pi)

    assert np.all(pi >= -1e-10), "Stationary distribution has negative values."
    assert np.isclose(np.sum(pi), 1.0), "Stationary distribution does not sum to 1."

    print("\n✅ All tests passed!")

if __name__ == "__main__":
    main()
