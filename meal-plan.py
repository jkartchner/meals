import sys
from recipe import *


print(" _______   ________  _________  ___  ___  ___       ")
print("|\  ___ \ |\   __  \|\___   ___\\  \|\  \|\  \      ")
print("\ \   __/|\ \  \|\  \|___ \  \_\ \  \ \  \ \  \     ")
print(" \ \  \_|/_\ \   __  \   \ \  \ \ \  \ \  \ \  \    ")
print("  \ \  \_|\ \ \  \ \  \   \ \  \ \ \__\ \__\ \__\   ")
print("   \ \_______\ \__\ \__\   \ \__\ \|__|\|__|\|__|   ")
print("    \|_______|\|__|\|__|    \|__|     ___  ___  ___ ")
print("                                     |\__\|\__\|\__\ ")
print("                                     \|__|\|__|\|__| \n\n")

##################### SET UP STUFF ###########################
recipes = []
weeks = []
meals = []

        
mp = open("master-plan.txt", 'r')
list_lines_mp = mp.readlines()                      # each line in a list
mp.close()


i = 0
i_b_recipe = 0                                      # index of begin of recipe
i_b_week = 0                                        # index of begin of week


############# MAIN LOOP: READ MASTER PLAN ################

for line in list_lines_mp:
    line = line.strip()
    if len(line.strip()) < 1:                       # ignore comments, empty lines
        i += 1
        continue
    if line[0] == '#':
        i += 1
        continue
    if "Recipe:" in line or "recipe:" in line or "RECIPE:" in line:
        i_b_recipe = i
    elif i_b_recipe > 0 and "end recipe" in line or "End Recipe" in line or "END RECIPE" in line:
        # add recipe to list with recipes.append(x); temporarily using placeholder here
        recipe = Recipe(list_lines_mp[i_b_recipe:i])
        recipes.append(recipe)
        # now clear vars
        i_b_recipe = 0
    elif "Week " in line and ":" in line:
        assert(i_b_recipe == 0), "Can't have meal planning in the middle of a recipe in your master-plan.txt at line " + str(i)
        i_b_week = i
    elif i_b_week > 0 and "end week" in line or "End Week" in line or "END WEEK" in line:
        week = Week(list_lines_mp[i_b_week:i + 1])  # add 1 line to make sure capture "end week" line
        weeks.append(week)
        # now clear vars
        i_b_week = 0
    i += 1

weeks.sort()                            # see the __lt__ function in the class
# generate.groceries()
print("File 'master-plan.txt' is " + str(i) + " lines long.")
print("Collected " + str(len(recipes)) + " recipes.")
print("Preparing " + str(len(weeks)) + " weeks of meals.")
#print("Planning " + str(len(meals)) + " meals for the year.")





################ MAIN LOOP: WRITE MEAL PLAN ###################
f = open("meal-plan.txt", 'w')

f.write(" _______   ________  _________     \n")
f.write("|\  ___ \ |\   __  \|\___   ___\   \n")
f.write("\ \   __/|\ \  \|\  \|___ \  \_\   \n")
f.write(" \ \  \_|/_\ \   __  \   \ \  \    \n")
f.write("  \ \  \_|\ \ \  \ \  \   \ \  \   \n")
f.write("   \ \_______\ \__\ \__\   \ \__\  \n")
f.write("    \|_______|\|__|\|__|    \|__|  \n")
f.write("                                   \n")
f.write("                                   \n")

## TEST CODE
#j = Ingredient("40 grams garam masala (homemade)")

#j.test()

#recipes[0].test()
#print("~~~~~~~~~~~~~~~~~~~~~~")
#recipes[1].test()

f.write("\n\n")
for week in weeks:
    week.generate_groceries(recipes)        # doing this separately so we can put recipes wherever we want in our master plan.txt
    week.publish(f)                         # publish in the master file "f"
    plan = open("Week " + str(week.number) + " - " + week.name + " Meal Plan.txt", "w")
    week.publish(plan)                    # publish in an individual file "plan"
    plan.close()
f.write("\n____________________________________\n")
f.write("\nRecipes\t\tRecipes")
h_rec_nams = open("Recipe List.txt", 'w')
h_rec_nams.write("____________________________________\n\n")
h_rec_nams.write("LIST OF RECIPES\n")
h_rec_nams.write("____________________________________\n\n")
for recipe in recipes:
    recipe.publish(f)
    f.write("\nRecipes\t\tRecipes")
    h_rec_nams.write(recipe.name + "\n")
h_rec_nams.close()
# later
f.close()
