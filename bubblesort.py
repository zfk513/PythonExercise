import random
def bubbleSort(numlist):
  for passnum in range(len(numlist)-1,0,-1):
    for i in range(passnum,0):
     if numlist[i]>numlist[i+1]:
         numlist[i],numlist[i+1],=numlist[i+1],numlist[i];
		 


def numlist(a):
  for a in range(0,9):
        numlist[a]=random.randrange(0,999,1);
bubbleSort(numlist)
print(numlist)
