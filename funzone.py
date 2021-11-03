from collections import namedtuple, defaultdict
from datetime import datetime

class Ticket:

	def __init__(self):
		self.filename 	= "nyc_parking_tickets_extract.csv"
		self.func_list	= (self.parser_int,
	                		self.parser_str,
	                		lambda x: self.parser_str(x, default='fred'),
	                		lambda x: self.parser_str(x, default='fred'),
	                		self.parser_date,
	                		self.parser_int,
	                		lambda x: self.parser_str(x, default='fred'),
	                		self.parser_str,
	                		lambda x: self.parser_str(x, default='fred')
	            			)
		headers = self.header_parser()
		self.ticket = namedtuple("Ticket", headers)

	def header_parser(self):
		with open(self.filename) as file:
			row = next(file)
		return [label.replace(" ","_") for label in row.strip().split(",")]

	def row_parser(self, row):
		data_cleaned = [func(field) for func, field in zip(self.func_list, row.strip().split(","))]
		return self.ticket(*data_cleaned)

	def read_data(self):
		with open(self.filename) as file:
			next(file)
			yield from file

	def parsed_data(self):
		for row in self.read_data():
			data = self.row_parser(row)
			yield data

	def parser_int(self,value, *other, default=None):
		try:
			return int(value)
		except ValueError:
			return default

	def parser_date(self,value, *other, default=None):
		try:
			return datetime.strptime(value, '%m/%d/%Y').date()
		except ValueError:
			return default

	def parser_str(self,value, *other, default=None):
		try:
			if value.strip() == '':
				return default
			else:
				return str(value)
		except ValueError:
			return default

	

