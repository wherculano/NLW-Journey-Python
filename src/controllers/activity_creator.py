from uuid import uuid4
from typing import Dict


class ActivityCreator:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def create(self, body, trip_id) -> Dict:
        try:
            _id = str(uuid4())
            activities_infos = {
                "id": _id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }
            self.__activities_repository.register_activity(activities_infos)
            return {"body": {"activity_id": _id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
