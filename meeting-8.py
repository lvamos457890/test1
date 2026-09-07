# while True:
#     print("Body mass index (BMI)")
#     weight = float(input("How much do you in Kilograms "))
#     height = float(input("how tall are you in meters?"))
#     BMI = weight / (height * height)

#     if BMI < 18.5:
#         print("Less Weight")
#     elif 18.5 < BMI:
#         print("Normal Weight")

#     elif 25 < BMI < 29.9:
#         print("Over Weight")

#     else:
#         print("Obesity")



#     print("Your BMI = " + str(BMI))



#     ans = input("Do you want to input again ? y/n --> ").upper()
#     if ans == "n":
#         break

# def greet():
#     print("Hello! Welcome to our website.")
#     print("Enjoy your stay!")

# greet()
        
# number = [53,23,9,70,12]
# print("Maximum value : " + str(max(number)))
# print("Minimum value : " + str(min(number)))
    


# def calculate_average():
#     scores = [70,85,90,80]
#     total = 0 

#     for score in scores:
#         total += score

#     average = total / len(scores)

#     if average >= 70:
#         status = "Pass"

#     else:
#         status = "Fail"   
#     print("Average score: ", average)
#     print("Pass status: ", status)

# calculate_average()