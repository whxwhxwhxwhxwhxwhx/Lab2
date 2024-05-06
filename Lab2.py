import statistics

def display_main_menu():
    print("Welcome to the Temperature Calculator")

def get_user_input():
    x = input("Enter temp values separated by commas: ")
    num_list = x.split(", ")
    num_list = [float(x) for x in num_list]
    return num_list

def calc_average(num_list):
    # Calculate average temperature
    average = sum(num_list) / len(num_list)
    return average

def calc_median_temperature(num_list):
    median = statistics.median(num_list)
    return median

def sort_temperature(num_list):
    # Calculate sorted temperature in the list
    sort_list = sorted(num_list)
    return sort_list

def find_min_max(num_list):
    # Find minimum and maximum temperature in the list
    min_temp = min(num_list)
    max_temp = max(num_list)
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
