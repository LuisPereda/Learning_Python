class Leapx_org():
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
	
	def make_email(self):
		return self.f_name+ "."+self.l_name+"@xyz.com"
	
L_obj1 = Leapx_org('mohit', 'RAJ', 60000)
L_obj2 = Leapx_org('Ravender', 'Dahiya',70000) 

print L_obj1.full_name
print L_obj1.make_email()

print L_obj2.full_name
print L_obj2.make_email()

