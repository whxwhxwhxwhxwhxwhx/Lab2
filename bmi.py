def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi =(weight/(height*height))

    #Add code here to display calculate BMI
    print("BMI="+str(bmi))

    # Add code here to classify BMI
    if bmi < 18.5:
        print("-1") #underweight
    elif 18.5 <= bmi <= 25.0:
        print("0") #normalweight
    else:
        print("1") #overweight

    return bmi

calculate_bmi(weight=57, height=1.73)