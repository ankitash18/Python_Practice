from  src.resurces.CheckOut import CheckOut
import pytest

@pytest.fixture()
def checkout():
    checkout = CheckOut()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

#def test_canadditemprice(checkout):
 #   checkout.addItemPrice("a",1)

#def test_canadditem(checkout):
 #   checkout.additem("a")

def test_cancalcultetotal(checkout):
    checkout.additem("a")
    assert checkout.calculatetotal() ==1

def test_GetCorrecttotalwithmultipleitems(checkout):
    checkout.additem("a")
    checkout.additem("b")
    assert checkout.calculatetotal() == 3

def test_canadddiscountrules(checkout):
    checkout.addDiscount("a",3,2)

@pytest.mark.skip
def test_canapplydiscoutrule(checkout):
    checkout.addDiscount("a",3,2)
    checkout.additem("a")
    checkout.additem("a")
    checkout.additem("a")
    assert checkout.calculatetotal() ==2