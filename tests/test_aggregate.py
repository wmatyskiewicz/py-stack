# -*- coding: utf-8 -*-

import unittest

from py_stack.aggregate import Aggregate


class TestStack(unittest.TestCase):

    def setUp(self):
        Aggregate.clear()

    def test_merge_stack_items(self):
        ''' Merge dicts by key '''

        data = [
            {'id': 1, 'first_name': 'John', 'last_name': '', 'city': ''},
            {'id': 2, 'first_name': 'Arthur',
                'last_name': 'Moor', 'city': 'Poznan'},
            {'id': 2, 'first_name': 'Arthur', 'last_name': '', 'city': ''},
            {'id': 1, 'first_name': '', 'last_name': 'Schmit', 'city': ''},
            {'id': 1, 'first_name': '',
                'last_name': '', 'city': 'Los Angeles'},
        ]

        Aggregate.set(data)
        merged_data = Aggregate.merge(key='id')

        valid_data = [
            {'city': 'Los Angeles', 'first_name': 'John',
                'last_name': 'Schmit', 'id': 1},
            {'city': 'Poznan', 'first_name': 'Arthur',
                'id': 2, 'last_name': 'Moor'}
        ]
        self.assertTrue(Aggregate.isEmpty())
        self.assertEqual(tuple(merged_data), tuple(valid_data))

    def test_if_only_dicts_are_supported(self):
        ''' Unsuported data type '''

        data = [1, 2, 3, 4]
        Aggregate.set(data)
        with self.assertRaises(Exception) as context:
            Aggregate.merge(key='id')
        self.assertEqual(
            context.exception.message, 'Required list of dicts')

    def test_different_keys_count(self):
        ''' Different keys count '''

        data = [
            {'id': 1, 'first_name': 'John', 'last_name': ''},
            {'id': 2, 'first_name': 'Arthur',
                'last_name': 'Moor', 'city': 'Poznan'},
            {'id': 2, 'last_name': '', 'city': ''},
            {'id': 1, 'first_name': '', 'last_name': 'Schmit', 'city': ''},
            {'id': 1, 'first_name': '',
                'last_name': '', 'city': 'Los Angeles'},
        ]

        Aggregate.set(data)
        merged_data = Aggregate.merge(key='id')

        valid_data = [
            {'city': 'Los Angeles', 'first_name': 'John',
                'last_name': 'Schmit', 'id': 1},
            {'city': 'Poznan', 'first_name': 'Arthur',
                'id': 2, 'last_name': 'Moor'}
        ]
        self.assertTrue(Aggregate.isEmpty())
        self.assertEqual(tuple(merged_data), tuple(valid_data))

if __name__ == '__main__':
    unittest.main()
