import pytest
from script import main


def test_main():
	a = 2
	assert a+1 == main(a)

