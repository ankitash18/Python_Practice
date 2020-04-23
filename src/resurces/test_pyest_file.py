from pytest import approx, raises


class TestClass:
    def test_me(self):
        with raises(ValueError):
            raise ValueError

    def test_me2(self):
        assert True

    def test_float(self):
        assert (0.1+0.2) == approx(0.3)

class MyTestClass:
    def test_it(self):
        assert True

    def test_it2(self):
        assert  True