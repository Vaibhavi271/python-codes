'''
You are competing in a basketball contest. In this contest the score for each 
successful shot depends on both the distance from the basket and the player's 
position. The ball is shot N times, successfully. You are given an array A containing the 
distance of a player from basket for N shots. The index of array represents 
the position of the player. Score is calculated by multiplying the position with the 
distance from the basket.
Your task is to find and return an integer value, representing the maximum possible 
score you can achieve by choosing a contiguous subarray of size K from the given 
array.
Note:
* A subarray is a contiguous part of array.
* Assume 1 based indexing.
* The array contains both negative and positive values.
* Assume the player is standing on a cartesian plane.
Input Format
- input1:An integer value N representing the number of shots made by the player
- input2 : An integer K representing the size of subarray
- input3 : An array of integers

'''





n=int(input())
sub=int(input())
arr=list(map(int,input().split()))#12345
maxx=0
for i in range(0,n-sub+1):
    a=arr[i:i+sub]
    summ=0
    inc=1
    for j in a:
        summ=summ+(j*inc)
        inc+=1
    if summ>maxx:
        maxx=summ
print(maxx)

