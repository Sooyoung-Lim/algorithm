import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    costs = list(map(int, input().split()))[::-1]

    answer = 0
    now_max = costs[0]
    for j in range(1, N):
        if now_max > costs[j]:
            answer += now_max - costs[j]
        else:
            now_max = costs[j]

    print('#{} {}'.format(tc, answer))

