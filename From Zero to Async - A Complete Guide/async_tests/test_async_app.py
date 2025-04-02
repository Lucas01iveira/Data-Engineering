from async_app import fetch_data
import pytest 

# we should have a play button on the function left side (near the line numbers)
@pytest.mark.asyncio
async def test_fetch_data():
    result= await fetch_data()
    assert result == {'data': 123}, "Result didn't match expected"
