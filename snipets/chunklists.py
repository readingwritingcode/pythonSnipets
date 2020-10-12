#!/usr/bin/python3

list_for_chunk = [1,2,3,4,5,6,7,8,9,10]

def chunk_list(_list,size):
    result= [_list[i:i+size] for i in range(0, len(_list), size)]
    print(result)
    return result

if __name__ == "__main__":
    
    list_for_chunk = [1,2,3,4,5,6,7,8,9,10]
    assert chunk_list(list_for_chunk,5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
