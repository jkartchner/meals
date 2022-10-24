d_kinds = {   'gram':1,
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
			   'stalk':23,
			   'stalks':23,
			   'rib':24,
			   'ribs':24   }


dict_cats = { 
				'almonds':['produce',5.86,164,2624,11.02,33.06,529,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,-1,-1],
				'almond':['produce',5.86,164,2624,11.02,33.06,529,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,-1,-1],
				'apple':['produce',0.53,15,237,1.19,3.56,57,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,95,-1,-1],
				'apples':['produce',0.53,15,237,1.19,3.56,57,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,95,-1,-1],
				'avocados':['produce',1.76,50,800,5,15,240,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,320,-1,-1],
				'avocado':['produce',1.76,50,800,5,15,240,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,320,-1,-1],
				'baby bok choy':['produce',0.124,3.52,56.4,0.21,0.62,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'bananas':['produce',0.9,25.15,408.24,4.17,12.50,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,105,-1,-1],
				'banana':['produce',0.9,25.15,408.24,4.17,12.50,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,105,-1,-1],
				'bell pepper':['produce',0.32,9,144,0.58,1.75,28,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,37,-1,-1],
				'blackberries':['produce',0.42,12,195,1.29,3.88,62,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'blueberries':['produce',0.6,16,256,1.67,5,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'bok choy':['produce',0.14,4,64,0.21,0.62,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,110,-1,-1,-1],
				'broccoli':['produce',0.35,10,160,0.65,1.94,31,-1,-1,-1,30,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cabbage':['produce',0.25,7,112,0.35,1.06,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'carrot':['produce',0.42,12,192,0.94,2.81,45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1],
				'carrots':['produce',0.42,12,192,0.94,2.81,45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1],
				'cashews':['produce',5.54,157,2512,15.08,45.25,724,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,-1,-1],
				'cashew':['produce',5.54,157,2512,15.08,45.25,724,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,-1,-1],
				'cherry tomatoes':['produce',0.18,5,80,0.52,1.56,25,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1],
				'celery':['produce',0.14,4,64,0.29,0.88,14,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,10,10],
				'chia seeds':['produce',4.87,138,2208,16.67,50.00,800,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cilantro':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'dates':['produce',2.82,79.81,1277,8.62,25.88,414,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'dill':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'fresh dill':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'fresh basil':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'fresh cilantro':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'fresh ginger':['produce',0.81,23,368,1.58,4.75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'fresh mozzarella':['produce',2.79,79,1264,7.71,23.12,370,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'fresh parsley':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'garlic':['produce',1.48,42,672,4.23,12.69,203,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'ginger root':['produce',0.81,23,368,1.58,4.75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'ginger':['produce',0.81,23,368,1.58,4.75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'green bell pepper':['produce',0.21,6,96,0.38,1.12,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,24,-1,-1],
				'green bell peppers':['produce',0.21,6,96,0.38,1.12,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,24,-1,-1],
				'green onions':['produce',0.33,9.44,151,0.67,2.00,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'green peppers':['produce',0.21,6,96,0.38,1.12,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,24,-1,-1],
				'green pepper':['produce',0.21,6,96,0.38,1.12,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,24,-1,-1],
				'iceburg lettuce':['produce',0.13,3.56,57,0.21,0.62,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'jalapenos':['produce',0.29,8.19,131,0.54,1.62,26,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1],
				'jalapeno':['produce',0.29,8.19,131,0.54,1.62,26,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1],
				'jalapeno pepper':['produce',0.29,8.19,131,0.54,1.62,26,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1],
				'jalapeno peppers':['produce',0.29,8.19,131,0.54,1.62,26,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1],
				'lemon':['produce',0.29,8.31,133,1.27,3.81,61,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,17,-1,-1],
				'lemons':['produce',0.29,8.31,133,1.27,3.81,61,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,17,-1,-1],
				'lemon juice':['produce',0.22,6.19,99,1.10,3.31,53,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'lettuce':['produce',0.13,3.56,57,0.21,0.62,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'lime':['produce',0.30,8.44,135,0.42,1.25,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,20,-1,-1],
				'limes':['produce',0.30,8.44,135,0.42,1.25,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,20,-1,-1],
				'lime juice':['produce',0.25,7,112,1.25,3.75,60,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'onion':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'onions':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'oranges':['produce',0.47,13.31,213,1.77,5.31,85,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,60,-1,-1],
				'orange':['produce',0.47,13.31,213,1.77,5.31,85,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,60,-1,-1],
				'parmesan cheese':['produce',4.30,122,1952,8.98,26.94,431,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'parmiggiano reggiano':['produce',4.40,124.75,1996,8.98,26.94,431,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pecans':['produce',6.91,196.00,3136,15.69,47.06,753,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pecan':['produce',6.91,196.00,3136,15.69,47.06,753,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pecorino romano':['produce',3.87,109.69,1755,8.98,26.94,431,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'potato':['produce',0.97,27.50,440,1.23,3.69,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'potatoes':['produce',0.97,27.50,440,1.23,3.69,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pumpkin seeds':['produce',4.44,126,2016,5.94,17.81,285,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'peach':['produce',0.41,11.56,185,1.38,4.12,66,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,61,-1,-1],
				'peaches':['produce',0.41,11.56,185,1.38,4.12,66,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,61,-1,-1],
				'raspberries':['produce',0.53,15,240,1.35,4.06,65,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'raspberry':['produce',0.53,15,240,1.35,4.06,65,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'red bell pepper':['produce',0.32,9,144,0.58,1.75,28,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,37,-1,-1],
				'red onion':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'red onions':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'red pepper':['produce',0.32,9,144,0.58,1.75,28,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,37,-1,-1],
				'red peppers':['produce',0.32,9,144,0.58,1.75,28,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,37,-1,-1],
				'roasted almonds':['produce',5.86,164,2624,11.02,33.06,529,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,-1,-1],
				'roasted cashews':['produce',5.54,157,2512,15.08,45.25,724,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,-1,-1],
				'roma tomato':['produce',0.18,5.12,82,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1],
				'roma tomatoes':['produce',0.18,5.12,82,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1],
				'roma tomatos':['produce',0.18,5.12,82,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1],
				'russet potato':['produce',0.97,27.50,440,1.23,3.69,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'russet potatoes':['produce',0.97,27.50,440,1.23,3.69,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sage':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'salad mix':['produce',0.18,5,80,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'scallions':['produce',0.33,9.44,151,0.67,2.00,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'scallion':['produce',0.33,9.44,151,0.67,2.00,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'serrano chilis':['produce',0.32,9,144,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'serrano chili':['produce',0.32,9,144,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'serranos':['produce',0.32,9,144,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'spinach':['produce',0.23,6.62,106,0.15,0.44,7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'spinach leaves':['produce',0.23,6.62,106,0.15,0.44,7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sunflower seeds':['produce',5.86,166,2656,17.04,51.12,818,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'strawberries':['produce',0.32,9.06,145,1.02,3.06,49,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'strawberry':['produce',0.32,9.06,145,1.02,3.06,49,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sweet onions':['produce',0.32,9,144,0.98,2.94,47,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'sweet onion':['produce',0.32,9,144,0.98,2.94,47,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'swiss cheese':['produce',3.81,108,1728,10.46,31.38,502,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'thyme':['produce',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'tomato':['produce',0.18,5.12,82,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1],
				'tomatoes':['produce',0.18,5.12,82,0.67,2,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1],
				'vidalia onion':['produce',0.32,9,144,0.98,2.94,47,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'vidalia onions':['produce',0.32,9,144,0.98,2.94,47,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1,-1],
				'white onion':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,-1],
				'white onions':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,-1],
				'yellow onion':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,-1],
				'yellow onions':['produce',0.42,11.94,191,1.33,4,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,-1],
				'bacon':['meat',5.37,152.38,2438,-1,-1,-1,-1,-1,-1,-1,43,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chicken':['meat',2.39,67.81,1085,4.81,14.44,231,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chicken breasts':['meat',2.39,67.81,1085,4.81,14.44,231,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,284,-1,-1],
				'chicken breast':['meat',2.39,67.81,1085,4.81,14.44,231,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,284,-1,-1],
				'chicken thighs':['meat',1.78,50.38,806,5.81,17.44,279,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,206,-1,-1],
				'chicken thigh':['meat',1.78,50.38,806,5.81,17.44,279,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,206,-1,-1],
				'ground beef':['meat',3.32,94.12,1506,6.04,18.12,290,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'hot dogs':['meat',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,151,-1,-1],
				'hot dog':['meat',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,151,-1,-1],
				'pepperoni':['meat',4.94,140,2240,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pico de gallo':['meat',0.31,8.88,142,1.67,5,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pork butt':['meat',2.68,76.06,1217,8.35,25.06,401,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pork shoulder':['meat',2.68,76.06,1217,8.35,25.06,401,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pork tenderloin':['meat',1.44,40.69,651,4.54,13.62,218,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'steak':['meat',2.71,76.69,1227,7.04,21.12,338,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,679,-1,-1],
				'steaks':['meat',2.71,76.69,1227,7.04,21.12,338,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,679,-1,-1],
				'stew beef':['meat',2.07,58.75,940,7.04,21.12,338,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'turkey kielbasa sausage':['meat',1.59,45,720,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'flounder filets':['seafood',0.91,25.81,413,3.23,9.69,155,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,173,-1,-1],
				'salmon':['seafood',2.08,59.00,944,4.83,14.50,232,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,175,-1,-1],
				'salmon filets':['seafood',2.08,59.00,944,4.83,14.50,232,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,250,-1,-1],
				'salmon filet':['seafood',2.08,59.00,944,4.83,14.50,232,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,250,-1,-1],
				'shrimp':['seafood',0.99,28.06,449,4.35,13.06,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,7,-1,-1],
				'sole filets':['seafood',0.91,25.81,413,3.23,9.69,155,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,173,-1,-1],
				'donut':['bakery',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,290,-1,-1],
				'donuts':['bakery',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,290,-1,-1],
				'brownies':['bakery',320,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'lemon squares':['bakery',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,330,-1,-1],
				'granola':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'multigrain bread':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,130,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'potato bread':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sandwich bread':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'wheat bread':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,120,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'white bread':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,110,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'whole wheat bread':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'hot dog buns':['bread',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'hamburger buns':['buns',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'all purpose flour':['baking',3.64,103.19,1651,9.48,28.44,455,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'all-purpose flour':['baking',3.64,103.19,1651,9.48,28.44,455,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'baking powder':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'baking soda':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'basil':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'bay leaves':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'bay leaf':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'black pepper':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'bread flour':['baking',3.67,104.04,1664.71,9.17,27.50,440,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'brown sugar':['baking',3.70,105,1680,17.42,52.25,836,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'canola oil':['baking',8.82,250.12,4002,40.15,120.44,1927,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cornmeal':['baking',3.70,105,1680,12.10,36.31,581,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chicken bouillon':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'chocolate':['baking',5.38,152.52,2440.37,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chili flake':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'chili powder':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'cinnamon':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'coconut oil':['baking',8.61,244,3904,39.15,117.44,1879,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cornstarch':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'cumin':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'dried basil':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'dried oregano':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'dried parsley':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'extra virgin olive oil':['baking',8.85,251,4016,39.77,119.31,1909,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'flour':['baking',3.64,103.19,1651,9.48,28.44,455,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'fine sea salt':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'food coloring':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'garlic powder':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'granulated sugar':['baking',3.91,110.94,1775,16.10,48.31,773,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'ground coriander':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'ground ginger':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'ground paprika':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'instant yeast':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'kosher salt':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'mini marshmallows':['baking',3.25,92.00,1472,3.31,9.94,159,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'maltose':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'marshmallows':['baking',3.17,90,1440,3.31,9.94,159,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'molasses':['baking',2.89,82.00,1312,20.35,61.06,977,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'nutmeg':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'oat flour':['baking',4.06,115,1840,8.75,26.25,420,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'old fashioned oats':['baking',3.88,110,1760,7.60,22.81,365,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'olive oil':['baking',8.85,251,4016,39.77,119.31,1909,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'onion powder':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'oregano':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'paprika':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'parchment paper':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'parsley':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'pectin':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'pepper':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'protein powder':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'red pepper flakes':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'rolled oats':['baking',3.88,110,1760,7.60,22.81,365,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'salt':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'sherry vinegar':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'shredded coconut':['baking',6.53,185,2960,5.90,17.69,283,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sugar':['baking',3.91,110.94,1775,16.10,48.31,773,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'tempura flour':['baking',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'vanilla extract':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'vegetable oil':['baking',8.82,250.12,4002,40.15,120.44,1927,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'wax paper':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'white pepper':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'white vinegar':['baking',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'artichoke hearts':['baking',0.35,10,160,2.42,7.25,116,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'black beans':['canned goods',0.92,26,416,4.73,14.19,227,-1,110,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'black olives':['canned goods',1.06,30,480,3.21,9.62,154,-1,116,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'crushed tomatoes':['canned goods',0.32,9,144,0.67,2,32,-1,136,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'calabrian chilis':['canned goods',2.50,70.88,1134,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1],
				'diced tomatoes':['canned goods',0.18,5,80,0.67,2,32,-1,105,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'fruit cocktail':['canned goods',0.49,14,224,2.27,6.81,109,-1,120,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'pepperoncini':['canned goods',0.39,11,176,1.25,3.75,60,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'tomato paste':['canned goods',0.81,23,368,4.48,13.44,215,-1,139,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'tomato sauce':['canned goods',0.28,8,128,1.46,4.38,70,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chicken stock':['soups',0.04,1,16,1.79,5.38,86,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'basmati rice':['asian',3.58,101.59,1625.44,13.33,40,640,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'coconut milk':['asian',2.26,64,1024,11.50,34.50,552,-1,120,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chili paste':['asian',1.02,29,464,5.00,15,240,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chinese rose wine':['asian',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'fish sauce':['asian',0.32,9,144,2,6,96,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'five spice powder':['asian',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'hoisin sauce':['asian',2.19,62,992,11.67,35,560,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'jasmine rice':['asian',3.83,108.50,1736,53.33,160,640,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'medium grain rice':['asian',3.58,101.59,1625.44,13.33,40,640,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'medium-grain rice':['asian',3.58,101.59,1625.44,13.33,40,640,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'oyster sauce':['asian',0.49,14,224,3,9,144,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sesame oil':['asian',8.82,250,4000,40,120,1920,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sesame seeds':['asian',6,170.10,2721.60,17,51,816,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'soy sauce':['asian',0.56,16,256,3,9,144,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'teriyaki sauce':['asian',0.88,25,400,5.33,16,256,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'teriyaki sauces':['asian',0.88,25,400,5.33,16,256,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'thai red curry paste':['asian',1.00,28.35,453.60,10,30,480,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chiles in adobo':['hispanic',0.78,22,352,6,18,288,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chipotle peppers':['hispanic',0.78,22,352,6,18,288,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chipotle pepper':['hispanic',0.78,22,352,6,18,288,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'chipotle peppers in adobo sauce':['hispanic',0.78,22,352,6,18,288,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'hot sauce':['hispanic',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'pinto beans':['hispanic',0.88,25,400,2.60,7.81,125,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'taco shell':['hispanic',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,60,-1,-1],
				'taco shells':['hispanic',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,60,-1,-1],
				'angel hair noodles':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'angel hair':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cavatappi pasta':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cavatappi noodles':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cavatappi':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'egg noodles':['pasta',3.84,109,1744,4.60,13.81,221,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'elbow noodles':['pasta',3.74,106,1696,8.12,24.38,390,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'elbow pasta':['pasta',3.74,106,1696,8.12,24.38,390,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'thin spaghetti noodles':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,1600,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'thin spaghetti':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,1600,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'linguine':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,1600,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'linguine noodles':['pasta',3.53,100,1600,4.35,13.06,209,-1,-1,-1,-1,-1,1600,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'spaghetti':['pasta',3.53,100,1600,-1,-1,-1,-1,-1,-1,-1,-1,1600,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'spaghetti noodles':['pasta',3.53,100,1600,-1,-1,-1,-1,-1,-1,-1,-1,1600,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'barbeque sauce':['pasta',1.69,48,768,10,30,480,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'barbecue sauce':['pasta',1.69,48,768,10,30,480,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'ketchup':['condiments',1.13,32,512,5.58,16.75,268,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'catsup':['condiments',1.13,32,512,5.58,16.75,268,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'mayonnaise':['condiments',6.81,193,3088,31.15,93.44,1495,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'salad dressing':['condiments',4.83,137,2192,24.33,73,1168,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'frozen broccoli':['frozen foods',0.35,10,160,0.65,1.94,31,-1,-1,-1,30,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'frozen pizza':['frozen foods',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'frozen strawberries':['frozen foods',0.32,9.06,145,1.02,3.06,49,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'orange juice':['frozen foods',0.46,13,208,2.31,6.94,111,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'honey':['cereal',3.03,86,1376,21.48,64.44,1031,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'jam':['cereal',2.79,79,1264,18.67,56,896,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'maple syrup':['cereal',2.61,74,1184,17.06,51.19,819,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'peanut butter':['cereal',5.89,167,2672,31.62,94.88,1518,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'rice krispies':['cereal',3.81,108,1728,2.10,6.31,101,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'rolled oats':['cereal',3.88,110,1760,7.60,22.81,365,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'1% milk':['dairy',0.42,12,192,2.15,6.44,103,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'2% milk':['dairy',0.49,14,224,2.58,7.75,124,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'butter':['dairy',7.20,204,3264,33.90,101.69,1627,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'buttermilk':['dairy',0.39,11,176,2.06,6.19,99,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cheddar cheese':['dairy',4.02,114,1824,11.06,33.19,531,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'cream cheese':['dairy',3.42,97,1552,16.52,49.56,793,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'eggs':['dairy',1.55,44,704,4.40,13.19,211,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,80,-1,-1],
				'egg':['dairy',1.55,44,704,4.40,13.19,211,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,80,-1,-1],
				'fresh mozzarella':['dairy',2.79,79,1264,7.71,23.12,370,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'heavy cream':['dairy',3.63,103,1648,17.10,51.31,821,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'heavy whipping cream':['dairy',3.63,103,1648,17.10,51.31,821,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'milk':['dairy',0.60,17,272,3.08,9.25,148,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'monterey jack cheese':['dairy',3.74,106,1696,10.27,30.81,493,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'monterey jack':['dairy',3.74,106,1696,10.27,30.81,493,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'mozzarella':['dairy',2.79,79,1264,7.71,23.12,370,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'provolone':['dairy',3.53,100,1600,9.67,29,464,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'skim milk':['dairy',0.35,10,160,1.79,5.38,86,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'sour cream':['dairy',1.90,54,864,9.27,27.81,445,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'unsalted butter':['dairy',7.20,204,3264,33.90,101.69,1627,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'whole milk':['dairy',0.60,17,272,3.08,9.25,148,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'yogurt':['dairy',0.60,17,272,2.08,6.25,100,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'toilet paper':['toilet paper',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'beer':['junk food',0.42,12,192,2.17,6.50,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'doritos':['junk food',5.29,150,2400,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				'soda':['junk food',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'water':['junk food',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
				'white wine':['junk food',0.81,23,368,4,12,192,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
				}
