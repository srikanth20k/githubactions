from src.oparations import add,sub


def test_add(a,b):
    a = 1
    b = 2
    assert add(a,b) == 3
    a = 0
    b = 1
    assert add(a+b) == 1
    
def test_sub(a,b):
    a = 1
    b = 2
    assert sub(a,b) ==- 1
    a = 3
    b = 1
    assert sub(a,b) == 2
