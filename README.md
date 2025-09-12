# Purpose of Markov Chain

Markov chains are a tool in statistical modeling with applications in a variety of fields

## Objective

- Construct a Markov chain from an input sequence to analyze patterns in the given sequence
- Design a context-aware application
- Identify the advantages of using context in applications
- Discuss various types of mobility models

## Description

In this project, you will be given an input sequence of daily weather patterns, categorized into multiple groups.

Using that sequence of data, you will extract the probability distribution corresponding to transitions, build the Markov chain, generate new data, and compute the stationary distribution of the Markov chain in order to gain information abou the input data sequence.

The stationary distribution represents the long-term behavior of the Markov chain.

It is defined as the vector pi, such that pi * P = pi, where P is the transition matrix.

The recommended method for this assignment makes use of the eigenvalue/eigenvector equation:

``` 𝑀𝑣 = λ𝑣 for matrix M, eigenvector v and eigenvalue λ ```

Transform the original equation by taking the transpose of both sides:

``` (pi*P)^T = pi^T => P^T*pi^T = pi^T ```

Thus, pi is the eigenvector of the transpose of the transition matrix corresponding to eigenvalue 1

** Remember that you may still need to normalize this vector since it is a probability distribution.

## Directions

- [ ] All methods should be defined within a class named A1 (and therefore take as input self as an additional first parameter.  If an instruction requests two parameters, you would have self and those two.)
- [ ] Please name your file a1.py
- [ ] Define a method generate_markov_chain that takes as input two lists of strings, a list of potential states, and a sequence of states.  You should store the list of potential states for later, to help with indexing the transition matrix in a later method.  **In this method, you should generate the transition matrix and store it as a 2d NumPy array of floats.  Store this as a variable transition_matrix for later use.  Your method should return this array.
- [ ] Define a method generate_samples that takes as input a string representing the first state and two integers, a random seed and a length.  It should return a list of strings containing the generated sequence.  If the input length is nine (9), the generated sequence should start with the input string state and be a total of ten (10) states long. Look at a and b sublist.
- [ ] Define a method stationary_distribution that computes and returns the stationary distribution (also called steady-state vector) as a 1d NumPy array.  The stationary distribution is defined above in the Description section.  Generate it, ensuring it is normalized, and return it.
      
