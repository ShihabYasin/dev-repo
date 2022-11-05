import pytest


@pytest.mark.markername
@pytest.mark.parametrize("num, output", [(2,3),(3,4)]) # passing params if need 
def test_parametrize(num, output):    
    assert output == num+1
        
@pytest.mark.xfail # ignoring test 
def test_your_user():    
    assert True == False
    
@pytest.mark.skip  # skipping test
def test_your_user(fixture_1):    
    print(f"Fixture Value {fixture_1}")
    assert fixture_1 == 11

@pytest.mark.secret  # pytest -m secret => only runs those test with secret marker
def test_your_user(fixture_1):    
    print(f"Fixture Value {fixture_1}")
    assert fixture_1 == 10