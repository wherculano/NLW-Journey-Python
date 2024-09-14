from typing import Dict
from uuid import uuid4


class LinkCreator:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid4())
            link_infos = {
                "link": body["url"],
                "title": body["title"],
                "id": link_id,
                "trip_id": trip_id,
            }
            self.__link_repository.register_link(link_infos)
            return {"body": {"link_id": link_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request"},
                "message": str(exception),
                "status_code": 400,
            }
