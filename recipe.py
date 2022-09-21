import copy
# add categories for sorting
# add the ability to make a note in the meal plan that will go through the system and show up to users
# add ability to add ingredient to shop for in the meal plan (sodas, apples for snacks, etc)
# add the ability to reference other recipes and include them - you can mark the recipe somehow to opt out of this,  but it otherwise does so
# categories: produce, meat, seafood, bakery, bread, baking, canned goods, soups, asian, hispanic, pasta, frozen foods, dairy, junk food
dict_cats = {   'almonds':'produce',
		        'almond':'produce',
                'apple':'produce',
                'apples':'produce',
                'avocados':'produce',
                'avocado':'produce',
                'baby bok choy':'produce',
                'bananas':'produce',
                'bell pepper':'produce',
                'blackberries':'produce',
                'blueberries':'produce',
                'bok choy':'produce',
                'broccoli':'produce',
                'cabbage':'produce',
                'carrot':'produce',
                'carrots':'produce',
                'cashews':'produce',
		        'cashew':'produce',
                'cherry tomatoes':'produce',
                'celery':'produce',
		        'chia seeds':'produce',
                'cilantro':'produce',
		        'dates':'produce',
                'fresh basil':'produce',
                'fresh cilantro':'produce',
                'fresh ginger':'produce',
                'fresh parsley':'produce',
                'garlic':'produce',
                'ginger root':'produce',
                'ginger':'produce',
                'green bell pepper':'produce',
                'green bell peppers':'produce',
                'green onions':'produce',
                'green peppers':'produce',
                'green pepper':'produce',
                'iceburg lettuce':'produce',
                'jalapenos':'produce',
                'jalapeno':'produce',
                'jalapeno pepper':'produce',
                'jalapeno peppers':'produce',
		        'lemon':'produce',
		        'lemons':'produce',
		        'lemon juice':'produce',
                'lettuce':'produce',
                'lime':'produce',
                'lime juice':'produce',
                'onions':'produce',
                'onion':'produce',
		        'oranges':'produce',
		        'orange':'produce',
                'parmiggiano reggiano':'produce',
                'pecans':'produce',
                'pecorino romano':'produce',
                'pumpkin seeds':'produce',
                'peach':'produce',
                'peaches':'produce',
                'raspberries':'produce',
                'red bell pepper':'produce',
                'red onion':'produce',
                'red onions':'produce',
                'red pepper':'produce',
                'red peppers':'produce',
		        'roasted almonds':'produce',
		        'roasted cashews':'produce',
                'roma tomato':'produce',
                'roma tomatoes':'produce',
                'roma tomatos':'produce',
                'sage':'produce',
                'salad mix':'produce',
                'scallions':'produce',
                'scallion':'produce',
                'serrano chilis':'produce',
                'serrano chili':'produce',
                'serranos':'produce',
                'spinach':'produce',
                'spinach leaves':'produce',
                'sunflower seeds':'produce',
                'strawberries':'produce',
                'sweet onions':'produce',
                'sweet onion':'produce',
		        'swiss cheese':'produce',  	# the cheese is often by the produce, but this probably should be a separate section
                'thyme':'produce',
                'tomatoes':'produce',
                'tomato':'produce',
                'vidalia onion':'produce',
                'vidalia onions':'produce',
                'white onion':'produce',
                'white onions':'produce',
                'yellow onions':'produce',
                'yellow onion':'produce',
                'bacon':'meat',
                'chicken':'meat',
                'chicken breasts':'meat',
                'chicken breast':'meat',
                'chicken thighs':'meat',
                'chicken thigh':'meat',
                'ground beef':'meat',
                'hot dogs':'meat',
                'hot dog':'meat',
                'pepperoni':'meat',
		        'pork butt':'meat',
                'stew beef':'meat',
                'turkey kielbasa sausage':'meat',
		        'flounder filets':'seafood',
                'shrimp':'seafood',
		        'sole filets':'seafood',
                'donut':'bakery',
                'donuts':'bakery',
                'brownies':'bakery',
                'lemon squares':'bakery',
                'granola':'bread',
                'multigrain bread':'bread',
                'potato bread':'bread',
                'sandwich bread':'bread',
                'wheat bread':'bread',
                'white bread':'bread',
                'whole wheat bread':'bread',
                'hot dog buns':'bread',
                'hamburger buns':'buns',
                'all purpose flour':'baking',
                'all-purpose flour':'baking',
                'baking powder':'baking',
                'basil':'baking',               # see dried basil below as well
                'bay leaves':'baking',
                'bay leaf':'baking',
                'black pepper':'baking',
                'bread flour':'baking',
                'brown sugar':'baking',
                'canola oil':'baking',
                'cornmeal':'baking',
		        'chicken bouillon':'baking',
                'chocolate':'baking',
                'chili flake':'baking',         # see also red pepper flake
                'chili powder':'baking',
		        'cinnamon':'baking',
                'coconut oil':'baking',
                'cornstarch':'baking',
                'cumin':'baking',
                'dried basil':'baking',
                'dried oregano':'baking',       # see dried oregano below too
                'extra virgin olive oil':'baking',
                'flour':'baking',
                'fine sea salt':'baking',
                'food coloring':'baking',
                'garlic powder':'baking',
                'granulated sugar':'baking',
                'ground coriander':'baking',
                'ground ginger':'baking',
                'ground paprika':'baking',
                'instant yeast':'baking',
		        'kosher salt':'baking',
                'mini marshmallows':'baking',
                'marshmallows':'baking',
                'nutmeg':'baking',
                'oat flour':'baking',
                'old fashioned oats':'baking',
                'olive oil':'baking',
                'onion powder':'baking',
                'oregano':'baking',
                'paprika':'baking',
                'parchment paper':'baking',     # this isn't baking; 
                'pectin':'baking',
                'pepper':'baking',
                'red pepper flakes':'baking',
                'rolled oats':'baking',
                'salt':'baking',
                'sherry vinegar':'baking',
		        'shredded coconut':'baking',
                'sugar':'baking',
                'tempura flour':'baking',
                'vanilla extract':'baking',
                'vegetable oil':'baking',
		        'wax paper':'baking', 		# this isn't baknig; 
                'white pepper':'baking',
                'white vinegar':'baking',
                'black beans':'canned goods',
                'black olives':'canned goods',
                'crushed tomatoes':'canned goods',
                'calabrian chilis':'canned goods',
                'fruit cocktail':'canned goods',
                'peperoncini':'canned goods',
                'tomato paste':'canned goods',
                'tomato sauce':'canned goods',
                'chicken stock':'soups',
                'basmati rice':'asian',
                'coconut milk':'asian',
                'chili paste':'asian',
                'fish sauce':'asian',
                'hoisin sauce':'asian',
                'jasmine rice':'asian',
                'medium grain rice':'asian',
                'medium-grain rice':'asian',
                'oyster sauce':'asian',
                'sesame oil':'asian',
                'soy sauce':'asian',
                'teriyaki sauce':'asian',
                'teriyaki sauces':'asian',
                'thai red curry paste':'asian',
                'chiles in adobo':'hispanic',
                'chipotle peppers':'hispanic',
                'chipotle pepper':'hispanic',
                'chipotle peppers in adobo sauce':'hispanic',
                'hot sauce':'hispanic',
                'pinto beans':'hispanic',
                'taco shell':'hispanic',
                'taco shells':'hispanic',
                'angel hair noodles':'pasta',
                'angel hair':'pasta',
                'cavatappi pasta':'pasta',
                'cavatappi noodles':'pasta',
                'cavatappi':'pasta',
                'egg noodles':'pasta',
                'thin spaghetti noodles':'pasta',
                'thin spaghetti':'pasta',
                'linguine':'pasta',
                'linguine noodles':'pasta',
                'spaghetti':'pasta',
                'spaghetti noodles':'pasta',
		        'barbeque sauce':'pasta',
		        'barbecue sauce':'pasta',
                'ketchup':'condiments',
                'mayonnaise':'condiments',           
                'salad dressing':'condiments',      
                'frozen broccoli':'frozen foods',
                'frozen pizza':'frozen foods',
                'frozen strawberries':'frozen foods',
                'orange juice':'frozen foods',
                'honey':'cereal',         
                'jam':'cereal',
                'maple syrup':'cereal',
                'peanut butter':'cereal',
                'rice krispies':'cereal', 
                'rolled oats':'cereal', 
                '1% milk':'dairy',
                '2% milk':'dairy',
                'butter':'dairy',
                'buttermilk':'dairy',
                'cheddar cheese':'dairy',
                'eggs':'dairy',
                'egg':'dairy',
                'fresh mozzarella':'dairy',
                'heavy cream':'dairy',
                'heavy whipping cream':'dairy',
                'milk':'dairy',
                'mozzarella':'dairy',
                'provolone':'dairy',
                'skim milk':'dairy',
                'unsalted butter':'dairy',
                'whole milk':'dairy',
                'yogurt':'dairy',
                'beer':'junk food',
                'doritos':'junk food',
                'water':'junk food',
		        'white wine':'junk food'} 	# obviously this is not junk food; we need an alcohol section to go with the beer

