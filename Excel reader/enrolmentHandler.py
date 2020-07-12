import xlrd

class EnrolmentHander():
	def __init__(self,fileName):
		self.enrolment = xlrd.open_workbook(fileName)
		self.sheet = self.enrolment.sheet_by_index(0)
		self.enrolment = {}
		for i in range(1,self.sheet.nrows):
			self.enrolment[self.sheet.cell_value(1,i)] = self.sheet.cell_value(i,2)



	def getEnrolment(self, userName = None):
		try:
			return self.enrolment[userName]
		except:
			return "000000"


# if __name__ == '__main__':
# 	x = EnrolmentHander()
# 	for i in range(x.sheet.ncols):
# 		print(x.sheet.cell_value(0,i))