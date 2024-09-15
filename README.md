# NLW Journey (Python/Flask)

This application was developed during **[Rocketseat](https://www.rocketseat.com.br/)'s NLW Journey** course.    
It aims to help users organize trips for work or leisure. Users can create a journey with a name, start date, and end date. 
Users can plan their activities within each trip by adding things to do for each day.

## Creating Database:
```sql
CREATE TABLE IF NOT EXISTS 'trips' (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER -- 1 = true, 0 = false
);

CREATE TABLE IF NOT EXISTS 'emails_to_invite' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    email TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'links' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    link TEXT NOT NULL,
    title TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'participants' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    emails_to_invite_id TEXT NOT NULL,
    name TEXT NOT NULL,
    is_confirmed INTEGER, -- 1 = true, 0 = false
    FOREIGN KEY (trip_id) REFERENCES trips(id),
    FOREIGN KEY (emails_to_invite_id) REFERENCES emails_to_invite(id)
);

CREATE TABLE IF NOT EXISTS 'activities' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    title TEXT NOT NULL,
    occurs_at DATETIME,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);
```
