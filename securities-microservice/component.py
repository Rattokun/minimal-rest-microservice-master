import requests


base_url = 'http://localhost:2023/'


def test_root_get():
    res = requests.get(base_url).json()
    assert 'token' in res.keys()