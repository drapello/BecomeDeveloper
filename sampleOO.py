class Ticket:
	def __init__(self, price):
		self.price = price
	
	def discountedValue(self):
		return self.price

class SeniorTicket(Ticket):
	def discountedValue(self):
		return self.price - (self.price*0.5)

class KidsTicket(Ticket):

	def prize(self):
		return "You got a prize!"

	def discountedValue(self):
		return self.price - (self.price*0.25)

class GratuityTicket(Ticket):
	def discountedValue(self):
		return 0
