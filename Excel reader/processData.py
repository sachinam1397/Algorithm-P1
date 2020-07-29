# Batch enrolments:
# B1 1-32
# B2 33-64
# B3 65-96
# B4 97-129 , 264,269
# B5 130-160, 270
# B6 161-192, 265-268
# B7 178, 193-224
# B8 226-263

class ProcessData():
	def __init__(self, plagObject, enrolmentObject, contestDataObject):
		self.plagObject = plagObject
		self.enrolmentObject = enrolmentObject
		self.contestDataObject = contestDataObject

		# This dict holds the batch data as list of tuples(enrolment, score)
		self.batchDict = {'B1' : [], 'B2' : [], 'B3' : [], 'B4' : [], 'B5' : [], 'B6' : [], 'B7' : [], 'B8' : [], 'Unknown' : []}
		# Get the list of user names from contest class
		self.userList = self.contestDataObject.getUserNameList()		
		# Make results
		self.makeResults()


	def makeResults(self):
		# For every user,
		for user in self.userList:
			# Get user contest data
			userData = self.contestDataObject.getData(user)	
			userProblemSolved = userData["Problems Solved"]
			userTabSwitches = userData["Tab Switches"]
			userContestID = userData["Contest ID"]		# Contest A or B
			userPlagiarismStatus = self.plagObject.getStatus(user)

			if userContestID == 'A':
				fullMarks = 
				halfMarks = 
				noneMarks = 
			else:
				fullMarks = 
				halfMarks = 
				noneMarks = 
			discMarks = 

			userEnrolment = self.enrolmentObject.getEnrolment(user)
			# print(userEnrolment)
			if userEnrolment == None:
				# Bad google form response
				userEnrolment = 'Incorrect Form data filled.'
				userBatch = 'Unknown'
			else:
				userBatch = self.getBatch(userEnrolment)

			# Check user plagiarism status
			if userPlagiarismStatus == True:
				score = discMarks
				userPlagiarismStatus = 'Disqualified due to Plagiarism'
				if userTabSwitches > 5:
					userProblemSolved = 'Also disqualified due to Tab switches'

			elif userTabSwitches > 5:
				score = discMarks
				userProblemSolved = 'Disqualified due to Tab switches'
				userPlagiarismStatus = '-'

			elif userProblemSolved == 0:
				score = noneMarks
				userPlagiarismStatus = '-'

			elif userProblemSolved == 1: 
				score = halfMarks
				userPlagiarismStatus = '-'

			elif userProblemSolved == 2:
				score = fullMarks
				userPlagiarismStatus = '-'

			# Make data in required format
			data = (user, userEnrolment, score, userProblemSolved, userPlagiarismStatus)

			# Store data
			self.batchDict[userBatch].append(data)

			
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
		

	def getBatchReport(self, batch = 'B1'):
		return self.batchDict.get(batch, [])
