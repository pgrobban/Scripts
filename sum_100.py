# Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 
# (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
# naive approach
# author: Robert Sebescen (pgrobban at gmail dot com)

import itertools

all_combinations = []
for number in "123456789":
	sub_combinations = []
	for sign in ["", "+", "-"]:
		s = "{0}{1}".format(number, sign)
		sub_combinations.append(s)
	all_combinations.append(sub_combinations)
# print(all_combinations)
# print()

# make strings of cross product of all combinations, i.e. "123+45-67+8-9"
cross_product = itertools.product(*all_combinations);
cross_product_strings = []

for i in cross_product:
	string_to_calculate = "".join(i)
	if string_to_calculate.endswith("+") or string_to_calculate.endswith("-"):
		string_to_calculate = string_to_calculate[0:-1]
		cross_product_strings.append(string_to_calculate)
		# print(string_to_calculate)

# print("\n"*3)

# for i in cross_product:
# 	result = eval(i)
# 	if result == 100:
# 		print(i, "=", result)

print([i for i in cross_product_strings if eval(i) == 100])

#print(cross_product_strings)