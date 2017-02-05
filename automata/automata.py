import os
import sys
import re
import operator


class Automata:

	def __init__(self, module_path=''):
		self.dir_name = os.path.dirname(os.path.realpath(__file__))

		if module_path == '':
			module_path = self.dir_name + '/modules'

		self.modules_dir = module_path
		self.modules_dict = {}
		self.import_modules()

	def import_modules(self):
		sys.path.append(self.modules_dir)

		for module in os.listdir(self.modules_dir):
			if module == '__init__.py' or module[-3:] != '.py':
				continue

			self.modules_dict[module[:-3]] = (__import__(module[:-3]))

	def execute(self, query):
		module_match_dict = {}

		for module in self.modules_dict:
			count = 0
			module_obj = self.modules_dict[module]

			for keyword in module_obj.KEYWORDS:
				if re.findall(keyword, query, re.I):
					count += 1

			module_match_dict[module] = count

		sorted_modules = sorted(module_match_dict.items(), key=operator.itemgetter(1))

		if sorted_modules[-1][1] == 0:
			return 'No module found to execute this query'

		exec_module = self.modules_dict[sorted_modules[-1][0]]
		return exec_module.run(query)