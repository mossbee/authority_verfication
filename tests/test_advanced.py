# -*- coding: utf-8 -*-

from .context import authority_verification

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(authority_verification.hmm())


if __name__ == '__main__':
    unittest.main()
