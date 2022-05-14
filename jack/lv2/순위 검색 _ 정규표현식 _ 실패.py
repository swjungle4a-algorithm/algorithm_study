import re

def solution(info, query):
    answer = []
    applicants = set(range(len(info)))
    lang = {x : set() for x in ["cpp", "java", "python"]}
    pos = {x : set() for x in ["backend", "frontend"]}
    career = {x : set() for x in ["junior", "senior"]}
    food = {x : set() for x in ["chicken", "pizza"]}
    lang["-"] = applicants
    pos["-"] = applicants
    career["-"] = applicants
    food["-"] = applicants
    score = [0] * len(info)

    for idx, applicant in enumerate(info) :
        l, p, c, f, s = applicant.split()
        lang[l].add(idx)
        pos[p].add(idx)
        career[c].add(idx)
        food[f].add(idx)
        score[idx] = int(s)

    for q in query :
        q = re.sub("and ", "", q)
        l, p, c, f, s = q.split()
        found = (lang[l] & pos[p]) & (career[c] & food[f])
        
        answer.append(sum(map(lambda x: 1 if score[x] >= int(s) else 0, found)))
    return answer
