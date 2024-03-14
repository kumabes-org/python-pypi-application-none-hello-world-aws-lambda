from unittest import TestCase
from src.say_hello import SayHello

class TestSayHello(TestCase):
    def test_say_english(self):
        name = 'Kumabe'
        self.assertEqual(f'Hello world, {name}!', SayHello().say_english(name))