# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.CronIdRule import CronIdRule
from tests import RunFromText


GOOD_CMD_STATE = '''
run_postinstall:
  cron.present:
    - name: echo hello
    - identifier: yes

run_postinstall2:
  cron.present:
  - name: echo hello
  - identifier: yes2

'''

BAD_CMD_STATE = '''
run_postinstall:
  cron.present:
    - name: echo hello

run_postinstall2:
  cron.present:
  - name: echo hello

'''

class TestCmdWaitRecommendRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(CronIdRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_CMD_STATE)
        import pprint
        pprint.pprint(results)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_CMD_STATE)
        # import pprint
        # pprint.pprint(results)
        self.assertEqual(2, len(results))
