# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.



def sum_to_num(to=1000):
    def is_mult_35(num):
        return num % 3 == 0 or num % 5 == 0

    return sum(i for i in range(3, to) if is_mult_35(i))

print(sum_to_num(1000))
