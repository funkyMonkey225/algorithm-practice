

highestTotal = 0
i = 0 
for (i < input1[0]):
    tempTotal = 0
    counter = 0
    while total <= input1[1] and counter < input[0]:
        if (tempTotal + input2[counter]) <= max:
            tempTotal = tempTotal + input2[counter]
        counter =  counter + 1
    if tempTotal > highestTotal:
        highestTotal = tempTotal

return highestTotal