

i = float(raw_input("Enter calories: "))
s = raw_input("Enter input kind: ")
o_pounds = 0.0
o_ounces = 0.0
o_grams = 0.0
o_tsp = 0.0
o_tbsp = 0.0
o_cup = 0.0

if s == "o":
    o_ounces = i
    o_grams = i / 28.35 
    o_pounds = i * 16
if s == "p":
    o_ounces = i / 16
    o_grams = i / 453.6
    o_pounds = i
if s == "g":
    o_ounces = i * 28.35
    o_grams = i
    o_pounds = i * 453.6
if s == "t":
    o_tsp = i
    o_tbsp = i * 3
    o_cup = i * 12
if s == "b":
    o_tsp = i / 3
    o_tbsp = i
    o_cup = i * 4
if s == "c":
    o_tsp = i / 12
    o_tbsp = i / 4
    o_cup = i

print("\nCalories in grams: " + str(o_grams))
print("Calories in ounces: " + str(o_ounces))
print("Calories in pounds: " + str(o_pounds))

print("\nCalories in teaspoons: " + str(o_tsp))
print("Calories in tablespoons: " + str(o_tbsp))
print("Calories in cups: " + str(o_cup))

print("Zeros: 0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

print("Weight: " + "{:.2f}".format(o_grams) + ":" + "{:.2f}".format(o_ounces) + ":" + "{:.2f}".format(o_pounds))
print("Volume: " + "{:.2f}".format(o_tsp) + ":" + "{:.2f}".format(o_tbsp) + ":" + "{:.2f}".format(o_cup))
