from marshmallow import Schema, fields

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)