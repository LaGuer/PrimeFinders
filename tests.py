import unittest
# import the primefinders package
import primefinders

# import the primefinders module
from primefinders import primefinders

# or an object inside the primefinders module
from primefinders.primefinders import fermat

import tests.all_tests
testSuite = tests.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner().run(testSuite)
