import unittest
import json


class TestAdhoc(unittest.TestCase):
    def test_json(self):
        """Tests JSON parsing and dumping
        """
        # JSON string to python object/dict
        pyobj = json.loads('{ "key" : "value" }')
        self.assertTrue(pyobj.get('key') == 'value', 'bad value')
        pass
    
    
def run_all(testCase):
    """Runs all the tests for the specified test case
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    pass

def run():
    run_all(TestAdhoc)
    pass


if __name__ == "__main__":
    run()