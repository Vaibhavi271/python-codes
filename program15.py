'''
Andrew has a string N consisting of lowercase English letters representing respective grades of N 
students in his class. His grade is at Pth index. He can swap any two adjacent grades.
Your task is to help Andrew find and return a string value, representing maximized grade by 
bringing lexicographically smallest character on the Pth index after doing at most K swaps
Sample Input:
abcdefg
3
2
Sample Output:
a
'''
a=input()
pos=int(input())
adj=int(input())
start=max(0,pos-adj-1)
end=min(len(a)-1,pos+adj)
print(min(a[start:end]))