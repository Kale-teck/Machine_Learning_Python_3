## 1. Extract Values from Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(number):
    list_data = []
    for row in apps_data[1:]:
        data = row[number]
        list_data.append(data)
    return list_data

genres = extract(11)
print(genres)
    

## 2. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

def freq_table(list_input):
    frequency_dict = {}
    for keys in list_input:
        if keys in frequency_dict:
            frequency_dict[keys] += 1
        else:
            frequency_dict[keys] = 1
    return frequency_dict

genres = extract(11)
genres_ft = freq_table(genres)

## 3. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(number):
    frequency_list = []
    frequency_dict = {}
    for row in apps_data[1:]:
        value = row[number]
        frequency_list.append(value)
    for data in frequency_list:
        if data in frequency_dict:
            frequency_dict[data] += 1
        else:
            frequency_dict[data] = 1
    return frequency_dict

ratings_ft = freq_table(7)

## 4. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(table, index):
    frequency_table = {}
    
    for row in table:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(apps_data[1:], 7)

## 5. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set=apps_data, index=7)
genres_ft = freq_table(index=11, data_set=apps_data)

## 6. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    data = extract(data_set, index)
    return find_sum(data) / find_length(data)

avg_price = mean(apps_data, 4)

## 7. Debugging Functions ##

def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)