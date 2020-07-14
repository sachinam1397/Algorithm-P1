import xlrd

class PlagiarismHandler():
	def __init__(self, fileName):
		self.plagData = xlrd.open_workbook(fileName)
		self.sheet = self.plagData.sheet_by_index(0)
		self.plagirisedData = {}
		for i in range(1,self.sheet.nrows):
			username = self.sheet.cell_value(i,1).split('@')
			self.plagirisedData[username[1]] = True


	def get_data(self):
		return self.plagirisedData


	def getStatus(self, userName):
		try:
			return self.plagirisedData[userName.lower()]
		except:
			return False



# if __name__ == '__main__':
# 	plagData = PlagiarismHandler("./AlgorithmsP1-plagiarism-report.xlsx")
# 	plagData1 = plagData.get_data()
# 	print(plagData.getStatus('tejas10p'))
# 	print(plagData.getStatus('akshat743'))
	