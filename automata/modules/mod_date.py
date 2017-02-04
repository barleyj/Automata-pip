from datetime import datetime


KEYWORDS = ['what', 'date']


def run(query=''):
	return datetime.now().strftime("%Y:%m:%d")