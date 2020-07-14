from plagiarismHandler import PlagiarismHandler
from enrolmentHandler import EnrolmentHandler
from contestHandler import ContestHandler
from processData import ProcessData
from dataPostProcessHandler import PostProcessHandler


def main():
	# Read all 3 files and generate their handlers
	plagObject = PlagiarismHandler('AlgorithmsP1-plagiarism-final.xlsx')
	enrolmentObject = EnrolmentHandler('Algo P1 -final.xlsx')    # Also, add these files into git repo
	contestDataObject = ContestHandler('AlgorithmsP1-result-final.xlsx')

	# Process 3 files to create reports
	dataHandlerObject = ProcessData(plagObject, enrolmentObject, contestDataObject)

	# Get reports from processor and make reports
	PostProcessHandler(dataHandlerObject)
	

main()