import unittest
from reports.BSTestRunner import BSTestRunner
import time,logging

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
resport_name = report_dir+'/'+now+'test_report.html'

with open(resport_name,'wb') as f:
    runner = BSTestRunner(stream=f,title='kyb Test report',description='测试用例')
    logging.info('start run test case...')
    runner.run(discover)