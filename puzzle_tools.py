"""
	loads a text file <'input.txt'> and
	encrupts it using custom methods
	and outputs into <'output.txt'>
"""

import os
from PIL import Image

all_puzzles = []

def _printif(stat, cond):
    if cond: print(stat);

def _req_file(filename):
	if not os.path.isfile(filename):
		with open(filename, 'w') as f:
			pass
		return

def write_png(data, size, mode = 'RGB', filename = 'clue.png'):
	"""
	writes a (str) image into a file

	write_png(data, size, mode = 'RGB', filename = 'clue.txt') -> None
	"""
	im = Image.frombytes(mode, size, bytes(data,'utf-8'), )
	im.save(filename)

def write_clue(data, filename = 'clue.txt'):
	"""
	writes a clue into a file

	write_clue(data, filename = 'clue.txt') -> None
	"""
	with open(filename, 'w') as f:
		f.write(data)

# remove all files titled <clue>
def _remove_clues():
	for file in os.listdir():
		if file.startswith('clue'):
			os.remove(file)


# decorator function for puzzles
# adds puzzle to all_puzzles list, and resets all clue files
def puzzle(func):

	def wrapper():
		_remove_clues()
		func()

	all_puzzles.append(wrapper)
	wrapper.__name__ = func.__name__
	wrapper.__doc__ = '[?] ' + func.__doc__
	return wrapper

def _check_solutions():

	with open("solution.txt", 'r') as file:
		solutions = (line for line in file.readlines())

	# count how many correct answers in solutions.txt
	c = 0
	for solution in solutions:
		# if the given solution is equal to the name of the function, without the 'puzzle_',
		if solution.strip() == all_puzzles[c].__name__[7:]:
			c += 1 # increase correct answer counter
		else:
			break
	return c

def main():
	_req_file('solution.txt')
	cs = _check_solutions()

	for i in range(cs):
		print('[+] Puzzle %d solved' % (i+1))

	done = False
	try:
		cur_puzzle = all_puzzles[cs]
		cur_puzzle()
		print('[%s] Starting puzzle %s...\n[%s] Check clue file\n' % ('%', cs + 1 , '%'))
	except IndexError:
		print("[+] All puzzles complete!")
		done = True

	_printif('[+] Add your solution to "solution.txt" file\n', not done)
	print('[.] Press enter to continue...')
	_printif("[?] or type 'help' to get a hint for the current puzzle\n", not done)

	inp = input()

	if not done:
		hint_kws = ['help', 'hint', 'h', '?']
		if inp.strip() in hint_kws:
			print(cur_puzzle.__doc__)
			input()

if __name__ == '__main__':
	pass;
