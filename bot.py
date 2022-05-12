import main
import unittest
import random
from unittest import mock
bot_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(bot_move)


class Test(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=bot_move)
    def test_1(self, input):
        main.game()


if __name__ == " __main__":
    unittest.main



