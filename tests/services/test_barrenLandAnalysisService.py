from unittest import TestCase


class TestBarrenLandAnalysisService(TestCase):

    def setUp(self):
        pass

    def test_upper(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        assert 'foo'.upper() == 'FOO'
