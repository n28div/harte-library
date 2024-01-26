"""
Map of the Harte shorthands available, mapped to their correspondent
chord tones/grades.
"""

from collections import OrderedDict

SHORTHAND_DEGREES = {
    "": ["1", "3", "5"],
    "maj": ["1", "3", "5"],
    "min": ["1", "b3", "5"],
    "aug": ["1", "3", "#5"],
    "dim": ["1", "b3", "b5"],
    "7": ["1", "3", "5", "b7"],
    "maj7": ["1", "3", "5", "7"],
    "minmaj7": ["1", "b3", "5", "7"],
    "min7": ["1", "b3", "5", "b7"],
    "augmaj7": ["1", "3", "#5", "7"],
    "aug7": ["1", "3", "#5", "b7"],
    "hdim7": ["1", "b3", "b5", "b7"],
    "hdim": ["1", "b3", "b5", "b7"],
    "dim7": ["1", "b3", "b5", "bb7"],
    "dom7dim5": ["1", "3", "b5", "b7"],
    "maj6": ["1", "3", "5", "6"],
    "min6": ["1", "b3", "5", "6"],
    "maj9": ["1", "3", "5", "7", "9"],
    "9": ["1", "3", "5", "b7", "9"],
    "minmaj9": ["1", "b3", "5", "7", "9"],
    "min9": ["1", "b3", "5", "b7", "9"],
    "augmaj9": ["1", "3", "#5", "7", "9"],
    "aug9": ["1", "3", "#5", "b7", "9"],
    "hdim9": ["1", "b3", "b5", "b7", "9"],
    "hdimmin9": ["1", "b3", "b5", "b7", "b9"],
    "dim9": ["1", "b3", "b5", "bb7", "9"],
    "dimmin9": ["1", "b3", "b5", "bb7", "b9"],
    "11": ["1", "3", "5", "b7", "9", "11"],
    "maj11": ["1", "3", "5", "7", "9", "11"],
    "minmaj11": ["1", "b3", "5", "7", "9", "11"],
    "min11": ["1", "b3", "5", "b7", "9", "11"],
    "augmaj11": ["1", "3", "#5", "7", "9", "11"],
    "aug11": ["1", "3", "#5", "b7", "9", "11"],
    "hdim11": ["1", "b3", "b5", "b7", "b9", "11"],
    "dim11": ["1", "b3", "b5", "bb7", "b9", "b11"],
    "maj13": ["1", "3", "5", "7", "9", "11", "13"],
    "13": ["1", "3", "5", "b7", "9", "11", "13"],
    "minmaj13": ["1", "b3", "5", "7", "9", "11", "13"],
    "min13": ["1", "b3", "5", "b7", "9", "11", "13"],
    "augmaj13": ["1", "3", "#5", "7", "9", "11", "13"],
    "hdim13": ["1", "b3", "b5", "b7", "9", "11", "13"],
    "sus2": ["1", "2", "5"],
    "sus4": ["1", "4", "5"],
    "7sus4": ["1", "4", "5", "b7"],
    "power": ["1", "5"],
    "pedal": ["1"],
    "1": ["1"],
    "5": ["1", "5"],
    "6": ["1", "3", "5", "6"],
}

SHORTHAND_DEGREE_MAP = {
    'maj': ('3', '5'),
    'min': ('b3', '5'),
    'aug': ('3', '#5'),
    'dim': ('b3', 'b5'),
    'maj7': ('3', '5', '7'),
    'min7': ('b3', '5', 'b7'),
    '7': ('3', '5', 'b7'),
    'minmaj7': ('b3', '5', '7'),
    'dim7': ('b3', 'b5', 'bb7'),
    'hdim7': ('b3', 'b5', 'b7'),
    'maj6': ('3', '5', '6'),
    'min6': ('b3', '5', '6'),
    '9': ('3', '5', 'b7', '9'),
    'maj9': ('3', '5', '7', '9'),
    'min9': ('b3', '5', 'b7', '9'),
    'sus4': ('4', '5'),
}

TRIAD_SHORTHANDS = ['maj', 'min', 'aug', 'dim']

DEGREE_SHORTHAND_MAP = OrderedDict({
    ('3', '5', 'b7', '9'): '9',
    ('3', '5', '7', '9'): 'maj9',
    ('b3', '5', 'b7', '9'): 'min9',
    ('3', '5', 'b7'): '7',
    ('3', '5', '6'): 'maj6',
    ('b3', '5', '6'): 'min6',
    ('3', '5', '7'): 'maj7',
    ('b3', 'b5', 'bb7'): 'dim7',
    ('b3', '5', 'b7'): 'min7',
    ('b3', 'b5', 'b7'): 'hdim7',
    ('b3', '5', '7'): 'minmaj7',
    ('3', '5'): 'maj',
    ('b3', '5'): 'min',
    ('b3', 'b5'): 'dim',
    ('3', '#5'): 'aug',
    ('4', '5'): 'sus4',
})
