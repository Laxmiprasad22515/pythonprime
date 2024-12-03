# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find prime numbers in a given list
def find_primes_in_list(numbers):
    primes = [num for num in numbers if is_prime(num)]
    return primes

# Sample list of numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]

# Find and print prime numbers in the list
prime_numbers = find_primes_in_list(numbers)
print("Prime numbers in the list:", prime_numbers)

