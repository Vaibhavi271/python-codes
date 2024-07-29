'''
Alice has a mathematics test for which she is underprepared. She has to do at least 
one question correctly to pass the test. He decides to do a question which needs her 
to find the smallest prime number which is larger than a given integer N. Your task is 
to find and return an integer value representing the smallest prime number larger 
than N.
Input Format:
input1: An integer value N
Output Format:
Return an integer value representing the smallest prime number larger than N.
Sample Input
6
Sample Output
7
'''

n=int(input())
while True:
    n=n+1
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print("next primenumber :{}".format(n))
        break
