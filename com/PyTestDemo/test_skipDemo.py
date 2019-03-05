import pytest
import sys


@pytest.mark.skip(reason="not part of this build")
def test_demo1():
    assert True


def test_demo2():
    assert True

@pytest.mark.skipif(sys.version_info < (3, 6), reason= "not part")
def test_demo3():
    assert True

