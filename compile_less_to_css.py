#!/usr/bin/env python
# compiles the less style sheet to custom CSS
import lesscpy
from pathlib import Path

style = Path.cwd() / 'content' / 'extra' / 'style.less'
output = Path.cwd() / 'content' / 'extra' / 'custom.css'

with open(output, 'w') as custom:
    custom.write(lesscpy.compile(str(style)))

print('Compliled Succesfully')
