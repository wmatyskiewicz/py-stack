# -*- coding: utf-8 -*-

import unittest

from py_stack.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        Stack.clear()

    def test_clear_stack(self):
        data = [1, 2, 3]
        Stack.set(data)
        self.assertFalse(Stack.isEmpty())

        Stack.clear()
        self.assertTrue(Stack.isEmpty())

    def test_add_to_stack(self):
        ''' Add to stack '''
        data = [1, 2, 3]
        Stack.set(data)
        self.assertEqual(data, Stack.get())

    def test_add_to_stack_wrong_type(self):
        ''' Wrong data type input '''
        data = 'Hello World'

        with self.assertRaises(Exception) as context:
            Stack.set(data)
        self.assertEqual(context.exception.message, 'Required list')

    def test_push_to_stack(self):
        ''' Push to stack '''

        self.assertTrue(Stack.isEmpty())

        Stack.push(1)
        self.assertFalse(Stack.isEmpty())

    def test_stack_pop(self):
        ''' Pop from stack '''

        data = [1, 2, 3]
        Stack.set(data)
        item = Stack.pop()
        self.assertEqual(item, 3)
        self.assertEqual(Stack.get(), [1, 2])

    def test_get_first(self):
        ''' Get first item from stack '''

        data = [1, 2, 3]
        Stack.set(data)
        self.assertEqual(Stack.first(), 1)

    def test_get_first_from_empty_stack(self):
        ''' Get first item from empty stack '''

        with self.assertRaises(Exception) as context:
            Stack.first()
        self.assertEqual(context.exception.message, 'Stack is empty')

    def test_get_last(self):
        ''' Get last item from stack '''
        data = [1, 2, 3]
        Stack.set(data)
        self.assertEqual(Stack.last(), 3)

    def test_get_last_from_empty_stack(self):
        ''' Get last item from empty stack '''
        with self.assertRaises(Exception) as context:
            Stack.last()
        self.assertEqual(context.exception.message, 'Stack is empty')

    def test_sort_empty_stos(self):
        ''' Sort stack empty dict key '''
        with self.assertRaises(Exception) as context:
            Stack.sort()
        self.assertEqual(context.exception.message, 'Stack is empty')

    def test_sort_strings(self):
        ''' Sort strings '''

        data = ['Bob', 'John', 'Andrew']
        Stack.set(data)
        Stack.sort()

        self.assertEqual(Stack.get(), ['Andrew', 'Bob', 'John'])

    def test_sort_ints(self):
        ''' Sort stack '''

        data = [4, 2, 1, 3]
        Stack.set(data)

        Stack.sort()
        self.assertEqual(Stack.get(), [1, 2, 3, 4])

    def test_sort_ints_reverse(self):
        ''' Sort stack reverse'''

        data = [4, 2, 1, 3]
        Stack.set(data)

        Stack.sort(reverse=True)
        self.assertEqual(Stack.get(), [4, 3, 2, 1])

    def test_sort_tuples(self):
        ''' Sort tuples '''
        data = [
            ('Bob', 'B', 1),
            ('Andrew', 'A', 2),
            ('John', 'J', 3),
        ]
        valid_order = [
            ('Andrew', 'A', 2),
            ('Bob', 'B', 1),
            ('John', 'J', 3)
        ]

        Stack.set(data)
        Stack.sort(key=1)
        self.assertEqual(
            Stack.get(), valid_order)

    def test_sort_dicts(self):
        ''' Sort dicts '''
        data = [
            {'name': 'Bob', 'id': 3},
            {'name': 'Andrew', 'id': 1},
            {'name': 'John', 'id': 2},
        ]
        valid_order = [
            {'id': 3, 'name': 'Bob'},
            {'id': 2, 'name': 'John'},
            {'id': 1, 'name': 'Andrew'}
        ]

        Stack.set(data)
        Stack.sort(key='id', reverse=True)
        self.assertEqual(Stack.get(), valid_order)

    def test_sort_exceotion_if_items_has_wrong_type(self):
        ''' Sort - all items must be the same type '''

        data = [4, {1}, 1, 3]
        Stack.set(data)

        with self.assertRaises(Exception) as context:
            Stack.sort()
        self.assertEqual(
            context.exception.message, 'All items must be the same type')

if __name__ == '__main__':
    unittest.main()
