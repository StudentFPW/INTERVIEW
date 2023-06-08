list_key = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
list_item = [1, 2, 3, 4, 5, 6, 7, 8]
empty_dict = {}


def make_dict(empty, key, item):
    for n in range(len(key)):
        if n < len(item):
            empty[key[n]] = item[n]
        elif n > len(item):
            empty[key[n]] = None
        else:
            continue

    return empty


print(make_dict(empty_dict, list_key, list_item))
