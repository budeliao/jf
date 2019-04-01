print(1)
print(2)
print('坤哥牛逼')


def quick_sort(li):
    for i in range(len(li), 1, -1):
        swap_num = 0
        for j in range(i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swap_num += 1
        if swap_num == 0:
            return



if __name__ == '__main__':
    li = [9,8,7,6,5,4,3,2,1,2,3,4,6,8,45,63]
    quick_sort(li)
    print(li)