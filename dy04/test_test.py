import allure


@allure.feature('订单模块')
class Test_order:
    @allure.story('下订单')
    def test_order_app(self):
        #假装发了请求

        assert '成功' in '操作成功'

    @allure.story('发货')
    def test_order_wh(self):


        assert '成功'  in '操作成功'





