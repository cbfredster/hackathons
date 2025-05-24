import random

def SelectPivotPair(L):
	
 if len(L) < 5:
 	# if original list is less than required sample size then the sorted origianl list is used to find the pivots instead
  L.sort()
  P0 = L[1]
  P1 = L[-2]
  #as i've used constant values for indexing pivots, there is potential chance of L[-2] being greater than L[1]
  # if for example array of size 2 when very far down recursive trees (then L[1] is the 2nd element in ordered list whereas L[-2] #is the 1st element in an ordered list.)
  if P0 > P1:
  	#variable switch for this 2-case
    temp = P0
    P0 = P1
    P1 = temp
  return(P0,P1)
 else:
 	# for array size greater than 5
 	#using random module function and picking 5 distinct elements (randdm.sample produces ONLY distinct)
  k = random.sample(L,5)
  k.sort()
  P0 = k[1]
  P1 = k[-2]
  return(P0,P1)

def ThreePartition(L,P0,P1):
 #initialise three empty arrays for the three sublists
 L0 = []
 L1 = []
 L2 = []
 # simple categorisation for elements between pivots generated from last function written 
 # SIZE of each of these arrays dont have to be equivalent, as pivots are sort of produced from random 5 elements from L
 for i in range(len(L)):
	 if L[i] <= P0:
	  L0.append(L[i])
	 if P0 < L[i] <= P1:
	  L1.append(L[i])
	 if L[i] > P1:
	  L2.append(L[i])
 return(L0,L1,L2)

def ThreeWayQuickSort(L):
  
  #in order for the list to be sorted using in-built functions for arrays less than #size.10, so i found the 'hasattr' function. on W3SCHOOLS to resolve this problem, as i cannot store a value in definition without it being reassigned for all future recursion
 if not hasattr(ThreeWayQuickSort, "starting"):
 	# HASATTR (in this case) associated with function itself so will NOT BE REASSIGNED EVERY RECURSION
 	
 	#the recursion defaults the starting "call" to = 0 after the first recusion (initial)
 	#so the list L in any sublist cannot satisify the IF statement, as it must also have attribute = 1.
 	
 	#given the attribute value (format hasattr(object,attribute)) a numerical value as #supposed to boolean, as this will always initiliase it begin with beacuse the ThreeWayQuickSort will not have an attribute to begin with.
    ThreeWayQuickSort.starting = 1
    
  # this checks for both conditions (less than size 10 and attribute of the function itslef (ATTRIBUTE ALWAYS TRUE)), and ASSIGNS it to zero
 if ThreeWayQuickSort.starting == 1 and len(L) <= 10:
     ThreeWayQuickSort.starting = 0 
     return sorted(L) 
    
 #BASE CASE for 0 and 1, as trivial answer for ordered sublists after this
 if len(L) <= 1:
	   return L
 
 # as the output of select pivot pair is a tuple, then i have to use indexing in order to retrive pivot values
 P0 = SelectPivotPair(L)[0]
 P1 = SelectPivotPair(L)[1]
 # similiarly with threepartition, and tuple output so yet again indexing
 L0 = ThreePartition(L,P0,P1)[0]
 L1 = ThreePartition(L,P0,P1)[1]
 L2 = ThreePartition(L,P0,P1)[2]

 orderedLzero = ThreeWayQuickSort(L0)
 orderedLone = ThreeWayQuickSort(L1)
 orderedLtwo = ThreeWayQuickSort(L2)
  #for every 3-group of sublists, once the whole recursive tree has reached roots then 3-groups wi
 return orderedLzero + orderedLone + orderedLtwo
 
assert SelectPivotPair([5,4,3,2,1]) == (2,4)

assert ThreePartition([3,2,1],1,2) == ([1],[2],[3])

print(ThreeWayQuickSort([12,11,10,9,8,7,1,2,3,4,5,6]))
