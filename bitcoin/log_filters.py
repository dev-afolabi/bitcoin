from logging import Filter
from pprint import pprint

class ManagementFilter(Filter):

    def filter(self, record):
        if (hasattr(record, 'funcname') and record.funcname == 'execute'):
            return False
        else:
            return True