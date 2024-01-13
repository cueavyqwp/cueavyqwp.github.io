import pycmarkgfm
import os

os.chdir( os.path.dirname( __file__ ) )

s = pycmarkgfm.gfm_to_html(
"""
# about

> todo

```python
input()
```

|1|2|
|:---:|:---:|
|1|2|
""")

print(s)
