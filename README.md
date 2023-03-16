# installer-lib

 Make installers easy

## How to use

Heres a quick example:

```python3
from installer-lib import *

installer = installer('Example', '1.0',('127.0.0.1',5000),False) # args: appName, appVer, fileServer (tuple of server ip, port), gui (Enable gui or not)
installer.gui()     # Use this is you want to use the gui from installer-lib, only downloads files...
installer.install() # And use this if you just want to immidiately download files, and run our own script after its done.
```

I will add more utils soon, suggest in the github issues!
