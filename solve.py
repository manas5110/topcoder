def solve(sum):
	sum_left = sum
	func_h_r = []
	h_max=0
	list_of_fhrs=[]
	while sum_left>h_max:
		h_max=h_max+1
		sum_left = sum_left - h_max
		func_h_r.append(h_max)
	r_for_h_max=h_max-1
	while sum_left>=r_for_h_max:
		sum_left=sum_left-r_for_h_max
		func_h_r.append(r_for_h_max)
		r_for_h_max=r_for_h_max-1
	r_for_h_max=r_for_h_max+1
	if sum_left==0:
		list_of_fhrs.append(func_h_r)
	list_of_fhrs=list_of_fhrs+check_for_other_h(h_max,sum)
	list_of_list_lengths=[]
	for l in list_of_fhrs:
		list_of_list_lengths.append(len(l))
	if len(list_of_fhrs)>0:
		return min(list_of_list_lengths)
	else:
 		return -1
 		
 
def check_for_other_h(in_h,in_sum):
	list_of_list_temp=[]
	for x in range(in_h-1,0,-1):
		temp_list_of_minus_one=[]
		other_list=list_till(x)
		sum_left_for_r=in_sum-sum_till(x)
		curr_sum=sum_left_for_r
		for y in range(x-1,0,-1):
			curr_sum=curr_sum-y
			if curr_sum<0:
				temp_list_of_minus_one.append(-1)
				break
			elif curr_sum==0:
				other_list.append(y)
				list_of_list_temp.append(other_list)
				break
			else:
				other_list.append(y)
				continue
	return list_of_list_temp
				
def sum_till(n):
	temp_sum=0
	for i in range(1,n+1):
		temp_sum=temp_sum+i
	return temp_sum


def list_till(m):
	list=[]
	for v in range(1,m+1):
		list.append(v)
	return list


print(solve(100000000))
 @manas5110
 Owner
manas5110 commented 6 days ago
Problem Statement :
For positive integers h and r (1 <= r <= h) we define sequence Fh,r as {1, 2, 3, ..., h-1, h, h-1, h-2, ..., r+1, r}. Let S(Fh,r) be the the sum of all numbers in Fh,r and N(Fh,r) - the length of Fh,r.

For example, F3,2 is {1, 2, 3, 2}, S(F3,2) = 1 + 2 + 3 + 2 = 8, and N(F3,2) = 4. F5,5 is {1, 2, 3, 4, 5}, S(F5,5) = 15, and N(F5,5) = 5.

You are given a sum. Return minimal possible N(Fi,j) such that S(Fi,j) = sum. If there is no such sequence Fi,j, return -1 instead.

Definition
Class: AnEasyProblem
Method: solve
Parameters: long integer
Returns: integer
Method signature: def solve(self, sum):
Limits
Time limit (s): 2.000
Memory limit (MB): 256
Constraints

sum will be between 1 and 1,000,000,000,000(10^12).
Examples
6
Returns: 3
When h = r = 3, S(Fh,r) = 6 and N(Fh,r) = 3. There is no other h,r satisfing S(Fh,r) = 6. So you should return 3.
1)
7
Returns: -1
2)
100
Returns: 15
3)
1000000000000
Returns: 1428571
