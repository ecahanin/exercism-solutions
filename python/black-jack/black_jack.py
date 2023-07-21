
def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 == v2:
        return (card_one, card_two)
    elif v1 > v2:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    value_of_hand = value_of_card(card_one) + value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        value_of_hand += 10
    if value_of_hand > 10:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    return (card_one == 'A' and value_of_card(card_two) == 10) or \
        (card_two == 'A' and value_of_card(card_one) == 10)


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
