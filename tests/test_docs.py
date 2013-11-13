import doctest

def test_docs():
    failure_count, test_count \
        = doctest.testfile('../README.md', optionflags=doctest.ELLIPSIS)
    assert failure_count == 0
