import mock
import unittest

from bme280pi.raspberry_pi_version import (detect_raspberry_pi_version,
                                           get_list_of_revisions)


def raise_exception(*args, **kwargs):
    raise FileNotFoundError


class test_detect_raspberry_pi_version(unittest.TestCase):
    def test(self):
        known_revisions = get_list_of_revisions()

        for revision in known_revisions:
            m = mock.mock_open(read_data="\nRevision:" + revision + "\n")
            with mock.patch('builtins.open', m):
                self.assertEqual(detect_raspberry_pi_version(),
                                 known_revisions[revision])

        m = raise_exception
        with mock.patch('builtins.open', m):
            with self.assertWarns(Warning):
                self.assertEqual(detect_raspberry_pi_version(), "Unknown")