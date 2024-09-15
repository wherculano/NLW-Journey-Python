# NLW Journey (Python/Flask)

This application was developed during **[Rocketseat](https://www.rocketseat.com.br/)'s NLW Journey** course.    
It aims to help users organize trips for work or leisure. Users can create a journey with a name, start date, and end date. 
Users can plan their activities within each trip by adding things to do for each day.    

## Functional Requirements:    
1. The user registers a trip by providing the destination, start date, end date, guest emails, as well as their full name and email address.
1. The trip creator receives an email to confirm the new trip through a link. By clicking the link, the trip is confirmed, guests receive confirmation emails, and the creator is redirected to the trip page.
1. Guests, upon clicking the confirmation link, are redirected to the application where they must enter their name (with the email already filled in) to confirm their participation in the trip.
1. On the event page, trip participants can add important links related to the trip, such as Airbnb reservations, places to visit, etc.
1. On the event page, both the creator and guests can add activities that will take place during the trip, including the title, date, and time.
1. New participants can be invited from the event page via email and must go through the confirmation process like any other guest.

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