# categories: produce, meat, seafood, bakery, bread, baking, canned goods, soups, asian, hispanic, pasta, frozen foods, cereal, dairy, junk food
dict_king_soopers = {   'produce': 1,
                        'meat': 2,
                        'seafood': 3,
                        'bakery': 4,
                        'bread': 5,
                        'baking': 6,
                        'canned goods': 7,
                        'soups': 8,
                        'asian': 9,
                        'hispanic': 10,
                        'pasta': 11,
                        'frozen foods': 12,
                        'cereal':'13',
                        'dairy': 14,
                        'junk food': 15,
                        'unknown': 16     }

# categories: produce, meat, seafood, bakery, bread, baking, canned goods, soups, asian, hispanic, pasta, frozen foods, cereal, dairy, junk food
dict_walmart = {        'produce': 1,
                        'bakery': 2,
                        'frozen foods': 3,
                        'meat': 4,
                        'seafood': 5,
                        'bread': 6,
                        'baking': 7,
                        'canned goods': 8,
                        'soups': 9,
                        'asian': 10,
                        'hispanic': 11,
                        'pasta': 12,
                        'cereal':'13',
                        'junk food': 14,
                        'dairy': 15,
                        'unknown': 16     }

def walmart_sort(x):
    return dict_walmart[x.category]

