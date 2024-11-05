"""
Task Schema Module

Defines the Marshmallow schemas for task serialization/deserialization.
Includes validation rules and field specifications.
Used for converting between Python objects and API JSON data.
"""

from ..extensions import ma, db
from ..models.task import Task
from marshmallow import validate, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    # Add field validation
    description = ma.String(
        required=True,
        validate=validate.Length(min=1, max=500)
    )

    @validates('description')
    def validate_description(self, value):
        if value.strip() == "":
            raise ValidationError('Description cannot be empty')

# Initialize schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)