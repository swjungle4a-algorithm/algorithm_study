def solution(numbers, hand):
    answer = ''
    leftset = set([1, 4, 7])
    rightset = set([3, 6, 9])
    dist = [[] for _ in range(10)]
    dist[2] = [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4]
    dist[5] = [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3]
    dist[8] = [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2]
    dist[0] = [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1]
    plf = 10
    prf = 11
    for num in numbers:
        if num in leftset:
            answer += "L"
            plf = num
        elif num in rightset:
            answer += "R"
            prf = num
        else:
            if dist[num][plf] < dist[num][prf]:
                answer += "L"
                plf = num
            elif dist[num][plf] > dist[num][prf]:
                answer += "R"
                prf = num
            else:
                if hand == "left":
                    answer += "L"
                    plf = num
                else:
                    answer += "R"
                    prf = num
    return answer
