import xlrd

class plagirise:

	def get_data():
		plagData = xlrd.open_workbook('./AlgorithmsP1-plagiarism-report.xlsx')
		sheet = plagData.sheet_by_index(0)
		return sheet


plagData = plagirise.get_data()
for i in range(plagData.ncols):
	print(plagData.cell_value(0,i))