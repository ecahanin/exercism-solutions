def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    new_list = []
    for list in lists:
        append(new_list, list)
    return new_list    


def filter(function, list):
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list.append(item)
    return filtered_list


def length(list):
    i = 0
    for item in list:
        i += 1
    return i


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    while list:
        item = list.pop(0)
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    while list:
        item = list.pop(-1)
        initial = function(item, initial)
    return initial


def reverse(list):
    return list[::-1]
