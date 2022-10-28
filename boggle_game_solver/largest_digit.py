"""
File: largest_digit.py
Name: Lydia
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: an integer
	:return: the biggest digit in n
	"""
	return find_largest_digit_helper(n, -float('inf'))  # -float('inf') is a floating-point negative infinity


def find_largest_digit_helper(n, biggestnum):
	if n < 0:  # if n is negative, make it positive
		n = n * -1
	if n == 0:  # base case, which means we have compared all the digits in n
		return biggestnum
	else:
		if n % 10 > biggestnum:  # % to get the last digit
			biggestnum = n % 10
		number = n // 10  # // to remove the last digit
		return find_largest_digit_helper(number, biggestnum)


if __name__ == '__main__':
	main()
