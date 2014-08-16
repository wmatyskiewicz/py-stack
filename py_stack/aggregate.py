# -*- coding: utf-8 -*-

import itertools

from py_stack.stack import Stack


class Aggregate(Stack):

    @classmethod
    def _update_item(cls, key, merged_data, stack_item):
        for item in merged_data:
            if item.get(key) != stack_item.get(key):
                continue

            fields_list = itertools.chain(item.keys(), stack_item.keys())
            for field in fields_list:
                try:
                    if not item[field]:
                        item[field] = stack_item[field]
                except KeyError:
                    item[field] = stack_item[field]
            break
        return item

    @classmethod
    def _add_or_update(cls, key, merged_data, stack_item):
        merged_data_key_values = [item.get(key) for item in merged_data]

        if stack_item.get(key) in merged_data_key_values:
            cls._update_item(key, merged_data, stack_item)
        else:
            merged_data.append(stack_item)

        return merged_data

    @classmethod
    def merge(cls, key):
        if not isinstance(cls.first(), dict):
            raise Exception('Required list of dicts')
        merged_data = []

        while cls.stack:
            stack_item = cls.stack.pop()
            merged_data = cls._add_or_update(key, merged_data, stack_item)
        return merged_data
