from app import db
from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemySchema
from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text


class PersonalizationSettingsType:
    LINKEDIN_BIO = "LINKEDIN_BIO"
    TOTAL_EXPERIENCE = "TOTAL_EXPERIENCE"
    CURRENT_EXPERIENCE = "CURRENT_EXPERIENCE"
    LIST_OF_PAST_JOBS = "LIST_OF_PAST_JOBS"
    CURRENT_JOB_DESCRIPTION = "CURRENT_JOB_DESCRIPTION"
    CURRENT_JOB_SPECIALTIES = "CURRENT_JOB_SPECIALTIES"

    CHOICES = [
        LINKEDIN_BIO,
        TOTAL_EXPERIENCE,
        CURRENT_EXPERIENCE,
        LIST_OF_PAST_JOBS,
        CURRENT_JOB_DESCRIPTION,
        CURRENT_JOB_SPECIALTIES,
    ]


class PersonalizationSettings(db.Model):
    __tablename__ = "personalization_settings"

    id = Column(Integer, primary_key=True)
    created_date = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    modified_date = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
    )

    user_id = Column(Integer, ForeignKey("users.id"))

    is_disabled = Column(Boolean, nullable=False, default=False)

    name = Column(
        Enum(*PersonalizationSettingsType.CHOICES, name="settings_type"), nullable=False
    )
    description = Column(String(255), nullable=False)
    value = Column(Boolean, nullable=False, default=False)

    user = relationship(
        "User", foreign_keys=[user_id], back_populates="personalization_settings"
    )


class PersonalizationSettingsSchema(SQLAlchemySchema):
    class Meta:
        model = PersonalizationSettings
        load_instance = True

    id = fields.Integer()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

    # Required Fields
    name = fields.String(validate=validate.OneOf(PersonalizationSettingsType.CHOICES))
    description = fields.String(validate=validate.Length(min=1, max=256))
    value = fields.Boolean()
    is_disabled = fields.Boolean()

    # Optional Fields
    user = fields.Nested("UserSchema", exclude=("personalization_settings",))
