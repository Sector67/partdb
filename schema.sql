drop table if exists parts;
create table parts (
    id integer primary key autoincrement,
    drawer id not null,
    partnum text not null,
    description text
);
