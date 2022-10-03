import sys

class Product():
    category = "produce"
    grams = 0
    ounces = 0
    pounds = 0
    dict_cals = { 'grams':grams,
                  'ounces':ounces,
                  'pounds':pounds }
    def __init__(self, grams, ounces, pounds):
        grams = 0
        ounces = 0
        pounds = 0
        self.grams = grams
        self.ounces = ounces
        self.pounds = pounds
        self.dict_cals = dict_cals

dict_table = { 'gram':0,
               'grams':0,
               'g':0,
               'ounce':1,
               'ounces':1,
               'pound':2,
               'pounds':2,
               'lb':2,
               'lbs':2,
               'teaspoon':3,
               'teaspoons':3,
               'tablespoon':4,
               'tablespoons':4,
               'cup':5,
               'cups':5,
               'clove':6,
               'cloves':6,
               'can':7,
               'cans':7,
               'container':8,
               'containers':8,
               'crown':9,
               'crowns':9,
               'slice':10,
               'slices':10,
               'box':11,
               'boxes':11,
               'bottle':12,
               'bottles':12,
               'bunch':13,
               'bunches':13,
               'sprig':14,
               'sprigs':14,
               'jar':15,
               'jars':15,
               'wedge':16,
               'wedges':16,
               'pack':17,
               'packs':17,
               'rib':18,
               'ribs':18,
               'block':19,
               'blocks':19,
               'whole':20   }




abbre_dict = {'garlic':[10, 270, 2000],
              'salt':[0,0,0] }

garlic = abbre_dict["garlic"]
salt = abbre_dict["salt"]

print(garlic)
print(salt)
print("Garlic calories in grams is " + str(garlic[dict_table["ounce"]]))
print("Salt calories in grams is " + str(salt[1]))
