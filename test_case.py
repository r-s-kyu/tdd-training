import pytest 
from app import integer_closed_interval


class Test整数閉区間を示すクラスをつくる:
    def test_下端点lower_上端点upperをもつ(self):
        assert integer_closed_interval(3,8).lower == 3
        assert integer_closed_interval(3,8).upper == 8

    def test_文字列表現を返す(self):
        assert integer_closed_interval(3,8).return_string() == "[3,8]"

class Test基準となる整数閉空間の上端点より下端点が大きい場合:
    # @pytest.raises(Exception)                                                                                                                                   
    def test_stdの上端点より下端点が大きい場合は0を返す(self):
        with pytest.raises(Exception):
            integer_closed_interval(8,3)


class Test基準となる整数閉空間の上端点が下端点以上の場合:
    class Test受け取った整数閉空間が基準となる整数閉空間が確認する:
        params = {
            (
                "完全に一致する場合",
                (4,6),(4,6),2
            ),
            (
                "完全に含まれる場合",
                 (1,8),(4,6),3
            ),
            (
                "完全に一致しない場合",
                 (4,6),(5,7),1
            )
        }    
        @pytest.mark.parametrize("msg,std_range,inp_range,exp",params)
        def test_Test受け取った整数閉空間が基準となる整数閉空間が等価か確認する(self,msg,std_range,inp_range,exp):
            assert integer_closed_interval(std_range[0],std_range[1]).compare_with_closed_interval(inp_range) == exp, msg


