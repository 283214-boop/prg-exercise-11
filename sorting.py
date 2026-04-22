import random
import matplotlib.pyplot as plt

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
    return values

def bubble_sort(values):
    plt.ion()
    plt.show()
    for j in range(len(values)):

        for n in range(len(values)-1):

            if values[n] > values[n+1]:
                values[n], values[n+1] = values[n+1], values[n]
            index_highlight1 = n
            index_highlight2 = n + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return values






if __name__=="__main__":
    values = random_numbers(100)
    print(values)
    small = random_numbers(5, low=0, high=20)
    # print(small)
    # selection_sort(values)
    bubble_sort(values)