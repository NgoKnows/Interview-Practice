def palindrome_distance(str1):
    front_idx = 0
    end_idx = len(str1) - 1
    total = len(str1)
    # while front_idx <= end_idx:
    for front_idx in range(len(str1)//2):
        if front_idx == end_idx:
            total -= 1
            front_idx +=1
        elif str1[front_idx] == str1[end_idx]:
            total -= 2
            front_idx +=1
            end_idx -= 1
        else:
            total = len(str1)
            front_idx += 1
            back_idx = len(str1) - 1
    print(total)

palindrome_distance("afaba")