"""
This class reads the contest data and rprovides a getter for handler
"""
import xlrd


class ContestHandler():
	def __init__(self, fileName):
		self.all_records = xlrd.open_workbook(fileName)
		self.sheet = self.all_records.sheet_by_index(0)
		self.user = {}
		for i in range(1,self.sheet.nrows):
			self.temp_dict = {}
			self.temp_dict["Name"] = self.sheet.cell_value(i,0)
			self.temp_dict["Email"] = self.sheet.cell_value(i,1)
			self.temp_dict["Problems"]


	def getData(self, username = None):
		pass
		# return tuple(Username,Problems Solved,Tab Switch Count)

	def getUsernameList(self):
		pass


if __name__ == '__main__':
	contestData = ContestHandler("./AlgorithmsP1-result-837a223.xlsx")
	for i in range(contestData.sheet.ncols):
		print(contestData.sheet.cell_value(0,i))
	
