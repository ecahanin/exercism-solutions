from collections import Counter

def total(basket):
    book_cost = 800
    discounts = {
        1: 0,
        2: 5,
        3: 10,
        4: 20,
        5: 25
    }

    groupings = [set()]
    while basket:
        book = basket.pop()
        for grouping in groupings:
            if book not in grouping:
                grouping.add(book)
                book = 0
        if book:
            groupings.append({book})
    
    total_cost = 0
    for group in groupings:
        cost = book_cost * len(group) * (100 - discounts[len(group)])/100
        total_cost += cost

    return total_cost


    












