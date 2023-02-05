## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0
for each in a_list:
    sum_manual += each

print(sum_manual)
print(sum(a_list))

## 2. Built-In Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}
for each in ratings:
    if each in content_ratings:
        content_ratings[each] += 1
    else:
        content_ratings[each] = 1

print(content_ratings)

## 3. Creating Our Own Functions ##

def square(a_number):
    squared_number = a_number * a_number
    return squared_number

squared_10 = square(a_number = 10)
squared_16 = square(a_number = 16)

## 4. The Structure of a Function ##

def add_10(number):
    result = number + 10
    return result

add_30 = add_10(number = 30)
add_90 = add_10(number = 90)

## 5. Parameters and Arguments ##

def date(year, month, day):
    return str(month) + " " + str(day) + ", " + str(year)

print(date(2006, 'July', 15))
print(date(2004, 'February', 4))
print(date(1949, 'June', 9))

## 6. The Return Statement ##

def square(a_number):
    return a_number * a_number

squared_6 = square(6)
squared_11 = square(11)