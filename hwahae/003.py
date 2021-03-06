def solution(cards, words):
    answer = []
    len_card = len(cards)

    for i in range(len_card):
        cards[i] = list(cards[i])

    for w in words:
        tmp_card = [[] for _ in range(len_card)]
        cnt = 0
        for i in range(len_card):
            tmp_card[i] = list(cards[i])

        visit = [1, 1, 1]
        for i in range(len(w)):
            for j in range(3):
                if w[i] in tmp_card[j]:
                    tmp_card[j][tmp_card[j].index(w[i])] = -1
                    cnt += 1
                    visit[j] = 0

        if sum(visit) == 0 and cnt == len(w):
            answer.append(w)
    return answer if answer else ["-1"]


print(solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["GPQM", "GPMZ", "EFU", "MMNA"]))
print(solution(["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"], ["AAAKKKKKMMMMM", "ABCDKJ"]))
