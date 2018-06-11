#	An obtuse triangle is a triangle in which one of the internal angles has strictly more than 90 degrees. Equivalently, a triangle with side lengths a ≤ b ≤ c is obtuse if and only if c^2 > a^2 + b^2.			
#	You have 3*n sticks: for each integer x between a and a+3*n-1, inclusive, you have one stick of length x. You want to use these 3*n sticks to build n disjoint obtuse triangles. (Hence, each stick has to be used as a side of exactly one of the triangles.)			
#	You are given the ints a and n. Find out whether it is possible to construct n disjoint obtuse triangles, and if it is, construct one such set. If there is no solution, return an empty long[]. Otherwise, return a long[] constructed as follows:			
#	Suppose (x1, y1, z1), (x2, y2, z2), ..., (xn, yn, zn) is your way to construct n obtuse triangles. Then, return the following long[]: 			
#	{ 			
#				
#	x1*108 + y1*104 + z1, 			
#				
#	x2*108 + y2*104 + z2, 			
#				
#	..., 			
#				
#	xn*108 + yn*104 + zn 			
#				
#	}.			
#	If there are many ways to construct n obtuse triangles while using each stick exactly once, you may choose any one of them. Within each triangle, the order of the three sticks in your answer does not matter.			
#				
#	Definition			
#	  Class:		ObtuseTrianglesDiv1
#		Method:		findObtuseTriangles
#		Parameters:		int, int
#		Returns:		long[]
#		Method signature:		long[] findObtuseTriangles(int a, int n)
#		(be sure your method is public)		
#
#	Constraints			
#	-	a will be between 1 and 10, inclusive.		
#	-	n will be between 1 and 500, inclusive.		
#				
#	Examples			
#	0)			
#	    	2		
#		1		
#		Returns: {200030004 }		
#		Ordering of the three sticks within a triangle does not matter, so {300040002} is another correct answer.		
#	1)			
#	    	3		
#		1		
#		Returns: { }		
#		Using three sticks of length 3, 4, and 5, respectively, we can only create a right triangle, but not an obtuse triangle.		
#	2)			
#	    	2		
#		2		
#		Returns: {200040005, 300070006 }		
#		We have sticks of length 2, 3, 4, 5, 6, and 7, respectively. The return value shown above describes the obtuse triangles (2,4,5) and (3,6,7).		
#				
#				
#		Ordering of the elements in the returned array does not matter, so {300070006, 200050004} is another correct answer.		
#	3)			
#	    	10		
#		6		
#		Returns: {1000160025, 1100170024, 1200190023, 1300210026, 1400150022, 1800200027 }		
#				
#	4)			
#	    	8		
#		5		
#		Returns: {800130020, 900140019, 1000170021, 1100120018, 1500160022 }
