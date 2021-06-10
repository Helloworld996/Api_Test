import unittest
from api.user_manager import UserManage
from datas.user_manager_data import UserManagerData


class TestUserManagerCase(unittest.TestCase):
    user_id = None

    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManage()
        # cls.user.login('admin123', 'admin123')

        um = UserManagerData()
        cls.username = um.user_case_data.get('username')
        cls.password = um.user_case_data.get('password')
        cls.new_username = um.user_case_data.get('new_username')
        cls.new_password = um.user_case_data.get('new_password')

    # case1: 只输入用户名和密码进行添加
    def test01_normal_add(self):
        # 定义测试用例数据
        # username = 'test038'
        # password = 'test038'
        # 1)请求添加管理员接口
        actual_result = self.user.add_user(self.username, self.password)
        print(actual_result)
        data = actual_result.get('data')
        if data:
            TestUserManagerCase.user_id = data.get('id')

        # 2)对返回结果数据校验
        self.assertEqual(actual_result['errno'], 0)
        self.assertEqual(data.get('username'), self.username)

    # case2:编辑用户
    def test02_edit(self):
        # 1）定义测试数据
        # 2）调用编辑接口
        # new_password = new_username = 'abcdefgh'
        actual_result = self.user.edit_user(TestUserManagerCase.user_id, self.new_username, password=self.new_password)
        # 3)断言
        self.assertEqual(actual_result['errno'], 0)
        self.assertEqual(actual_result.get('data').get('username'), self.new_username)

    # 查询用户
    def test03_search(self):
        actual_result = self.user.search_user()
        self.assertEqual(actual_result['errno'], 0)
        self.assertEqual(actual_result.get('data').get('list')[0].get('username'), self.new_username)

    # case4:删除用户
    def test04_delete(self):
        # 1）定义测试用例中的数据
        # 2）调用被测接口
        actual_result = self.user.del_user(TestUserManagerCase.user_id)
        # 3）断言
        self.assertEqual(actual_result['errno'], 0)


if __name__ == '__main__':
    unittest.main()

# 运行时请将光标放置代码外。否则仅运行一条测试用例。可能是pycharm的bug
