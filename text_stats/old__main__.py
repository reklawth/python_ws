# text_stats/__main__.py

import sys

segments = sys.argv[1:]

full_text = ' '.join(segments)

output = '# words: {}, # chars: {}'.format(
    len(full_text.split()),
    sum(len(w) for w in full_text.split())
)

print(output)