class Ingredient:
    amount = ""
    kind = ""
    real_ingredient = ""
    additional_info = ""
    float_amount = 0.0
    text = ""
    category = ""
    jake = False
    
    def __init__(self, in_text):
        # break down the ingredient and allocate vars
        in_text = in_text.strip()               # clean up text first
        in_text = in_text.replace("  ", " ")

        # in case this ingredient is a dummy, just pack what you can and bail
        if in_text.count(" ") < 1:
            self.text = in_text;
            return
        
        ## CONVERT AMOUNT TO A NUMBER INSTEAD OF STRING
        indx = in_text.find(" ")                # slice out first word entered, which is usually a number (edge cases will be dealt with later)
        nxt_indx = 0
        if in_text[indx + 1].isdigit():         # deal with cases where it's a whole number followed by a fraction: 1 1/2
            nxt_indx = in_text.find(" ", indx+1)
        self.amount = in_text[0:indx]

        try:
            if "/" in self.amount:
                self.float_amount = self.convert_float(self.amount)
            elif nxt_indx > 0 and "/" in in_text[indx + 1:nxt_indx]:   # deal with cases where it's a whole number followed by a fraction: 1 1/4
                self.float_amount = float(self.amount) + self.convert_float(in_text[indx + 1:nxt_indx])
                self.amount = in_text[0:nxt_indx]
                indx = nxt_indx                     # now move it all over - create consistency in indx var for later
            else:
                self.float_amount = float(self.amount)
        except:
            self.float_amount = 0.0
            
        ## IDENTIFY KIND OF INPUT MEASUREMENT
        nxt_indx = in_text.find(" ", indx+1)
        self.kind = in_text[indx + 1:nxt_indx]
        if "oz" in self.kind or "ounce" in self.kind:
            self.kind = "ounce"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif ("g" in self.kind or "gram" in self.kind) and "egg" not in self.kind \
             and "bag" not in self.kind and "wedge" not in self.kind \
	     and "orange" not in self.kind and "package" not in self.kind:
            self.kind = "gram"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "lb" in self.kind or "pound" in self.kind:
            self.kind = "pound"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "tbsp" in self.kind or "tablespoon" in self.kind:
            self.kind = "tablespoon"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "tsp" in self.kind or "tspn" in self.kind or "teaspoon" in self.kind:
            self.kind = "teaspoon"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "cup" in self.kind or "C." in self.kind or "c." in self.kind:
            self.kind = "cup"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "clove" in self.kind:
            self.kind = "clove"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "can" in self.kind:
            self.kind = "can"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "bag" in self.kind:
            self.kind = "bag"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "case" in self.kind:
            self.kind = "case"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "container" in self.kind or "cont" in self.kind:
            self.kind = "container"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "crown" in self.kind:
            self.kind = "crown"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "slice" in self.kind:
            self.kind = "slice"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "box" in self.kind:
            self.kind = "box"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "es"
        elif "bottle" in self.kind:
            self.kind = "bottle"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "bunch" in self.kind:
            self.kind = "bunch"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "es"
        elif "sprig" in self.kind:
            self.kind = "sprig"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "jar" in self.kind:
            self.kind = "jar"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "wedge" in self.kind:
            self.kind = "wedge"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "recipe" in self.kind:
            self.kind = "recipe"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "package" in self.kind:
            self.kind = "package"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "rib" in self.kind:
            self.kind = "rib"
            if self.float_amount > 0 and self.float_amount > 1:
                self.kind = self.kind + "s"
        elif "whole" in self.kind:
            self.kind = "whole"
        else:                                                       # no kind measurement; we count darabonkent
            self.kind = ""
            nxt_indx = indx
        ## REMOVE FROM STRING ADDITIONAL DESCRIPTORS
        self.real_ingredient = in_text[nxt_indx + 1:]
        if "(" in self.real_ingredient and ")" in self.real_ingredient:
            indx = self.real_ingredient.find("(")
            nxt_indx = self.real_ingredient.find(")")
            self.additional_info = self.real_ingredient[indx + 1:nxt_indx]
            self.real_ingredient = self.real_ingredient[:indx - 1]  # + self.real_ingredient[nxt_index:]
            
        self.text = in_text
        try:
            self.category = dict_cats[self.real_ingredient]
        except:
            self.category = "unknown"

    def __lt__(self, other):
        return dict_king_soopers[self.category] < dict_king_soopers[other.category]

    def convert_float(cls, txt):
        nos = txt.split('/')
        if len(nos) == 2:
            return float(nos[0]) / float(nos[1])
        else:
            return -1

    def convert_grams_ounces(cls):
        if cls.float_amount > 0 and "gram" in cls.kind:
            return cls.float_amount / 28.35
        else:
            return -1

    def convert_ounces_pounds(cls):
        if cls.float_amount > 0 and "ounce" in cls.kind:
            return cls.float_amount / 16
        else:
            return -1

    def convert_pounds_ounces(cls):
        if cls.float_amount > 0 and "pound" in cls.kind:
            return cls.float_amount * 16
        else:
            return -1

    def convert_pounds_grams(cls):
        if cls.float_amount > 0 and "pound" in cls.kind:
            return cls.float_amount * 453.59
        else:
            return -1

    def convert_grams_pounds(cls):
        if cls.float_amount > 0 and "grams" in cls.kind:
            return cls.float_amount / 453.59
        else:
            return -1

    def convert_ounces_grams(cls):
        if cls.float_amount > 0 and "ounce" in cls.kind:
            return cls.float_amount * 28.35
        else:
            return -1

    def test(cls):
        print("_______________Ingredient______________")
        print("Full Text: " + cls.text)
        print("Amount: " + cls.amount + "\tKind: " + cls.kind + " and we got " + str(cls.float_amount) + " as the actual float converted number")
        print("Real Ingredient is " + cls.real_ingredient + ".")
        print("Category is " + cls.category + ".\n")
        print("Converting grams to ounces: " + str(cls.convert_grams_ounces()))
        print("Converting ounces to pounds: " + str(cls.convert_ounces_pounds()))
        print("Converting pounds to ounces: " + str(cls.convert_pounds_ounces()))
        print("Converting pounds to grams: " + str(cls.convert_pounds_grams()))
        print("Converting ounces to grams: " + str(cls.convert_ounces_grams()))

    def publish(cls, file):
        file.write("  " + cls.text + "\n")

