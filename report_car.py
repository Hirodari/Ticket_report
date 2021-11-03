#The code below generate a report of number of tickets per car make
#from a csv format file
from funzone import  Ticket
from collections import defaultdict

myticket = Ticket()

def ticket_dict():
	make_count = defaultdict(int)
	for row in myticket.parsed_data():
		make_count[row.Vehicle_Make] += 1

	return {make: cnt for make, cnt in
			sorted(make_count.items(), key=lambda t: t[1],
			reverse=True)}


print("="*135)
car = ticket_dict()
for ticket in car.items():
	print(f"{ticket[0]} received {ticket[1]} times", end="| ")
print()
print("="*135)
