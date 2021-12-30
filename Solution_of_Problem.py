

# The prime function extracted the prime numbers between the lower and upper variable values using for loop.

def prime():
    lower = 1
    upper = 1000000
    prime_number_list = []
    for i in range(lower, upper + 1):

        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                prime_number_list.append(i)

    return prime_number_list


# The distance function extracted all distances between two consecutive prime numbers using for loop.

def distance():
    get_prime_number = prime()
    prime_number_list_length = len(get_prime_number)
    distance_data = []
    for i in range(0, prime_number_list_length-1):
        value = get_prime_number[i+1] - get_prime_number[i]
        distance_data.append(value)

    return distance_data


distance_data_list = distance()


# The mean function extracted the average value of a given data list.

def mean(get_data):
    distance_data_list_length = len(get_data)
    add = 0
    for d in get_data:
        add += d

    result = add/distance_data_list_length
    print("Mean: " + str(result))


mean(distance_data_list)


# The median function extracted the middle value of a given data list.

def median(get_data):
    distance_data_list_length = len(get_data)
    get_data.sort()
    if distance_data_list_length % 2 == 0:
        median1 = get_data[distance_data_list_length//2]
        median2 = get_data[distance_data_list_length//2 - 1]
        result = (median1 + median2)/2
    else:
        result = get_data[distance_data_list_length//2]
    print("Median: " + str(result))


median(distance_data_list)


# The mode function extracted the most common value from a given data list.

def mode(get_data):
    data = {}
    for a in get_data:
        if a not in data:
            data[a] = 1
        else:
            data[a] += 1
    result = [k for k, v in data.items() if v == max(data.values())]
    print("Mode: " + ', '.join(map(str, result)))


mode(distance_data_list)