class Recipe:
    name = ""
    time_active = ""
    time_inactive = ""
    time_total = ""
    cal_serving = ""
    cal_total = ""
    link = ""
    ingredients = []
    directions = []
    keywords = []
    def __init__(self, lines):                  # takes a list of lines of text from a file which contain the recipe
        self.ingredients = []
        self.directions = []
        self.keywords = []
        i_b_ingredients = 0
        i_b_directions = 0
        for line in lines:
            line = line.strip()
            if len(line) < 1:
                continue
            if "Recipe:" in line or "recipe:" in line or "RECIPE:" in line:
                line = line.replace("Recipe:", "")
                line = line.replace("recipe:", "")
                line = line.replace("RECIPE:", "")
                line = line.strip()
                self.name = line
            if ("Time" in line or "time" in line or "TIME" in line) and \
               ("Inactive" in line or "inactive" in line or "INACTIVE" in line) and \
               (":" in line):
                line = line.replace("Time", "")
                line = line.replace("time", "")
                line = line.replace("TIME", "")
                line = line.replace("Inactive", "")
                line = line.replace("inactive", "")
                line = line.replace("INACTIVE", "")
                line = line.replace(":", "")
                line = line.strip()
                self.time_inactive = line
            if ("Time" in line or "time" in line or "TIME" in line) and \
               ("Active" in line or "active" in line or "ACTIVE" in line) and \
               (":" in line):
                line = line.replace("Time", "")
                line = line.replace("time", "")
                line = line.replace("TIME", "")
                line = line.replace("Active", "")
                line = line.replace("active", "")
                line = line.replace("ACTIVE", "")
                line = line.replace(":", "")
                line = line.strip()
                self.time_active = line
            if ("Time" in line or "time" in line or "TIME" in line) and \
               ("Total" in line or "total" in line or "TOTAL" in line) and \
               (":" in line):
                line = line.replace("Time", "")
                line = line.replace("time", "")
                line = line.replace("TIME", "")
                line = line.replace("Total", "")
                line = line.replace("total", "")
                line = line.replace("TOTAL", "")
                line = line.replace(":", "")
                line = line.strip()
                self.time_total = line
            if ("Calories" in line or "calories" in line or "CALORIES" in line) and \
               ("Total" in line or "total" in line or "TOTAL" in line) and \
               (":" in line):
                line = line.replace("Calories", "")
                line = line.replace("calories", "")
                line = line.replace("CALORIES", "")
                line = line.replace("Total", "")
                line = line.replace("total", "")
                line = line.replace("TOTAL", "")
                line = line.replace(":", "")
                line = line.strip()
                self.cal_total = line
            if ("Calories" in line or "calories" in line or "CALORIES" in line) and \
               ("Serving" in line or "serving" in line or "SERVING" in line) and \
               (":" in line):
                line = line.replace("Calories", "")
                line = line.replace("calories", "")
                line = line.replace("CALORIES", "")
                line = line.replace("Serving", "")
                line = line.replace("serving", "")
                line = line.replace("SERVING", "")
                line = line.replace(" per ", "")            # calories per serving
                line = line.replace(" Per ", "")
                line = line.replace(" PER ", "")
                line = line.replace(":", "")
                line = line.strip()
                self.cal_serving = line
            if "Link:" in line or "link:" in line or "LINK:" in line:
                line = line.replace("Link:", "")
                line = line.replace("link:", "")
                line = line.replace("LINK:", "")
                line = line.strip()
                self.link = line
            if "Keywords:" in line or "KEYWORDS:" in line or "keywords:" in line:
                line = line.replace("Keywords:", "")
                line = line.replace("keywords:", "")
                line = line.replace("KEYWORDS:", "")
                line = line.strip()
                words = line.split(",")
                for word in words:
                    self.keywords.append(word.strip())
            if "Directions" == line or "DIRECTIONS" == line or "directions" == line:
                i_b_ingredients = 0
                i_b_directions = 100
                continue
            if "Ingredients" == line or "INGREDIENTS" == line or "ingredients" == line:
                i_b_ingredients = 100
                i_b_directions = 0
                continue
            if i_b_ingredients > 0:
                self.ingredients.append(Ingredient(line))
            if i_b_directions > 0:
                self.directions.append(line)
                
    def __lt__(self, other):
        return self.name < other.name
    
    def test(cls):
        print("____________RECIPE____________")
        print("Name: " + cls.name)
        print("Time Active: " + cls.time_active)
        print("Time Inactive: " + cls.time_inactive)
        print("Calories per Serving: " + cls.cal_serving)
        print("Total Calories: " + cls.cal_total)
        print("Link: " + cls.link)
        print("Keywords: ")
        for word in cls.keywords:
            print("\t\t" + word)
        print("Ingredients")
        for ingredient in cls.ingredients:
            #ingredient.test()
            print("\t" + ingredient.text)
        print("Directions")
        for direction in cls.directions:
            print("\t" + direction)
        print("Recipe has " + str(len(cls.ingredients)) + " ingredients.")
        print("Recipe has " + str(len(cls.directions)) + " directions.")


    def publish(cls, file):
        file.write("\n____________________________________\n")
        file.write("\n" + cls.name.upper() + "\n\n")
        if cls.time_active:
            file.write("Time Active: " + cls.time_active + "\t\t")
        if cls.time_inactive:
            file.write("Cooking Time: " + cls.time_inactive + "\n")
        if cls.time_total:
            file.write("Total Time: " + cls.time_total + "\n")
        file.write("\nIngredients\n")
        for ingredient in cls.ingredients:
            ingredient.publish(file)
        file.write("\nDirections\n")
        for direction in cls.directions:
            file.write("\n  " + direction + "\n")
        file.write("\n")
        if cls.cal_serving:
            file.write("Calories per Serving: " + cls.cal_serving + "\t")
        if cls.cal_total:
            file.write("Total Calories: " + cls.cal_total + "\n")
        if cls.link:
            file.write("Link to Recipe: " + cls.link + "\n")
        if len(cls.keywords) > 0:
            file.write("Keywords: ")
            for keyword in cls.keywords:
                file.write(keyword + ", ")
            file.write("\n")
        file.write("____________________________________\n")


            
