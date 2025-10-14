import random

# Sample space: all possible outcomes when rolling a fair 6-sided die
sample_space = {1, 2, 3, 4, 5, 6}
print("Sample Space (S):", sample_space)

# Define some events
event_A = {2, 4, 6}   # Event A: rolling an even number
event_B = {1, 2, 3}   # Event B: rolling a number <= 3
event_C = {5}         # Event C: rolling exactly a 5

print("\nDefined Events:")
print("Event A (Even numbers):", event_A)
print("Event B (Numbers <= 3):", event_B)
print("Event C (Exactly 5):", event_C)

# Probability of an event
def probability(event, sample_space):
    return len(event) / len(sample_space)

# Conditional probability P(A|B)
def conditional_probability(A, B, sample_space):
    if len(B) == 0:
        return 0
    return probability(A.intersection(B), sample_space) / probability(B, sample_space)

print("\nProbability Values:")
print("P(A) =", probability(event_A, sample_space))
print("P(B) =", probability(event_B, sample_space))
print("P(C) =", probability(event_C, sample_space))

# Intersection and Union (ASCII safe)
print("\nSet Operations:")
print("A INTERSECTION B =", event_A.intersection(event_B),
      " => P(A INTERSECTION B) =", probability(event_A.intersection(event_B), sample_space))
print("A UNION B =", event_A.union(event_B),
      " => P(A UNION B) =", probability(event_A.union(event_B), sample_space))

# Conditional probabilities
print("\nConditional Probabilities:")
print("P(A | B) =", conditional_probability(event_A, event_B, sample_space))
print("P(B | A) =", conditional_probability(event_B, event_A, sample_space))

# Simulate an experiment (roll the die once)


