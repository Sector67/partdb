import sys

for l in sys.stdin:
    v = ['"' + x.strip().replace('"', '""') + '"' for x in l.split("\t")]
    print(f'INSERT INTO `parts` (`drawer`, `category`, `partnum`, `description`) VALUES ({", ".join(v)});')
