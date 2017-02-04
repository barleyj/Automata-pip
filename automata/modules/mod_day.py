from datetime import datetime


KEYWORDS = ['what', 'day']


def run(query=''):
	return datetime.now().strftime("%A")