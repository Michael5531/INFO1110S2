item_list = []
cost_list = []
def mean(cost_list):
	return sum(cost_list) / len(cost_list)
while True:
	item_cost_input = input("Enter item and cost: ")
	if item_cost_input == "stop":
		if len(cost_list) == 0:
			print("No items entered.")
			quit()
		else:
			mean = float(mean(cost_list))
			i = 0
			counter = 0
			print("The average cost of all items is ${:.2f}.".format(mean))
			while i < len(cost_list):
				if cost_list[i] > mean:
					counter += 1
				i += 1
			if counter == 1:
				print("There is 1 item above average cost.")
				quit()
			else:
				print("There are {} items above average cost.".format(counter))
				quit()
	if len(item_cost_input.split(" ")) > 2:
		print("Invalid input. Requires item and cost.")
		continue
	if len(item_cost_input.split(" ")) == 2:
		item = item_cost_input.split(" ")[0]
		cost = item_cost_input.split(" ")[1]
	else:
		print("Invalid input. Requires item and cost.")
		continue
	try:
		if float(cost) < 0:
			print("Invalid input. {} cannot have negative cost.".format(item))
			continue
	except Exception:
		print("Invalid input. Cost must be numeric.")
	else:
		item_list.append(item)
		cost_list.append(float(cost))
print("The average cost of all items is ${:.2f}.".format(mean(cost_list)))
