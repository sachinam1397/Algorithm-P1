import xlrd

class PlagiarismHandler():
	def __init__(self, fileName):
		self.plagData = xlrd.open_workbook(fileName)


	def get_data():
		sheet = self.plagData.sheet_by_index(0)
		return sheet


	def getStatus(self, userName):
		# return if userName is plagiarising or not ( bool )



if __name__ == '__main__':
	plagData = plagirise.get_data()
	for i in range(plagData.ncols):
		print(plagData.cell_value(0,i))