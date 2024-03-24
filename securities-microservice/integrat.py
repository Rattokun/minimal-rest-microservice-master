from main import root


def test_root_get():
    res = root()
    assert res == '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Im1pa2UucGF5bmVAZXhhbXBsZS5jb20iLCJpYXQiOjE3MTA2ODYxOTAsImV4cCI6MTcxMDY4OTc5MH0.O8dsdrzcXIwsuhO_OXi_QCxCiMm-XzVDuOJhGyKzLVY"}'
