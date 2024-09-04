import pytest
from uuid import uuid4
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository


db_connection_handler.connect()
trip_id = str(uuid4())


@pytest.mark.skip(reason="database iteration")
def test_register_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    email_trips_infos = {
        "id": str(uuid4()),
        "trip_id": trip_id,
        "email": "hello@world.com",
    }

    emails_to_invite_repository.register_email(email_trips_infos)


@pytest.mark.skip(reason="database iteration")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails = emails_to_invite_repository = EmailsToInviteRepository(conn)
    emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)
