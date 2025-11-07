def unique_list(list):
    for idx in list:
        if idx == " ":
            continue
        elif idx in new_list:
            continue
        else:
            new_list.append(idx)

    return new_list

list = input()
new_list = []
print(unique_list(list))