from src.money import Money

def test_multiplication():
    five = Money(5, "USD")
    product = five.times(2)
    assert product.amount == 10
    assert product.currency == "USD"
