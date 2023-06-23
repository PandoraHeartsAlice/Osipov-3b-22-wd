first_ans = input()
second_ans = input()


def revver(first_list, second_list):
    list = []
    list.append(first_list[0].upper())
    list.append(second_list[0].upper())
    return list


print(revver(first_ans, second_ans))
