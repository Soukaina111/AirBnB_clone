#!/usr/bin/python3

"""
raise the errors in file storage if the model or the instance aren't found"""


class ModelNotFoundError(Exception):
    """Raised when an unknown module is passed"""
    def __init__(self, global_entity="BaseModel"):
        super().__init__(f"Model with name {global_entity} is not found, try later!")


class InstanceNotFoundError(Exception):
    """in case an unknown instance's id is passed"""

    def __init__(self, obj_id="", global_entity="BaseModel"):
        super().__init__(
                f"Object Instance belonging to {global_entity} with id {obj_id} does not exist!")
