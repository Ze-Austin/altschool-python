from apiflask.schemas import Schema
from apiflask import fields

"""
    class Task:
        id int
        content str
        date_added datetime
        is_complete Boolean
"""

class TaskOutputSchema(Schema):
    id = fields.Integer()
    content = fields.String()
    date_added = fields.DateTime()
    is_completed = fields.Boolean()

class TaskCreationSchema(Schema):
    content = fields.String(required=True)

class TaskUpdateSchema(Schema):
    content = fields.String(required=True)
    is_completed = fields.Boolean(required=True)
