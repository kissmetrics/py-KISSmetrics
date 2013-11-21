# -*- coding: utf-8 -*-

import doctest
import unittest


# We avoid using doctest.DocFileSuite so the tests are runnable by both py.test
# and unittest.
class DocTestCase(unittest.TestCase):
    def test_readme(self):
        failure_count, test_count \
            = doctest.testfile('../../README.md', optionflags=doctest.ELLIPSIS)
        assert failure_count == 0

    def test_long_description(self):
        failure_count, test_count \
            = doctest.testfile('../../DESCRIPTION.rst', optionflags=doctest.ELLIPSIS)
        assert failure_count == 0


if __name__ == '__main__':
    unittest.main()
