# http://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/
# author: Robert Sebescen (pgrobban at gmail dot com)

def make_palindromic(n):
	num_steps = 0
	while not is_palindromic(n):
		# print(n)
		sn = str(n);
		n_rev = int(sn[::-1])
		n = n + n_rev
		num_steps += 1
	return n, num_steps

def is_palindromic(n):
	sn = str(n)
	return sn == sn[::-1]

print(make_palindromic(196196871))