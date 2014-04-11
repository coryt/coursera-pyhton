import rpsls
import unittest

class TestFunctions(unittest.TestCase):

    def test_number_to_name(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(rpsls.number_to_name(0), 'rock')
        self.assertEqual(rpsls.number_to_name(1), 'Spock')
        self.assertEqual(rpsls.number_to_name(2), 'paper')
        self.assertEqual(rpsls.number_to_name(3), 'lizard')
        self.assertEqual(rpsls.number_to_name(4), 'scissors')

    def test_name_to_number(self):
        self.assertEqual(rpsls.name_to_number("rock"), 0)
        self.assertEqual(rpsls.name_to_number("Spock"), 1)
        self.assertEqual(rpsls.name_to_number("paper"), 2)
        self.assertEqual(rpsls.name_to_number("lizard"), 3)
        self.assertEqual(rpsls.name_to_number("scissors"), 4)

if __name__ == '__main__':
    unittest.main()
