# -*- coding: utf-8 -*-

##### Import os module to enable python to read directory.
#### Use exception handling in case user has not got os module installed in the machine.
try:
    import os
except ImportError:
    os.system("pip install os")
    import os

### Pops up command prompt.
os.system("start cmd")

#### type 'python "Weather script.py"' in the command prompt to test that the script works.


