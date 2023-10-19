data = [
    20, 74, 80, 65, 52, 25, 40, 72, 60, 48, 34, 74,
    60, 52, 77, 92, 15, 80, 71, 88, 78, 82, 67, 63,
    79, 70, 81, 85, 60, 98, 83, 62, 89, 90, 17, 80,
    32, 82, 95, 55, 75, 81, 54, 74, 70, 19, 82, 85,
    56, 36, 41, 76, 72, 67, 64, 43, 84, 79, 68, 61,
]

duplicate_sorted_data = sorted(data)

nonDuplicate_data = set(duplicate_sorted_data)
sorted_data = sorted(nonDuplicate_data)

count = []
for i in range (len(sorted_data)):
    count.append(duplicate_sorted_data.count(sorted_data[i]))

print("Value","\t","Frequency")
for i in range (len(sorted_data)):
    print(sorted_data[i],"\t",count[i])

mean = sum(data)/len(data)
print("Mean: ", mean)

median = (duplicate_sorted_data[((len(duplicate_sorted_data))//2)-1] + duplicate_sorted_data[(len(duplicate_sorted_data))//2])/2
print("Median: ", median)

squared_diff = [(x - mean) ** 2 for x in data]
variance = sum(squared_diff) / len(duplicate_sorted_data)
print("Variance: ", variance)

print("Standard Deviation: ", variance**(1/2))

largestFrequency = max(count)
print("Largest Frequency: ", largestFrequency)
for i in range (len(sorted_data)):
    if count[i] == largestFrequency:
        print("Mode: ", sorted_data[i])
