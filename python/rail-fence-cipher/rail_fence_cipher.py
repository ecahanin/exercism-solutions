
def encode(message, rails):
    fence = build_fence(len(message), rails)
    letters = list(message)
    for i in range(len(message)):
        for j in range(rails):
            if fence[j][i] is not None:
                fence[j][i] = letters.pop(0)
    encoded_message = ''.join(flatten_by_rows(fence))
    return encoded_message


def decode(encoded_message, rails):
    fence = build_fence(len(encoded_message), rails)
    letters = list(encoded_message)
    for i, row in enumerate(fence):
        for j, space in enumerate(row):
            if space == '_':
                fence[i][j] = letters.pop(0)
    decoded_message = ''.join(flatten_by_columns(fence)) 
    return decoded_message


def flatten_by_rows(array):
    flattened_array = []
    for row in array:
        for element in row:
            if element is not None:
                flattened_array += element
    return flattened_array


def flatten_by_columns(array):
    flattened_array = []
    for i in range(len(array[0])):
        for row in array:
            if row[i] is not None:
                flattened_array += row[i]
    return flattened_array


def build_fence(length, rails):
    fence = [[None] * length for _ in range(rails)]
    rail = 0
    down = False
    for i in range(length):
        fence[rail][i] = '_'
        if rail == rails - 1 or rail == 0:
            down = not down
        if down:
            rail += 1
        else:
            rail -= 1
    return fence
