import csv
import random
import sys
#Global dictionaries used in this project
results = {}
sorted_dictionary= {}
below_average = {}
over_average = {}
#Executes all the functions below
def main():
    csv_reader("new_numbers.csv")
    sorted_dict(results)
    print (f"Sorted list of all the numbers and times repeated:{sorted_dictionary}")
    average(sorted_dictionary)
    print("NUMBERS BELOW AVERAGE")
    for numbers in below_average.keys():
        print(f"{numbers} with {below_average[numbers]:.2f}%,", end = '    ')
    print()
    print()
    print("NUMBERS ABOVE AVERAGE")
    for numbers in over_average.keys():
        print(f"{numbers} with {over_average[numbers]:.2f}%,", end = '    ')
    print()
    print()

    if len(sys.argv) == 3:
        number_of_numbers = sys.argv[2]
        below_or_above = sys.argv[1]
        if sys.argv[1] == "below":
            if len(number_of_numbers) < len(below_average.keys()):
                print (f"List of {number_of_numbers} numbers below average random choices: {sorted(below_avg(below_average, number_of_numbers))}")
            else:
                sys.exit("There is no such amount of numbers below average.Pleace pick another number")
        elif sys.argv[1] == "above":
            if len(number_of_numbers) < len(over_average.keys()):
                print (f"List of {number_of_numbers} numbers above average random choices: {sorted(above_avg(over_average, number_of_numbers))}")
            else:
                sys.exit("There is no such amount of numbers over average.Pleace pick another number")
        else:
            sys.exit("Please pick into sys.argv[1] between below and above")
    else:
        sys.exit("Please insert below or above of average and the amount of numbers")


#Read a CSV file and iterates over the numbers to save them in a global dictionary counting the times the key appears in the file
def csv_reader(the_file):
    if the_file.endswith(".csv"):
        with open(the_file) as file:
            count = 1
            r = csv.reader(file)
            for row in r:
                for number in row:
                    #Deletes the key saved as " " in case the rows end with a ","
                    if number == "":
                        continue
                    #Continues appending to the dict keys and values
                    if int(number) not in results:
                        results[int(number)] = count
                    else:
                        results[int(number)] += 1
    else:
        sys.exit("Please insert a csv file")

# Creates an new dictionary from the old one sorting it by keys.
def sorted_dict(diction):
    for k,v in sorted(diction.items()):
        sorted_dictionary[k] = v
    return sorted_dictionary

# A function that his purpose in life is to calculate the average of the numbers and after add them to a dict that contains the numbers below average or a  dict that contains numbers above average for each value
def average(the_dict):
    total_numbers = 0
    the_average = 0
    for numbers in the_dict.keys():
        total_numbers += the_dict[numbers]
    print(f" All the numbers appears in the file:   {total_numbers} times")
# Adds each key with the new value(average) to the dictionary that belows
    for k in the_dict.keys():
        the_dict[k] = the_dict[k] / total_numbers * 100
    the_average = 100 / len(the_dict.keys())
    print (f"Global average: {the_average:.2f}% is the average")
    for k in the_dict.keys():
        if the_average > the_dict[k]:
            below_average[k] = the_dict[k]
        else:
            over_average[k] = the_dict[k]
    return below_average, over_average


# Return a list with random choices of keys that are below the average (including equals) with the desired amount of numbers
def below_avg(below, numbers):
    result = []
    choices = list(below.keys())
    x = 0
    while True:
        try:
            if len(result) < int(numbers):
                x = random.choice(choices)
                if x not in result:
                    result.append(x)
                    continue
                else:
                    continue
            elif len(result) == int(numbers):
                break
        except False:
            break

    return result


# Return a list with random choices of keys that are above the average (including equals) with the desired amount of numbers
def above_avg(above, numbers):
    result = []
    choices = list(above.keys())
    x = 0
    while True:
        try:
            if len(result) < int(numbers):
                x = random.choice(choices)
                if x not in result:
                    result.append(x)
                    continue
                else:
                    continue
            elif len(result) == int(numbers):
                break
        except False:
            break

    return result

#Calls main
if __name__ == "__main__":
    main()
