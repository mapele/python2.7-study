import pdb
import logging
logging.basicConfig(level=logging.INFO)

s = '2'
n = int(s)
pdb.set_trace()
logging.info('n=%d' %n)
print 10 / n