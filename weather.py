import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# myresult=format_temperature("5")
# print(myresult)


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    my_datetime_object=datetime.fromisoformat(iso_string)
    date_formatted = my_datetime_object.strftime('%A %d %B %Y')

    return date_formatted

# myresult=convert_date("2021-07-05T07:00:00+08:00")
# print(myresult)


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    temp_in_f_to_c= (float(temp_in_farenheit) - 32) * 5/9
    # return temp_in_f_to_c
    return round(temp_in_f_to_c,1)

# print(convert_f_to_c(350))




def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.


    """
    sum=0
    for data in weather_data:
        sum += float(data)

    mean_value=(sum/len(weather_data))

    return mean_value

# print(calculate_mean([3,5,7]))




def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    information_list = []

    

    print(csv_file)
    with open(csv_file) as this_file:
        my_reader = csv.reader(this_file) # take the information from the file
        next(my_reader) # This command is going to skip one line

        for line in my_reader:
            if line == []:
                continue
            date,min,max = line 
            information_list.append([date, float(min), float(max)]) # we append a list into a list and this list contains three items
            print(line)

    return information_list

result = load_data_from_csv ("tests/data/example_one.csv")



print(result)
    




def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()

    min = float(weather_data[0])# minimum value so far in the list 
    min_i = 0
  
    for i in range(1,len(weather_data)):

          if float(weather_data[i]) <= min:
            min = float(weather_data[i]) 
            min_i = (i)

    return (min, min_i)


    ## TRYING TO DO MIN VALUE FROM STRING TO FLOAT

  


# print(find_min([49, 57, 56, 55, 53]))

# print(find_min([10, -8, 2, -16, 4]))

# print(find_min([10.4, 14.5, 12.9, 8.9, 10.5, 11.7]))



# print(find_min(["49", "57", "56", "55", "53", "49"]))

# print(find_min([49, 57, 56, 55, 53, 49]))

# print(find_min([]))




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()

    max = float(weather_data[0]) # maximum value so far in the list 
    max_value = 0
  
    for i in range(1,len(weather_data)):
        if float(weather_data[i]) >= max:
            max = float(weather_data[i])
            max_value = i
    return (max, max_value)


# print(find_max([49, 57, 56, 55, 53]))


# print(find_max([-10, -8, 2, -16, 4]))

# print(find_max([10.4, 14.5, 12.9, 8.9, 10.5, 11.7]))

# print(find_max(["49", "57", "56", "55", "53", "49"]))

# print(find_max([49, 57, 56, 55, 53, 49]))

# print(find_max([]))




def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    # """
    newline_twospaces = "\n  "
    # min_temp
    # min_temp_average
    # max_temp
    # max_temp_average

    date_list = []  # dates in weather_data
    min_list = []  # minimums in weather_data
    max_list = [] # maximum in weather_data

    # we extract the information with a loop

    for information in weather_data:  # building list
        date_list.append(information[0])
        min_list.append(information[1])
        max_list.append(information[2])


    ## use the find_min to find the minimum temperature (AND ITS POSITION)
    ## minimum date

    min_and_position = find_min(min_list)  # our function gives us 2 values! position, and temperature

    min_position = min_and_position[1]  # its a number e. g. 0
    min_date = date_list[min_position]
    min_date = convert_date(min_date) # convert the date into a human redeable format

    # # min temperature

    min_temp = min_and_position[0]  # extracting the minimum e.g. 49
    min_temp = convert_f_to_c(min_temp)  # converting minimum to celsius e.g. 9.4
    min_temp = format_temperature(min_temp)  # adding degree celsius


    ## use the find_max to find the maximum temperature (AND ITS POSITION)

    ## maximun date

    max_and_position = find_max(max_list)  # our function gives us 2 values! position, and temperature

    max_position = max_and_position[1]  # its a number e. g. 0
    max_date = date_list[max_position]
    max_date = convert_date(max_date) # convert the date into a human redeable format

    # # max temperature

    max_temp = max_and_position[0]  # extracting the minimum e.g. 49
    max_temp = convert_f_to_c(max_temp)  # converting minimum to celsius e.g. 9.4
    max_temp = format_temperature(max_temp)  # adding degree celsius

    ## Average low temperature

    min_temp_average = float(sum(min_list)/len(min_list))  #Give tha average low temperature in isotring format
    min_temp_average= convert_f_to_c(min_temp_average) #we convert the average low temperature in celcius grades
    min_temp_average = format_temperature(min_temp_average) #we format the isostring format into a redeable human format
   



    ## Average high temperature

    max_temp_average = float(sum(max_list)/len(max_list)) #Give tha average max temperature in isotring format
    max_temp_average= convert_f_to_c(max_temp_average) #we convert the average max temperature in celcius grades
    max_temp_average = format_temperature(max_temp_average) # we format the isostring format into a redeable human format



    #calculating the amount of days

    days_amount = len(weather_data)

    # CREATING THE OUTPUT SUMMARY

    # summary = str(days_amount) + "Day Overview" + \n + 


    # creating the first line of the summary

    summary = str(days_amount) + " Day Overview"  # e.g. 5 Day Overview

    # Adding the second line of code (min temperature value with the day that was min temperature)

    summary += newline_twospaces  # one line down + 2 spaces
    summary += "The lowest temperature will be "  # starting to write 2nd line
    summary += min_temp
    summary += ", and will occur on "
    summary += min_date
    summary += "."

    # Adding the third line of code (max temperature value with the day that was max temperature)

    summary += newline_twospaces  # one line down + 2 spaces
    summary += "The highest temperature will be "
    summary += max_temp
    summary += ", and will occur on "
    summary += max_date
    summary += "."


     # Adding the four line of code (The average low temperature)

    summary += newline_twospaces  # one line down + 2 spaces
    summary += "The average low this week is "
    summary += min_temp_average
    summary += "."


    # Adding the fith  line of code (The average high temperature)

    summary += newline_twospaces  # one line down + 2 spaces
    summary += "The average high this week is "
    summary += max_temp_average
    summary += ".\n" 

    return summary


result = generate_summary(
    [
        ["2021-07-02T07:00:00+08:00", 49, 67],
        ["2021-07-03T07:00:00+08:00", 57, 68],
        ["2021-07-04T07:00:00+08:00", 56, 62],
        ["2021-07-05T07:00:00+08:00", 55, 61],
        ["2021-07-06T07:00:00+08:00", 53, 62],
    ]
)
print(result)
    




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    output = "" # This is for initialize as an empty list

    # This is a loop for getting the information of the weather in one day given the minimum and maximum temperature
    # \n new line
    # \ at the end split one string into multiple lines

    for data in weather_data:
        output += f"---- {convert_date(data[0])} ----\n\
  Minimum Temperature: {format_temperature(convert_f_to_c(data[1]))}\n\
  Maximum Temperature: {format_temperature(convert_f_to_c(data[2]))}\n\n"
    
    return output


# print(generate_daily_summary(
#     [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]

# )
# )

    
