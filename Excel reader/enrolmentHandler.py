import xlrd

class EnrolmentHandler():
	def __init__(self,fileName):
		self.enrolment = xlrd.open_workbook(fileName)
		self.sheet = self.enrolment.sheet_by_index(0)
		self.enrolment = {}
		for i in range(1,self.sheet.nrows):
			self.enrolment[self.sheet.cell_value(i,1)] = self.sheet.cell_value(i,2)



	def getEnrolment(self, userName = None):
		try:
			return self.enrolment[userName.lower()]
		except:
			return None


# if __name__ == '__main__':
# 	x = EnrolmentHandler('./Algorithm_P1.xlsx')
# 	for i in range(x.sheet.nrows):
# 		print(x.sheet.cell_value(i,0)," ",x.sheet.cell_value(i,1)," ",x.sheet.cell_value(i,2))