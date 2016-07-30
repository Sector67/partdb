Partdb is a webapp for querying the part to drawer mapping databases for the back-room sorters at Sector67.
We were provided with a virus-infested MS Access DB of the part-number->drawer-number mapping catalog, with a VB6 frontend.
We dumped this Access db into a sqlite3 db using MDBtool, and wrote a Flask app to query it, with a static js/html frontend.

## License
Partdb is licensed under the GPLv3.
