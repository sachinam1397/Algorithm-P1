from plagiarismHandler import PlagiarismHandler
from enrolmentHandler import EnrolmentHandler
from generalHandler import GeneralHandler
from processData import ProcessData
from dataPostProcessHandler import PostProcessHandler


def main():
	# Read all 3 files and generate their handlers
	plagObject = PlagiarismHandler('./AlgorithmsP1-plagiarism-report.xlsx')
	enrolmentObject = EnrolmentHandler('./---enrolmentFile----.xlsx')    # Also, add these files into git repo
	contestDataObject = ContestHander('./---contest-report----.xlsx')

	# Process 3 files to create reports
	dataHandlerObject = ProcessData(plagObject, enrolmentObject, contestDataObject)

	# Get reports from processor and make reports
	PostProcessHandler(dataHandlerObject)
	

main()