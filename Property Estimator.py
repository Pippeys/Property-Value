import csv


print("Property Type: ")
type_answer = input()

print("Zip Code: ")
zip_answer = input()

print("Cap Rate: " )
cap_answer = input()

print("Square Footage: ")
sqft_answer = input()

print("Floor to lot size Ratio")
far_answer = input()

if type_answer == "multi-family" or "Multi-Family":
    print("Number of Units")
    units_answer = input()

answer_list = [type_answer,zip_answer,cap_answer,far_answer,units_answer]

print(answer_list)
