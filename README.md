Partdb is a webapp for querying the part to drawer mapping databases for the back-room sorters at Sector67.
We were provided with a virus-infested MS Access DB of the part-number->drawer-number mapping catalog, with a VB6 frontend.
We dumped this Access db into a sqlite3 db using MDBtool, and wrote a Flask app to query it, with a static js/html frontend.

## Populating the DB from the MDB dumps
```bash
$ ./data/insert_csv.sh data/db1.mdb > data.sql # generate a file of INSERTs from the mdb
$ flask initdb # uses schema.sql and data.sql to generate a new db
```

## License
Partdb is licensed under the GPLv3.
