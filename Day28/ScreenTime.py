import statistics

def too_much_screen_time(hours):
    window_size = 3
    avg_list = statistics.mean(hours)

    if avg_list>=6:
        return True

    for i in hours:
        if i >= 10:
            return True

    for i in range(len(hours)-window_size+1):
        window = hours[i:i + window_size]
        avg = statistics.mean(window)
        if avg >= 8:
            return True

    return False

too_much_screen_time([1, 2, 3, 4, 5, 6, 7])
too_much_screen_time([7, 8, 8, 4, 2, 2, 3])
too_much_screen_time([5, 6, 6, 6, 6, 6, 6])
too_much_screen_time([1, 2, 3, 11, 1, 3, 4])
too_much_screen_time([1, 2, 3, 10, 2, 1, 0])
too_much_screen_time([3, 9, 4, 8, 5, 7, 6])



#we are given a list of  seven integers that represent the number of hours spent on screen per day, we are required to determine presumably  at the end of the week if the user spent too much screen time or not based on some constraints , 
#first if any single day has 10hrs or more we return True, we can do this by using a for loop to traverse the list and return true as soon as it finds an element greater than equal to 10
#secondly, if the average of any three days in a row is greater than or equal to 8 hours we return true, in the for loop that traverses the list , the first if is there to check if there is any element greater than or equal to ten , we will have an elif or perhaps a nested for loop , for each three elements in a row calculate the average , we can get the three elements using slicing , what do you think 
#lastly, if the average of the seven day is greater than or equal to 6 hours we return True, we can use statistics.mean(hours) to check for this 