from sampleOO import *

t = Ticket(100)
print(t.discountedValue())

t1 = SeniorTicket(100)
print(t1.discountedValue())

t2 = KidsTicket(100)
print(t2.discountedValue())
print(t2.prize())


t3 = GratuityTicket(100)
print(t3.discountedValue())

