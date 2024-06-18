import re

def read_temperatures(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    temp = line.strip().split(',')
                    temp_pattern = re.compile(r"(\d{1,2})°")
                    degrees = [int(temp_pattern.search(x).group(1)) for x in temp] 
                    return degrees
                except ValueError:
                    print(f"Skipping invalid temperature entry: {line.strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")
    


def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0
    return sum(temperatures) / len(temperatures)

def main():
    temp1 = read_temperatures("Weather2020.txt")
    temp2 = read_temperatures("Weather2021.txt")

    avg_temp1 = calculate_average_temperature(temp1)
    avg_temp2 = calculate_average_temperature(temp2)

    if avg_temp1 > avg_temp2:
        return f"The average temp for 2020 is {avg_temp1}, which is higher than 2021"
    else:
        return f"The average temp for 2021 is {avg_temp2}, which is higher than 2020"

print(main())
