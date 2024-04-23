from solutions.CHK.checkout_solution import checkout

class TestCheckout():
    def test_invalid(self):
        assert checkout([]) == -1
        assert checkout(9) == -1

    def test_empty(self):
        assert checkout("") == 0

    def test_non_sale(self):
        assert checkout("DDD") == 45
        assert checkout("CD") == 35

    def test_sale(self):
        assert checkout("AAA") == 130

    def test_sale_under_offer(self):
        assert checkout("AA") == 100

    def test_symbol(self):
        assert checkout("-AB") == -1

    def test_lower(self):
        assert checkout("a") == -1
        assert checkout("abcd") == -1
        assert checkout("ABCd") == -1

    def test_buy_get_free(self):
        assert checkout("EEB") == 80
        assert checkout("EEEB") == 120
        assert checkout("EEEEBB") == 160