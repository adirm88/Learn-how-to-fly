
def amir_15_5_3():
    a = []
    for i in range(0, 100):
        if i == 0: continue
        if i % 15 == 0:
            print(i)
        if i % 3 == 0 and i % 5 == 0: continue
        if i % 3 == 0:
            a.append(i)
        if i % 5 == 0:
            a.append(i)
    for x in a:
        print(x)



if __name__ == '__main__':
    amir_15_5_3()