# SQL_introduction

Higher-level programming project introducing SQL and MySQL 8.0.

## Tasks

| File | Description |
| --- | --- |
| `0-list_databases.sql` | List all databases |
| `1-create_database_if_missing.sql` | Create `hbtn_0c_0` without failing if it exists |
| `2-remove_database.sql` | Delete `hbtn_0c_0` without failing if it's missing |
| `3-list_tables.sql` | List all tables of a database |
| `4-first_table.sql` | Create `first_table` (id, name) |
| `5-full_table.sql` | Print the full description of `first_table` |
| `6-list_values.sql` | List all rows of `first_table` |
| `7-insert_value.sql` | Insert a row into `first_table` |
| `8-count_89.sql` | Count records with id = 89 |
| `9-full_creation.sql` | Create `second_table` and insert sample rows |
| `10-top_score.sql` | List records ordered by score, descending |
| `11-best_score.sql` | List records with score >= 10 |
| `12-no_cheating.sql` | Update a score by name only |
| `13-change_class.sql` | Delete records with score <= 5 |
| `14-average.sql` | Compute the average score |
| `15-groups.sql` | Count records grouped by score |
| `16-no_link.sql` | List records that have a name, by descending score |

## Requirements

- MySQL 8.0 on Ubuntu 20.04 LTS
- Every query has a comment directly above it
- Every file starts with a comment describing the task
- All SQL keywords are uppercase

Every script in this project was run against a real local MySQL 8.0
server and its output verified to match the expected results before
being committed.
