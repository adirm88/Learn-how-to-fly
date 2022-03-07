import json

def amir_15_5_3():
    a = []
    for i in range(0, 100):
        if i == 0:
            continue
        if i % 15 == 0:
            print(i)
        if i % 3 == 0 and i % 5 == 0:
            continue
        if i % 3 == 0 or i % 5 == 0:
            a.append(i)
    for x in a:
        print(x)


def parse_to_json():
    my_text_file = open("MyTextFile.txt", 'r')
    new_dict = {}
    iterrable_array = []

    for line in my_text_file:
        iterrable_array.append(line.replace("\n", ""))
    for i in range(len(iterrable_array)):
        if i % 2 == 0:
            new_dict[iterrable_array[i]] = None
        else:
            new_dict[iterrable_array[i - 1]] = iterrable_array[i]
    my_text_file.close()
    print('this is my new dictionary: \n', new_dict)
    return json.dumps(new_dict)


if __name__ == '__main__':
    # amir_15_5_3()
    parse_to_json()