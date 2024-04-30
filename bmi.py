def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi =(weight/(height*height))

    #Add code here to display calculate BMI
    print("BMI="+str(bmi))

    # Add code here to classify BMI
    if bmi < 18.5:
        print("underweight") #underweight
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("normal weight") #normalweight
        return 0
    else:
        print("overweight") #overweight
        return 1

calculate_bmi(weight=57, height=1.73)