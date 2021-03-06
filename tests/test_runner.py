import unittest
from metrunner.runner import Runner
from metrunner.parser import input_parser


class TestRunner(unittest.TestCase):

    def setUp(self):
        self.input_file = "./inputs/input_2.json"
        self.exps = input_parser(self.input_file)
        self.runner = Runner(self.exps)

    def test_runner_exps(self):
        self.assertEqual(len(self.exps), len(self.runner.experiments))
    @unittest.skip("Travis.yml")
    def test_runner_run_all(self):
        self.assertTrue(self.runner.run_all())
