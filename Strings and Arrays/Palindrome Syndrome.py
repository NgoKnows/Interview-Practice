def palindrome_syndrome(str):
    letter_count = dict()

    for letter in str:
        if letter in letter_count:
            letter_count[letter] += 1
    else:
        letter_count[letter] = 1

    odd_counts = 0
    for count in letter_count.values():
        if count % 2 != 0:
            odd_counts += 1

        if odd_counts > 1:
            return False
    if odd_counts and len(str) %2 == 0:
        return False
    return True

print(palindrome_syndrome("hihih"))
