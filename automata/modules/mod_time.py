from datetime import datetime


KEYWORDS = ['what', 'time']


def run(query=''):
	return datetime.now().strftime("%H:%M:%S")