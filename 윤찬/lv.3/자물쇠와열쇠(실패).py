def right_rotate(key):
    return list(zip(*key[::-1]))

def arr_list(arr, status):
    tmp = []
    arr_size = len(arr)
    for row in range(arr_size):
        for col in range(arr_size):
            if arr[row][col] == status:
                tmp.append([row, col])
    return tmp

def check(key, lock):
    print(''.join(key))
            
def solution(key, lock):
    lock_list = arr_list(lock, 0)
    need_size = len(lock_list)
    
    for _ in range(4):
        key = right_rotate(key)
        key_list = arr_list(key, 1)
        check(key_list, lock_list)

    return False
