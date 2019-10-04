"""
Minimal working example for puzzle_tools library
"""


from puzzle_tools import * # import the puzzle_tools library


@puzzle #use decorate to signify that a function is a puzzle
def puzzle_goosebump(): # name the function "puzzle_<answer>" such that the answer is the solution to the puzzle
	"Sometimes, the answers lies in not one beginning, but all of them." # Put the hint in the functions docstring

	# use some form of encryption to encrypt some information
	data = """go to the beginning\nor never finish\noh just maybe\nsince then\neverythings changed\nbelieve me or not\nuniversally\nmaybe just then\npolish the change"""


	write_clue(data) # write said data into a clue file

	# import image from a converted image. see image.py for help
	from img import data
	write_png(data, (50,50)) # pass data and size to the function, optional mode, see PIL docs

if __name__ == '__main__':
	main()
