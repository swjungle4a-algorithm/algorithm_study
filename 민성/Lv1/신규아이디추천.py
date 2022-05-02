# 윤찬 코드

import re
def solution(new_id):
    # 1단계 - 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2단계 - 알파벳, 소문자, 숫자, 빼기(-), 밑줄(_), (.)을 제외한 모든 문자 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # 3단계 - 연속된 . 들을 . 하나로 변경하기
    new_id = re.sub('[.]+', '.', new_id)
    # 4단계 - 앞에있는 . 혹은 뒤에있는 .은 제거한다.
    new_id = re.sub('^[.]|[.]$', '', new_id)
    # 5단계 - 빈 문자열이라면 a 를 대입한다.
    new_id = 'a' if new_id == '' else new_id
    # 6단계 - 16자 이상이라면 15글자까지만 자른다.
    # 자른 후 만약 마침표가 new_id 끝에 위치한다면 끝에 위치한 마침표 제거
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = re.sub('[.]$', '', new_id)
    # 7단계 - 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙인다.
    new_id = new_id + new_id[-1]*(3-len(new_id)) if len(new_id) <= 2 else new_id
    return new_id
