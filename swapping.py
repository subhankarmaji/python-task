x=10
y=5
print("Before Swap "+a+" & "+b)
#x,y=y,x
# Code to swap 'x' and 'y' 
x = x ^ y; # x now becomes 15 (1111) 
y = x ^ y; # y becomes 10 (1010) 
x = x ^ y; # x becomes 5 (0101) 
  
print("after swapping values of x and y are ",x,y)
