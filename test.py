import unittest
from sampleOO import * 

class TicketTest(unittest.TestCase):
	def test_NormalTicket(self):
		ticket = Ticket(50)
		self.assertEqual(ticket.discountedValue(), 50)

	def test_SeniorTicket(self):
		ticket = SeniorTicket(50)
		self.assertEqual(ticket.discountedValue(), 25)

	def test_KidsTicket(self):
		ticket = KidsTicket(50)
		self.assertEqual(ticket.discountedValue(), 37.5)

	def test_GratuityTicket(self):
		ticket = GratuityTicket(50)
		self.assertEqual(ticket.discountedValue(), 0)

if __name__ == '__main__':
	unittest.main()