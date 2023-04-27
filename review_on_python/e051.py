num_list = input('Enter elements of a list separated by space: ').split()
# sorting the numbers
sort_num_list = sorted([int(i) for i in num_list])

# finding max and min
max, min = sort_num_list[-1], sort_num_list[0]
# finding the mean
mean = sum(sort_num_list)/len(sort_num_list)
#finding the median
median = sort_num_list[len(sort_num_list) // 2 + 1] if len(sort_num_list) % 2 == 1 else 1/2*(sort_num_list[len(sort_num_list) // 2] + sort_num_list[len(sort_num_list) // 2 - 1 ])

print({ "max" : max,
            "min" : min,
            "mean" : round(mean, 2),
            "median" : median
        })