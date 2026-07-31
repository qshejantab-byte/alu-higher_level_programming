# SQL_more_queries

Higher-level programming project on MySQL users, privileges,
constraints, foreign keys, and multi-table queries (subqueries and
joins).

## Tasks

| File | Description |
| --- | --- |
| `0-privileges.sql` | List privileges of two users |
| `1-create_user.sql` | Create a user with all privileges |
| `2-create_read_user.sql` | Create a database and a SELECT-only user |
| `3-force_name.sql` | Table with a `NOT NULL` name column |
| `4-never_empty.sql` | Table with a defaulted id column |
| `5-unique_id.sql` | Table with a unique, defaulted id column |
| `6-states.sql` | `states` table with an auto-increment primary key |
| `7-cities.sql` | `cities` table with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California, via subquery |
| `9-cities_by_state_join.sql` | Cities with their state, via `JOIN` |
| `10-genre_id_by_show.sql` | Shows that have at least one genre |
| `11-genre_id_all_shows.sql` | All shows, `NULL` if no genre |
| `12-no_genre.sql` | Shows with no genre linked |
| `13-count_shows_by_genre.sql` | Show count per genre |
| `14-my_genres.sql` | All genres of the show Dexter |
| `15-comedy_only.sql` | All shows in the Comedy genre |
| `16-shows_by_genre.sql` | All shows with their genre names |

## Requirements

- MySQL 8.0 on Ubuntu 20.04 LTS
- Every query has a comment directly above it
- Every file starts with a comment describing the task
- All SQL keywords are uppercase

Every script in this project was run against a real local MySQL 8.0
server. Tasks 10-16 depend on the `hbtn_0d_tvshows` dump referenced
in the project instructions; a dataset matching that dump's exact
published example rows was reconstructed locally to verify these
scripts before submission.
