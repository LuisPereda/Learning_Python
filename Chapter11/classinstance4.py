class Leapx_org():

	mul_num = 1.20
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
	
	def make_email(self):
		return self.f_name+ "."+self.l_name+"@xyz.com"
		
	def incrementpay(self):
		self.pay_amt = int(self.pay_amt*self.mul_num)
		return self.pay_amt
	
L_obj1 = Leapx_org('mohit', 'RAJ', 60000)
L_obj2 = Leapx_org('Ravender', 'Dahiya',70000) 

L_obj1.mul_num = 1.3

print "instance space L_obj1 \n",L_obj1.__dict__
print "\ninstance space L_obj2 \n",L_obj2.__dict__
print "\nclass space \n",Leapx_org.__dict__

print L_obj1.mul_num 
print L_obj2.mul_num 
print Leapx_org.mul_num


