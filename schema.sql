drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  'search' text not null
);
