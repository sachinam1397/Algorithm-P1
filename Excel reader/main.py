from plagiarismHandler import PlagiarismHandler
from enrolmentHandler import EnrolmentHandler
from generalHandler import GeneralHandler

def main():
	plagObject = PlagiarismHandler('./AlgorithmsP1-plagiarism-report.xlsx')
	enrolmentObject = EnrolmentHandler('./---enrolmentFile----.xlsx')    # Also, add these files into git repo
	contestDataObject = ContestHander('./---contest-report----.xlsx')

main()