#!/usr/bin/python3

def removefalsy(_list):
    rsult = list(filter(None,_list))
    print(rsult)
    return rsult

if __name__ =="__main__":
    data = [0, 1, False, 2, '', 3, 'a', 's', 34]
    removefalsy(data) == [ 1, 2, 3, 'a', 's', 34 ]
    
