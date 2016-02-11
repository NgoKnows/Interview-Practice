def is_unique(str):
    letter_set = set()

    for letter in str:
        if letter in letter_set:
            return False
        letter_set.add(letter)
    return True

is_unique("not not")

