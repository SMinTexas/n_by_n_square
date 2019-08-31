# Print a NxN square of * characters. Prompt the user for N.

square = int(input("How big is the square? "))

def print_square(size_of_square, to_print):
    for number in range(0, size_of_square):
        print(size_of_square * to_print)

print_square(square,'*')