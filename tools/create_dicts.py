import sys

lines = []

lines.append("d_kinds = {   'gram':1,")
lines.append("\t\t\t   'grams':1,")
lines.append("\t\t\t   'g':1,")
lines.append("\t\t\t   'ounce':2,")
lines.append("\t\t\t   'ounces':2,")
lines.append("\t\t\t   'pound':3,")
lines.append("\t\t\t   'pounds':3,")
lines.append("\t\t\t   'lb':3,")
lines.append("\t\t\t   'lbs':3,")
lines.append("\t\t\t   'teaspoon':4,")
lines.append("\t\t\t   'teaspoons':4,")
lines.append("\t\t\t   'tablespoon':5,")
lines.append("\t\t\t   'tablespoons':5,")
lines.append("\t\t\t   'cup':6,")
lines.append("\t\t\t   'cups':6,")
lines.append("\t\t\t   'clove':7,")
lines.append("\t\t\t   'cloves':7,")
lines.append("\t\t\t   'can':8,")
lines.append("\t\t\t   'cans':8,")
lines.append("\t\t\t   'container':9,")
lines.append("\t\t\t   'containers':9,")
lines.append("\t\t\t   'crown':10,")
lines.append("\t\t\t   'crowns':10,")
lines.append("\t\t\t   'slice':11,")
lines.append("\t\t\t   'slices':11,")
lines.append("\t\t\t   'box':12,")
lines.append("\t\t\t   'boxes':12,")
lines.append("\t\t\t   'bottle':13,")
lines.append("\t\t\t   'bottles':13,")
lines.append("\t\t\t   'bunch':14,")
lines.append("\t\t\t   'bunches':14,")
lines.append("\t\t\t   'sprig':15,")
lines.append("\t\t\t   'sprigs':15,")
lines.append("\t\t\t   'jar':16,")
lines.append("\t\t\t   'jars':16,")
lines.append("\t\t\t   'wedge':17,")
lines.append("\t\t\t   'wedges':17,")
lines.append("\t\t\t   'pack':18,")
lines.append("\t\t\t   'packs':18,")
lines.append("\t\t\t   'rib':19,")
lines.append("\t\t\t   'ribs':19,")
lines.append("\t\t\t   'block':20,")
lines.append("\t\t\t   'blocks':20,")
lines.append("\t\t\t   'head':21,")
lines.append("\t\t\t   'heads':21,")
lines.append("\t\t\t   'whole':22   }")

lines.append("\n")


d_kinds = { 'gram':1,
               'grams':1,
               'g':1,
               'ounce':2,
               'ounces':2,
               'pound':3,
               'pounds':3,
               'lb':3,
               'lbs':3,
               'teaspoon':4,
               'teaspoons':4,
               'tablespoon':5,
               'tablespoons':5,
               'cup':6,
               'cups':6,
               'clove':7,
               'cloves':7,
               'can':8,
               'cans':8,
               'container':9,
               'containers':9,
               'crown':10,
               'crowns':10,
               'slice':11,
               'slices':11,
               'box':12,
               'boxes':12,
               'bottle':13,
               'bottles':13,
               'bunch':14,
               'bunches':14,
               'sprig':15,
               'sprigs':15,
               'jar':16,
               'jars':16,
               'wedge':17,
               'wedges':17,
               'pack':18,
               'packs':18,
               'rib':19,
               'ribs':19,
               'block':20,
               'blocks':20,
               'head':21,
               'heads':21,
               'whole':22,
               'stalk':23  }



il = open("ingredients.txt", 'r')
list_lines = il.readlines()                      # each line in a list
il.close()

lines.append("dict_cats = { ")

for line in list_lines:
        line = line.strip()
        if len(line) < 1:
            continue
        l_fig = line.split(":")

        # generate the rest here
        index = 0
        for value in l_fig:
            if index == 0:
                line = "\t\t\t\t" + "'" + l_fig[0] + "'" + ":"
            elif index == 1:
                line = line + "[" + "'" + l_fig[1] + "'"
            else:
                try: 
                    test = int(l_fig[index])
                    line = line + "," + l_fig[index]
                except:
                    l_id = l_fig[index].split("=")
                    if len(l_id) > 2:
                        print("The ingredients list has more than one = symbol in one of the lists")
                    sign = l_id[0].strip()
                    value = l_id[1].strip()
                    rup = d_kinds[sign] + 1
                    if rup > index:
                        while True:
                            line = line + ",-1"
                            index += 1
                            if index == rup:
                                break
                    line = line + "," + value
            index += 1
        while index < 24:
            line = line + ",-1"
            index += 1

        # finish up
        line = line + "],"
        lines.append(line)

lines.append("\t\t\t\t}")


f = open("calories.txt", 'w')
for line in lines:
    f.write(line + "\n")

f.close()
