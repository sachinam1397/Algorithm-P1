from plagiarismHandler import PlagiarismHandler
from enrolmentHandler import EnrolmentHandler
from contestHandler import ContestHandler
from processData import ProcessData
from dataPostProcessHandler import PostProcessHandler


def main():
	# Read all 3 files and generate their handlers
	plagObject = PlagiarismHandler('AlgorithmsP1-Retest-plagiarism-report.xlsx')
	enrolmentObject = EnrolmentHandler('Algo P1 (Second).xlsx')    # Also, add these files into git repo
	contestDataObject = ContestHandler('AlgorithmsP1-Retest-result-3bd74ca.xlsx')

	# Process 3 files to create reports
	dataHandlerObject = ProcessData(plagObject, enrolmentObject, contestDataObject)

	# Get reports from processor and make reports
	PostProcessHandler(dataHandlerObject)
	

main()