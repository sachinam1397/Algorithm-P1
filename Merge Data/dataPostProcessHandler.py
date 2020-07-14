from openpyxl import Workbook
# Batch enrolments:
# B1 1-32
# B2 33-64
# B3 65-96
# B4 97-129 , 264,269
# B5 130-160, 270
# B6 161-192, 265-268
# B7 178, 193-224
# B8 226-263 

class PostProcessHandler():
	def __init__(self, dataHandlerObject):
		# List of all batches
		self.batchList = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
		# This dict holds the batch data as list of tuples(enrolment, score)
		self.batchDict = {'B1' : [], 'B2' : [], 'B3' : [], 'B4' : [], 'B5' : [], 'B6' : [], 'B7' : [], 'B8' : [], "Unknown" : []}
		
		self.dataHandlerObject = dataHandlerObject

		self.makeDict()
		self.makeSheets()


	def makeDict(self):
		for enrolment in range(1, 271):
			enrolmentString = "181B" + "{0:0=3d}".format(enrolment)

			userData = self.dataHandlerObject.getUserData(enrolmentString)
			userBatch = self.getBatch(enrolmentString)

			if userData == None:
				userData = ('<< Unknown >>', enrolmentString, 4, 0, '-')

			print('Adding', enrolmentString, ' into batch:', userBatch)
			self.batchDict[userBatch].append(userData)


	def makeSheets(self):
		for batch in self.batchList:
			batchData = self.batchDict[batch]

			fileName = batch + '.xlsx'
			workbook = Workbook()
			activeSheet = workbook.active
			activeSheet.title = batch + ' Marks'
			activeSheet.append(('Hackerearth Username', 'Enrolment', 'Score', 'Problems Solved', 'Plagiarism Status'))

			for user in batchData:
				# user : (enrolment, score, problem solved, plag status)
				activeSheet.append(user)

			workbook.save(fileName)


	def getBatch(self, enrolment):
		# enrolment is in the form 181Bxxx, eDigit = xxx
		try:
			if type(enrolment) == type(""):
				eDigit = int(enrolment[4:])	# Remove 181B
		except:
			return "Unknown"

		if eDigit >= 1 and eDigit <= 32:
			return 'B1'
		elif eDigit >= 33 and eDigit <= 64:
			return 'B2'
		elif eDigit >= 65 and eDigit <= 96:
			return 'B3'
		elif (eDigit >= 193 and eDigit <= 224) or eDigit == 178:
			return 'B7'
		elif eDigit >= 226 and eDigit <= 263:
			return 'B8'
		elif (eDigit >= 97 and eDigit <= 129) or eDigit == 264 or eDigit == 269:
			return 'B4'
		elif (eDigit >= 130 and eDigit <= 160) or eDigit == 270:
			return 'B5'
		elif (eDigit >= 161 and eDigit <= 192) or eDigit in [265, 266, 267, 268]:
			return 'B6'
		else: 
			return 'Unknown'