from pathlib import Path

import more_itertools as mitertools
from lark import Lark, Transformer

with open(Path.cwd() / 'grammar' / "harte.lark", 'r') as g:
    HARTE_LARK_GRAMMAR = g.read()


class TreeToHarteTransformer(Transformer):
    """
    Lark transformer to turn a parse tree into a Harte chord representation.
    The representation consists of a dict with keys:
      * root
          Root note of the chord
      * shorthand - OPTIONAL
          Shorthand of the chord
      * bass - OPTIONAL
          Modified bass note if slash chord is used
      * degrees - OPTIONAL
          Modified degrees on the chord (with missing degrees identified with *
           i.e. *3
    """
    NATURAL = str
    MODIFIER = str
    MISSING = str
    SHORTHAND = lambda self, sh: {"shorthand": str(sh)}
    INTERVAL = str
    degree = lambda self, elems: "".join(elems)
    bass = lambda self, elems: {"bass": "".join(elems)}
    note = lambda self, elems: {"root": "".join(elems)}
    degree_list = lambda self, elems: elems

    def chord(self, elems):
        d = dict()
        for elem in elems:
            if isinstance(elem, dict):
                d.update(**elem)
            elif isinstance(elem, list):
                d.update({"degrees": list(mitertools.collapse(elem))})

        return d


PARSER = Lark(HARTE_LARK_GRAMMAR,
              parser='lalr',
              start="chord",
              propagate_positions=False,
              maybe_placeholders=False,
              transformer=TreeToHarteTransformer())

if __name__ == '__main__':
    # test the grammar parsed Tree
    print(PARSER.parse('C:maj7(4,b6)/b4'))
