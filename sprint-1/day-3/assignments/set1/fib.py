def fibonacci_sequence(length):
    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

sequence_length = 5
fibonacci_result = fibonacci_sequence(sequence_length)
print(fibonacci_result)
