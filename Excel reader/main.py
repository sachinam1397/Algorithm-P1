from plagiarismHandler import PlagiarismHandler
from enrolmentHandler import EnrolmentHandler
from generalHandler import GeneralHandler
from processData import ProcessData
from dataPostProcessHandler import PostProcessHandler


def main():
	# Read all 3 files and generate their handlers
	plagObject = PlagiarismHandler('./AlgorithmsP1-plagiarism-report.xlsx')
	enrolmentObject = EnrolmentHandler('./Algorithm_P1.xlsx')    # Also, add these files into git repo
	contestDataObject = ContestHander('./AlgorithmsP1-result-7250d07.xls')

	# Process 3 files to create reports
	dataHandlerObject = ProcessData(plagObject, enrolmentObject, contestDataObject)

	# Get reports from processor and make reports
	PostProcessHandler(dataHandlerObject)
	

main()