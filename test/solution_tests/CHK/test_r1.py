from solutions.CHK import checkout_solution

class TestCheckout():
    def test_invalid(self):
        assert checkout([]) == -1
        assert checkout(9) == -1

    def test_empty(self):
        assert checkout("") == 0

    def test_non_sale(self):
        assert checkout("ddd") == 45
        assert checkout("cd") == 35

    def test_sale(self):
        assert checkout("aaa") == 130