import numpy as np
import matplotlib.pyplot as plt
import random

def calculate_average(num_list):
    total = 0
    for i in num_list:
        total += i
    return total / len(num_list)

def get_data():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 100]
    return data

def clean_data(data_list):
    clean = []
    for val in data_list:
        if isinstance(val, int):
            clean.append(val)
    return clean

def calculate_sum(numbers):
    sum_val = 0
    for number in numbers:
        sum_val += number
    return sum_val

def plot_graph(data):
    plt.plot(data)
    plt.title("Data Graph")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

def print_stats(numbers):
    average = calculate_average(numbers)
    sum_of_numbers = calculate_sum(numbers)

def main():
    mydata = get_data()
    cleanlist = clean_data(mydata)
    print_stats(cleanlist)
    plot_graph(cleanlist)
    print("Your code build successfully ✅")

if __name__ == "__main__":
    main()
