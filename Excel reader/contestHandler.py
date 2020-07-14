"""
This class reads the contest data and rprovides a getter for handler
"""
import xlrd


class ContestHandler():
	def __init__(self, fileName):
		self.all_records = xlrd.open_workbook(fileName)
		self.sheet = self.all_records.sheet_by_index(0)
		self.user = {}
		for i in range(1, self.sheet.nrows):
			self.temp_dict = {}
			self.temp_dict["Name"] = self.sheet.cell_value(i,0)
			self.temp_dict["Email"] = self.sheet.cell_value(i,1)
			self.temp_dict["Problems Solved"] = ((int(self.sheet.cell_value(i,11))//4) + (int(self.sheet.cell_value(i,12))//4))
			self.temp_dict["Tab Switches"] = self.sheet.cell_value(i,7)

			username = self.sheet.cell_value(i,9).split('@')
			username = username[1].lower()
			# --------------------------------------------------------------------
			# New changes here:
			self.contestID = self.sheet.cell_value(i,    x      )

			if self.contestID == 'B':
				# Overwrite any data for contest A, as contest B has more priority
				self.user[username] = self.temp_dict

			elif self.contestID == 'A':
				# Check if any record of contest B for this user has already been read:
				data_ = self.user.get(username, None)
				# If no previous record is found:
				if data_ == None:
					# User has not given contest B, so accept this contest data
					self.user[username] = self.temp_dict


	def getData(self, username = None):
		return self.user[username.lower()]

	def getUserNameList(self):
		usernameList = []
		for key,value in self.user.items():
			usernameList.append(key)
		return usernameList


# if __name__ == '__main__':
# 	contestData = ContestHandler("./AlgorithmsP1-result-837a223.xlsx")
# 	for key,value in contestData.user.items():
# 		print(key, " : ", value)
	
