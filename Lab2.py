
def display_main_menu():
    print("Welcome to the Temperature Calculator")

def get_user_input():
    num_list = input("Enter temp values separated by commas: ")
    return num_list

def calc_average(num_list):
    # Calculate average temperature
    numbers = [float(num) for num in num_list.split(",")]
    average = sum(numbers) / len(numbers)
    return average

def calc_median_temperature(num_list):
    # Calculate the median temperature in the list
    numbers = sorted([float(num) for num in num_list.split(",")])
    length = len(numbers)
    if length % 2 == 0:
        #median is division of 2 middle numbers
        median = (numbers[length//2 - 1] + numbers[length//2]) / 2
    else:
        median = numbers[length//2]
        #median is only 1 middle number
    return median

def sort_temperature(num_list):
    # Calculate sorted temperature in the list
    sort_list = sorted([float(num) for num in num_list.split(",")])
    return sort_list

def find_min_max(num_list):
    # Find minimum and maximum temperature in the list
    numbers = [float(num) for num in num_list.split(",")]
    min_temp = min(numbers)
    max_temp = max(numbers)
    return min_temp, max_temp

def main():
    display_main_menu()
    num_list = get_user_input()
    #show final results
    print("Input list:", num_list)
    average = calc_average(num_list)
    median = calc_median_temperature(num_list)
    sort_list = sort_temperature(num_list)
    min_temp, max_temp = find_min_max(num_list)
    print("Average value:", average)
    print("Median temperature:", median)
    print("Sorted list:", sort_list)
    print("Min temperature:", min_temp)
    print("Max temperature:", max_temp)

if __name__ == "__main__":
    main()
