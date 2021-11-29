#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo


class TestPep8(unittest.TestCase):
    def test_upper_echo(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "teSt"], 
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(
            stdout.decode('utf-8'), "TEST")

    def test_lower_echo(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "teSt"], 
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(
            stdout.decode('utf-8'), "test")

    def test_title_echo(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "teSt"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(
            stdout.decode('utf-8'), "Test")

    def test_all_echo(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-tul", "teSt"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(
            stdout.decode('utf-8'), "Test")

    def test_none_echo(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "teSt"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(
            stdout.decode('utf-8'), "teSt")

    def test_help_echo(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout.decode('utf-8'), usage)


if __name__ == '__main__':
    unittest.main()
