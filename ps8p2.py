# Fibonacci sequence using a for loop

# Constants
NUM_NUMBERS = 20

# Initialize variables
first = 1
second = 1

# Print the first two numbers (1, 1)
print(first)
print(second)

# Compute and display the rest of the sequence
for _ in range(2, NUM_NUMBERS):
    next_number = first + second
    print(next_number)
    first = second
    second = next_number