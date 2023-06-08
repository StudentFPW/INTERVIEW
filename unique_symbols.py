filename = input("")

with open(filename[5:], encoding="utf-8") as file:
    word_cnt = 0
    command = input("").split()

    if command[0] == "wordcount":
        for word in file:
            if word.replace("\n", "") == command[1]:
                word_cnt += 1
        print(word_cnt)

    if command[0] == "clear-memory":
        f = open(filename[5:], 'w', encoding='utf8')
        f.write("")
