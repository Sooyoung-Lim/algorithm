import sys
sys.stdin = open('input.txt')

def BubbleSort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = BubbleSort(numbers)
    print('#{} {}'.format(tc, result))



