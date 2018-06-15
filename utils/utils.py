import re


def input_set_to_actual_set(input_set):
    if len(input_set) == 0:
        return []
    return [re.sub('[{}"]', '', section).strip() for section in input_set.split(',')]
