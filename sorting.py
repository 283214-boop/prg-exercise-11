import random


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    n = 0
    while n < len(values):
        min_index = n
        min_value = values[min_index]
        for x in range(n+1, len(values)):
            if values[x] < min_value:
                min_index = x
                min_value = values[x]
        print(values)
        values[n], values[min_index] = values[min_index], values[n]
        n+=1
    print(values)

def bubble_sort(values):
    n = len(values)-1
    for i in range(len(values)):
        index=i
        if values[index]>values[index+n]:
           values[n], values[index] = values[index+n], values[n]
    print (values)






if __name__=="__main__":
    values = random_numbers(10)
    # print(values)
    small = random_numbers(5, low=0, high=20)
    # print(small)
    selection_sort(values)
    bubble_sort(values)