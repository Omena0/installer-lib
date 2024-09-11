
# installer-lib

installer lib real

## Actions:

```html
download_file <url> <location>
create_folder <path>
copy_file <src> <destination>
move_file <src> <destination>
unpack_archive <archive> <destination>

create_shortcut <path> <name> <destination> <icon>

set <var> <value>
copy_var <from> <to>

add <value> <value>
substract <value> <value>
multiply <value> <value>
divide <value> <value>
```

## Control flow:

```html
namespace <name> ()
use <library> [as <name>]

routine <name> ()
call <routine>
jump <line>
return [<amount>=1]

if [not] <condition> <routine>
else <routine>
loop <n-times> <routine>
while <condition> <routine>
break [<amount>=1]
continue [<amount>=1]
```

## Conditions

```html
a == b
a != b
a > b
a < b
a >= b
a <= b
a or b
a and b
a nor b
!a
```
