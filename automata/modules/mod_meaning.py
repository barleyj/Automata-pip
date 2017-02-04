from wordster import wordster


KEYWORDS = ['dictionary', 'meaning']


################################################################
# Find the next word of 'of'. Ex "Find the meaning of elephant"
# 'elephant' should be fed to the module
################################################################
def run(query=''):
	word = ''

	try:
		_query_list = query.split()
		for i in range(len(_query_list)):
			if _query_list[i].lower() == 'of':
				word = _query_list[i+1].lower()
				break
	except:
		print 'Something went wrong'

	_res = wordster.find_meaning(word)

	return _res[0]