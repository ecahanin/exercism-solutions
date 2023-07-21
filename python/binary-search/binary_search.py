def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError('not contained in list')
    i = len(search_list)//2
    if value == search_list[i]:
        return i
    elif value < search_list[i]:
        return find(search_list[:i], value)
    elif value > search_list[i]:
        return find(search_list[i+1:], value) + i + 1

    
