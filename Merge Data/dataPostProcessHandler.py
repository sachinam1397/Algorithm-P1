from openpyxl import Workbook

class PostProcessHandler():
	def __init__(self, dataHandlerObject):
		self.batchList = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'Unknown']
		self.dataHandlerObject = dataHandlerObject

		self.makeSheets()


	def makeSheets(self):
		for batch in self.batchList:
			batchData = self.dataHandlerObject.getBatchReport(batch)
			fileName = batch + '.xlsx'
			
			workbook = Workbook()
			activeSheet = workbook.active
			activeSheet.title = batch + ' Marks'
			activeSheet.append(('Hackerearth Username', 'Enrolment', 'Score', 'Problems Solved', 'Plagiarism Status'))

			for user in batchData:
				# user : (enrolment, score, problem solved, plag status)
				activeSheet.append(user)

			workbook.save(fileName)