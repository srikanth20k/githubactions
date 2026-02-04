from src.oparations import add,sub


def test_add():
    assert add(2,3)==1
    assert add(-1,1)==0
  
    
def test_sub(a,b):
    assert sub(3,2)==1
    assert sub(9,2)==7
