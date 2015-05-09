# Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 
# (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
# naive approach
# author: Robert Sebescen (pgrobban at gmail dot com)

import itertools

all_combinations = []
for number in "123456789":
	if number != "9":
		signs = ["", "+", "-"]
	else:
		signs = [""]
	sub_combinations = []
	for sign in signs:
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
	cross_product_strings.append(string_to_calculate)

result = [i for i in cross_product_strings if eval(i) == 100]
for i in result:
	print(i)

