#	Andrew has a combination lock. The lock consists of multiple dials that are placed next to each other. Each dial contains the digits 0 through 9, in order. At any moment, exactly one of the digits on each dial is visible. The string formed by the currently visible digits is called the current combination.
#	The visible digit on a dial can be changed by rotating the dial up or down. Rotating the dial up changes 0 to 1, 1 to 2, and so on. Note that the digits on a dial wrap around: if we rotate up a dial that shows a 9, it will show a 0 again. Naturally, rotating the dial down changes the digit in the other direction.
#	We are able to rotate multiple dials at the same time, as long as they are next to each other. More precisely, in a single turn we can take an arbitrarily long segment of consecutive dials, and rotate all of them one step in the same direction (i.e., either all of them up, or all of them down).
#	For example, suppose that the current combination is "123". In one step, we can change it to many different combinations, including "012" (all three dials down), "234" (all three dials up), "133" (middle dial up), and "013" (first two dials down). Note that we cannot change "123" to "224" in a single step.
#	You are given two String[]s: P and Q. Concatenate the elements of P to get S. S is the current combination. Concatenate the elements of Q to get T. T is the secret combination that unlocks the lock. That is, to open the lock we need to change S into T by rotating some of the dials. Return the smallest number of steps needed.
#	Definition
#	Class: CombinationLockDiv1
#	Method: minimumMoves
#	Parameters: String[], String[]
#	Returns: int
#	Method signature: int minimumMoves(String[] P, String[] Q)
#	(be sure your method is public)
#	Constraints
#	P and Q will each contain no more than 50 elements.
#	Each element of P and Q will contain no more than 50 characters.
#	S will contain at least 1 character.
#	S will contain the same number of characters as T.
#	Each character in S and T will be a digit ('0'-'9').
#	Examples
#	0)
#	{"123"}
#	{"112"}
#	Returns: 1
#	Rotate the last two dials down.
#	1)
#	{"1"}
#	{"7"}
#	Returns: 4
#	Rotate the dial down 4 times: from 1 to 0, from 0 to 9, from 9 to 8, and from 8 to 7.
#	2)
#	{"6","07"}
#	{"","60","7"}
#	Returns: 0
#	3)
#	{"1234"}
#	{"4567"}
#	Returns: 3
#	4)
#	{"020"}
#	{"909"}
#	Returns: 2
#	5)
#	{"4423232218340"}
#	{"6290421476245"}
#	Returns: 18
def minimumMoves(x,y):
	lx=[int(list(x)[p]) for p in range(0,len(list(x)))]
	print('LX is : '+str(lx))
	ly=[int(list(y)[q]) for q in range(0,len(list(y)))]
	n=len(lx)
	for step in range(1,10):
		print('Step is '+str(step)+' currently ====================')
		for window in range(1,n+1):
			print('Window is '+str(window)+' now ------------------------------------')
			for start_pt in range(0,n+1-window):
				temp_x=lx[:]
				print('Start_pt is '+str(start_pt)+' now.')
				for k in range(start_pt,start_pt+window):
					temp_x[k]=int(temp_x[k])+step
				if temp_x == ly:
					print('Lock combination is : Window - '+str(window)+', Start point - '+str(start_pt))
					return step
				else:
					continue

print(minimumMoves('123456','127856'))
