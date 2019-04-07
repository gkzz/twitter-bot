import unittest

from get_oath_twiter import GetOathOfTwitter
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class TestGetOathOfTwitter(unittest.TestCase):

  def test_get_oath(self):
      test_obj = GetOathOfTwitter(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
      test_client = test_obj.get_oath()

