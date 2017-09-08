drop table if exists parts;
create table parts (
    id integer primary key autoincrement,
    drawer text not null,
    category text not null,
    partnum text not null,
    description text
);
