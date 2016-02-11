def compress(string):
    cur = ""
    count = 0
    compressed_string = ""

    for letter in string:
        if letter == cur:
            count += 1
        else:
            if count != 0:
                compressed_string += cur + str(count)
                cur = letter
                count = 1
                if len(compressed_string) >= len(string):
                    return string

            else:
                cur = letter
                count = 1
    compressed_string += cur + str(count)
    return compressed_string

print(compress("abbcd"))
