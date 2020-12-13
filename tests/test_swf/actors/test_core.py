# -*- coding: utf-8 -*-

import unittest

import swf.settings
from swf.models import Domain
from swf.actors import Actor


swf.settings.set(aws_access_key_id="fakeaccesskey", aws_secret_access_key="fakesecret")


class TestActor(unittest.TestCase):
    def setUp(self):
        self.domain = Domain("TestDomain")
        self.actor = Actor(self.domain, "test-task-list")

    def tearDown(self):
        pass

    def test_start_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.actor.start()

    def test_stop_alters_state(self):
        with self.assertRaises(NotImplementedError):
            self.actor.stop()
