from marshmallow import Schema, fields, validate


class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    apellido = fields.String(required=True)
    nombre = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
