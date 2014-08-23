# -*- coding: utf-8 -*-

import datetime
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
        valid_data = [
            {'city': 'Los Angeles', 'first_name': 'John',
                'last_name': 'Schmit', 'id': 1},
            {'city': 'Poznan', 'first_name': 'Arthur',
                'id': 2, 'last_name': 'Moor'}
        ]

        Aggregate.set(data)
        merged_data = Aggregate.merge(key='id')
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
        valid_data = [
            {'city': 'Los Angeles', 'first_name': 'John',
                'last_name': 'Schmit', 'id': 1},
            {'city': 'Poznan', 'first_name': 'Arthur',
                'id': 2, 'last_name': 'Moor'}
        ]

        Aggregate.set(data)
        merged_data = Aggregate.merge(key='id')
        self.assertTrue(Aggregate.isEmpty())
        self.assertEqual(tuple(merged_data), tuple(valid_data))

    def test_update_lists_dicts_field(self):
        ''' Check if dicts, and lists are update '''

        data = [
            {'id': 1, 'name': '', 'values': [1, 2]},
            {'id': 1, 'name': 'Numbers', 'values': [1, 3, 4]},
            {'id': 2, 'name': 'Words', 'values': {'a': 1, 'c': 3}},
            {'id': 2, 'name': 'Words', 'values': {'a': 2, 'b': 2}},
        ]
        valid_data = [
            {'id': 1, 'name': 'Numbers', 'values': [1, 2, 3, 4]},
            {'id': 2, 'name': 'Words', 'values': {'a': 2, 'b': 2, 'c': 3}},
        ]

        Aggregate.set(data)
        merged_data = Aggregate.merge(key='id')
        for index in xrange(2):
            self.assertEqual(
                merged_data[index].get('values'),
                valid_data[index].get('values')
            )

    def test_simple_replace(self):
        data = [
            {'id': 1, 'values': 2},
            {'id': 1, 'values': 3},
            {'id': 1, 'values': 1},
            {'id': 3, 'values': 3},
            {'id': 2, 'values': 2},
        ]
        valid_data = [
            {'id': 1, 'values': 3},
            {'id': 2, 'values': 2},
            {'id': 3, 'values': 3},
        ]

        Aggregate.set(data)
        Aggregate.sort(key='values')
        merged_data = Aggregate.merge(key='id', replace_field='values')
        self.assertEqual(merged_data, valid_data)

    def test_merge_with_update_data(self):
        data = [
            {
                'id': 1,
                'date': datetime.datetime(2000, 01, 02),
                'values': {'a': 1, 'c': 3}
            },
            {
                'id': 1,
                'date': datetime.datetime(2000, 01, 03),
                'values': {'a': 1, 'b': 2}
            },
            {
                'id': 1,
                'date': datetime.datetime(2000, 01, 01),
                'values': {'a': 1, 'b': 2}
            },
            {
                'id': 1,
                'date': datetime.datetime(2000, 01, 02),
                'values': {'a': 1, 'b': 2}
            },
        ]
        valid_data = [
            {
                'id': 1,
                'date': datetime.datetime(2000, 01, 03),
                'values': {'a': 1, 'b': 2, 'c': 3}
            }
        ]

        Aggregate.set(data)
        Aggregate.sort(key='date')
        merged_data = Aggregate.merge(key='id', replace_field='date')
        self.assertEqual(merged_data, valid_data)

if __name__ == '__main__':
    unittest.main()
