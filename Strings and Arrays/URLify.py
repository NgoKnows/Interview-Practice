def urlify(str):
    return "%20".join(str.strip().split())

print(urlify("reddit blah    balh test "))