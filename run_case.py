import unittest

from api.user_manager import UserManage
from setting import TEST_REPORT_PATH, LOGIN_INFO
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # user = UserManage()
    UserManage().login(LOGIN_INFO.get('username'), LOGIN_INFO.get('password'))
    suite = unittest.TestLoader().discover('./cases', pattern='test*.py')
    with open(TEST_REPORT_PATH, 'wb') as f:
        runner = HTMLTestRunner(f, title='测试报告')
        runner.run(suite)
