#!/bin/bash

BASEDIR=$(dirname "$0")

tables="$(mdb-tables $1)"

for table in $tables; do
	echo "select Drawer, TableName, PARTNUM, Description from $table" | mdb-sql -HFp $1 \
		| awk 'NF' - \
		| python "$BASEDIR/tsv_to_insert.py"
done;
