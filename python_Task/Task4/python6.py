#problem6
HackerRank link:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
scores = list(map(int, input().split()))

unique_scores = sorted(set(scores))
print(unique_scores[-2])
