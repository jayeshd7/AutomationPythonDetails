import pytest
import sys




print("KID", len("030E064B-134F-414E-B0FE-FD18001FE639"))


print("AID", len("5F811244-EC79-46FF-88DC-14513CFDF760"))


print("")
@pytest.mark.skip(reason="not part of this build")
def test_demo1():
    assert True


def test_demo2():
    assert True

@pytest.mark.skipif(sys.version_info < (3, 6), reason= "not part")
def test_demo3():
    assert True