class Day:
    name = ""
    eaters = ""
    meals = []
    def __init__(self, lines):
        self.meals = []
        for line in lines:
            line = line.strip()
            if len(line) < 1:
                continue
            if "day:" in line or "Day:" in line or "DAY:" in line:
                line = line.replace("Day:", "")
                line = line.replace("day:", "")
                line = line.replace("DAY:", "")
                line = line.strip()
                self.name = line
                continue
            if "meal:" in line or "Meal:" in line or "MEAL:" in line:
                line = line.replace("Meal:", "")
                line = line.replace("meal:", "")
                line = line.replace("MEAL:", "")
                line = line.strip()
                self.meals.append(line)
                
    def publish(cls, file):
        file.write("\n  " + cls.name + ":")
        #print("\n\t" + cls.name)
        for meal in cls.meals:
            file.write("  " + meal.replace(" - jake","")) # no sense seeing who's eating what
            #print("\t\t" + meal)

class Week:
    days = []
    number = 0
    name = ""
    groceries = []
    jake_groceries = []
    weekly_recipes = []
    def __init__(self, lines):
        self.days = []
        self.groceries = []
        self.jake_groceries = []
        self.recipes = []
        self.weekly_recipes = []
        i_b_days = 0
        i = 0
        for line in lines:
            line = line.strip()
            #print(line)
            if len(line) < 1:
                continue
            if ("week" in line or "Week" in line or "WEEK" in line) and \
               ":" in line:
                line = line.replace("Week", "")
                line = line.replace("WEEK", "")
                line = line.replace("week", "")
                index = line.find(":")
                wkno = line[:index]
                self.number = int(wkno)
                line = line[index+1:]
                line = line.strip()
                self.name = line
            if "day:" in line or "Day:" in line or "DAY:" in line:
                if i_b_days > 0:
                    self.days.append(Day(lines[i_b_days:i]))
                    i_b_days = i
                i_b_days = i
            # can't be 0 bc week name occuplies that slot
            if i_b_days > 0 and \
                ("end week" in line or "End Week" in line or \
                 "END WEEK" in line):
                self.days.append(Day(lines[i_b_days:i]))
                i_b_days = 0
            i += 1

    def __lt__(self, other):
        return self.number < other.number

    def generate_groceries(cls, recipes):
        tobuy = []
        tojake = []
        jake = False
        for day in cls.days:
            for meal in day.meals:
                jake = False
                for recipe in recipes:
                    # first decide if this is a jake only meal
                    if " - jake" in meal or " - Jake" in meal or " - JAKE" in meal:
                        jake = True
                        meal = meal.replace(" - jake","")
                        meal = meal.replace(" - Jake","")
                        meal = meal.replace(" - JAKE","")
                    if meal == recipe.name:
                        # append the recipe
                        if recipe not in cls.weekly_recipes:
                            cls.weekly_recipes.append(recipe)
                        for ingredient in recipe.ingredients:
                            if jake:
                                ingredient.jake = True
                                tojake.append(copy.deepcopy(ingredient)) # if we don't deepcopy this, we have references in memory for these objects that get modified below in a way that cumulatively throws ingredient amount out of whack
                            else:
                                tobuy.append(copy.deepcopy(ingredient))
        cls.weekly_recipes.sort()
        backup = copy.deepcopy(tobuy)
        #tojake = copy.deepcopy(tojake) # will this reset the list into its own memory?
        index = 0
        jdex = 0
        for ingredient in tobuy:
            for grocery in backup:
                if index >= jdex:
                    jdex += 1
                    continue            # don't want to compare against the same elements
                if ingredient.real_ingredient == grocery.real_ingredient:
                    if ingredient.float_amount < 0.0001 or grocery.float_amount < 0.0001:
                        jdex += 1
                        continue                                            # no hope of adding them, so just bail
                    # we have the same ingredient and hope to combine them
                    if ingredient.kind in grocery.kind or grocery.kind in ingredient.kind:
                        ingredient.float_amount += grocery.float_amount
                        backup.remove(grocery)                              # delete this one from the list so we don't confuse it later
                        del tobuy[jdex]
                    elif "gram" in ingredient.kind and "ounce" in grocery.kind:
                        ingredient.float_amount += grocery.convert_ounces_grams()
                        # I don't like buying things in "grams" so will convert to ounces for the shopping list
                        tmp = ingredient.convert_grams_ounces()
                        ingredient.kind = "ounces"
                        ingredient.float_amount = tmp
                        backup.remove(grocery)
                        del tobuy[jdex]
                    elif "ounce" in ingredient.kind and "gram" in grocery.kind:
                        ingredient.float_amount += grocery.convert_grams_ounces()
                        backup.remove(grocery)
                        del tobuy[jdex]
                    elif "ounce" in ingredient.kind and "pound" in grocery.kind:
                        ingredient.float_amount += grocery.convert_pounds_ounces()
                        backup.remove(grocery)
                        del tobuy[jdex]
                    elif "pound" in ingredient.kind and "ounce" in grocery.kind:
                        ingredient.float_amount += grocery.convert_ounces_pounds()
                        backup.remove(grocery)
                        del tobuy[jdex]
                    elif "pound" in ingredient.kind and "gram" in grocery.kind:
                        ingredient.float_amount += grocery.convert_grams_pounds()
                        backup.remove(grocery)
                        del tobuy[jdex]
                    elif "gram" in ingredient.kind and "pound" in grocery.kind:
                        ingredient.float_amount += grocery.convert_pounds_grams()
                        backup.remove(grocery)
                        del tobuy[jdex]
                jdex += 1                
            index += 1
            jdex = 0
        cls.groceries = tobuy
        cls.groceries.sort()

        # now handle the jake list
        backup = []
        backup = copy.deepcopy(tojake) 
        index = 0
        jdex = 0
        for ingredient in tojake:
            for grocery in backup:
                if index >= jdex:
                    jdex += 1
                    continue            # don't want to compare against the same elements
                if ingredient.real_ingredient == grocery.real_ingredient:
                    if ingredient.float_amount < 0.0001 or grocery.float_amount < 0.0001:
                        jdex += 1
                        continue                                            # no hope of adding them, so just bail
                    # we have the same ingredient and hope to combine them
                    if ingredient.kind in grocery.kind or grocery.kind in ingredient.kind:
                        ingredient.float_amount += grocery.float_amount
                        backup.remove(grocery)       # delete this one from the list so we don't confuse it later
                        del tojake[jdex]
                    elif "gram" in ingredient.kind and "ounce" in grocery.kind:
                        ingredient.float_amount += grocery.convert_ounces_grams()
                        # I don't like buying things in "grams" so will convert to ounces for the shopping list
                        tmp = ingredient.convert_grams_ounces()
                        ingredient.kind = "ounces"
                        ingredient.float_amount = tmp
                        backup.remove(grocery)
                        del tojake[jdex]
                    elif "ounce" in ingredient.kind and "gram" in grocery.kind:
                        ingredient.float_amount += grocery.convert_grams_ounces()
                        backup.remove(grocery)
                        del tojake[jdex]
                    elif "ounce" in ingredient.kind and "pound" in grocery.kind:
                        ingredient.float_amount += grocery.convert_pounds_ounces()
                        backup.remove(grocery)
                        del tojake[jdex]
                    elif "pound" in ingredient.kind and "ounce" in grocery.kind:
                        ingredient.float_amount += grocery.convert_ounces_pounds()
                        backup.remove(grocery)
                        del tojake[jdex]
                    elif "pound" in ingredient.kind and "gram" in grocery.kind:
                        ingredient.float_amount += grocery.convert_grams_pounds()
                        backup.remove(grocery)
                        del tojake[jdex]
                    elif "gram" in ingredient.kind and "pound" in grocery.kind:
                        ingredient.float_amount += grocery.convert_pounds_grams()
                        backup.remove(grocery)
                        del tojake[jdex]
                jdex += 1                
            index += 1
            jdex = 0
        cls.jake_groceries = sorted(tojake, key=walmart_sort)
        #cls.jake_groceries.sort()


    
    def publish(cls, file):
        file.write("\n\n____________________________________\n\n")
        file.write("WEEK OF " + cls.name.upper() + "\n")
        file.write("____________________________________\n\n")
        file.write("Week: " + cls.name)
        print("\nWeek: " + cls.name)
        for day in cls.days:
            day.publish(file)

        file.write("\n\n____________________________________\n\n")
        file.write("GROCERIES\tFAMILY\n")
        file.write("____________________________________\n\n")
        file.write("Week of " + cls.name + "\n\n")
        if len(cls.groceries) < 1:
            file.write("No groceries this week!")
            return
        for grocery in cls.groceries:
            if grocery.float_amount > 0:
                file.write(str(grocery.float_amount) + " " + grocery.kind + " " + grocery.real_ingredient)
                if grocery.additional_info:
                    file.write(", " + grocery.additional_info)      # included in case the ingredient specifies a brand or type to buy
                file.write("\n") #file.write(" - " + grocery.category + "\n")
            else:
                file.write(grocery.text)

        # produce jake's grocery list, if there is one
        if len(cls.jake_groceries) > 1:
            file.write("\n____________________________________\n\n")
            file.write("GROCERIES\tJAKE\n")
            file.write("____________________________________\n\n")
            file.write("Week of " + cls.name + "\n\n")
            for grocery in cls.jake_groceries:
                if grocery.float_amount > 0:
                    file.write(str(grocery.float_amount) + " " + grocery.kind + " " + grocery.real_ingredient)
                    if grocery.additional_info:
                        file.write(", " + grocery.additional_info)      # included in case the ingredient specifies a brand or type to buy
                    file.write("\n") #file.write(" - " + grocery.category + "\n")
                else:
                    file.write(grocery.text)
        # generate list of recipes we'll be using
        file.write("\n____________________________________\n")
        file.write("\nRecipes\tWeek of " + cls.name)
        for recipe in cls.weekly_recipes:
            recipe.publish(file)
            file.write("\nRecipes\tWeek of " + cls.name)
