#Q2. Given a = [1,2,3,4] and b = [10,20,30,40], build a list of the pairwise sums.
a = [1,2,3,4]
b = [10,20,30,40]
sum = [x+y for x,y in zip(a,b)]
print(sum)