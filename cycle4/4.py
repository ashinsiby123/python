class Time:
	def __init__(self,hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	
	def cal_time(self):
		self.sum = self.hour+self.minute+self.second
		print("Time : ",self.sum)
	
	def __add__(self,second):
		if self.sum + second.sum:
			return True
		else:
			return False

print("Enter hour,minute and second of clock 1 : ")
h,m,s = int(input()), int(input()) , int(input())

print('Enter hour,minute and second of clock 2:')
h1,m1,s1 = int(input()), int(input()) , int(input())

print('clock 1 sum:')
t = Time(h,m,s)
t.cal_time()

print('clock 2 sum:')
t2 = Time(h1, m1,s1)
t2.cal_time()	
