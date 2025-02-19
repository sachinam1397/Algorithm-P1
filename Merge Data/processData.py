class ProcessData():
	def __init__(self, plagObject, enrolmentObject, contestDataObject):
		self.plagObject = plagObject
		self.enrolmentObject = enrolmentObject
		self.contestDataObject = contestDataObject

		self.allDict = {}
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
			userPlagiarismStatus = self.plagObject.getStatus(user)

			userEnrolment = self.enrolmentObject.getEnrolment(user)
			print('For user', user, ' got enrolment:', userEnrolment)
			if userEnrolment == None:
				# Fuck you user :P
				continue

			userContestID = userData.get("Contest ID", 'A')		# Contest A or B
			if userContestID == 'A':
				fullMarks = 
				halfMarks = 
				noneMarks = 
			else:
				fullMarks = 
				halfMarks = 
				noneMarks = 
			discMarks = 

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

			# store data
			data = (user, userEnrolment.lower(), score, userProblemSolved, userPlagiarismStatus)
			self.allDict[userEnrolment.lower()] = data

	def getUserData(self, enrolment):
		# Expected enrolment as an integer
		print('Request for enrolment:', enrolment, end = '')
		data = self.allDict.get(enrolment.lower(), None)
		if data == None:
			print(' : Did not get any data!')
		return data
