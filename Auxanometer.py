#Class Name : Auxanometer Method Name : countIncreasingMarks 
#Return Type : integerArg Types : (integer, integer)
#Problem Area
#Problem Statement
#An auxanometer is a device inside a medical cabinet used for measuring height. It is divided vertically into equal 1 centimeter segments. The segments are labeled differently on each side of the device. The left side is used to measure the height of an adult standing on the floor, and the right side is used to measure the height of a child standing on a footstool directly beneath the device. The segments on the left side are labeled nmin to nmax, inclusive, from bottom to top. The segments on the right side are labeled 1 to nmax-nmin+1, inclusive, from bottom to top.
#
#Your task is to determine the number of segments where the concatenation of the number on the left and the number on the right forms a non-decreasing sequence of digits. For example, if the number on the left is 168 and the number on the right is 89, the concatenation is 16889, a non-decreasing sequence of digits. Return the number of such segments on the given auxanometer.
#
#Definition
#Class: Auxanometer
#Method: countIncreasingMarks
#Parameters: integer, integer
#Returns: integer
#Method signature: def countIncreasingMarks(self, nmin, nmax):
#Limits
#Time limit (s): 840.000
#Memory limit (MB): 64
#Constraints
#- nmin and nmax will be between 1 and 10^9, inclusive.
#- nmin will be strictly less than nmax.
#Examples
#0)
#1
#9
#Returns: 9
#Here, the numbers on the left and right are the same. They both go from 1 to 9, so their concatenations are 11, 22, ..., 99, all of which are non-decreasing sequences of digits.
#1)
#2
#10
#Returns: 0
#Here, the numbers on the left side go from 2 to 10, and the corresponding numbers on the right side go from 1 to 9. None of the concatenations (21, 32, ..., 98, 109) are non-decreasing sequences of digits.
#2)
#1090
#1112
#Returns: 2
#There are only two satisfactory segments here: 1111-22 and 1112-23.
#3)
#80
#169
#Returns: 13
