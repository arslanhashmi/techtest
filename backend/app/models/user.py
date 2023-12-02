import bcrypt
from app import db
from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemySchema
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, text


class User(db.Model):
    __tablename__ = "users"

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
    is_active = Column(Boolean, nullable=False, default=False)

    email = Column(String(64), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))

    # Must contain hashed password
    password = Column(String(255))

    personalization_settings = relationship(
        "PersonalizationSettings", back_populates="user"
    )

    # Computed Fields
    @hybrid_property
    def full_name(self):
        full_name = ""

        if self.first_name is not None:
            full_name += self.first_name

        if self.last_name is not None:
            if full_name:
                full_name += " " + self.last_name
            else:
                full_name += self.last_name

        return full_name

    @full_name.expression
    def full_name(self):
        return func.concat(self.first_name, " ", self.last_name).label("full_name")

    def set_password(self, password: str, rounds: int = 12) -> None:
        """
        Generate hash and set the password.
        """
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds))

    def verify_password(self, password: str) -> bool:
        """
        Verify password.
        """
        return self.password == bcrypt.hashpw(password, self.password)


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = fields.Integer()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

    # Required Fields
    email = fields.Email(
        required=True,
        validate=validate.And(
            validate.Regexp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
            validate.Length(min=1, max=64),
        ),
    )

    # Optional Fields
    is_active = fields.Boolean()
    first_name = fields.String(validate=validate.Length(min=1, max=32))
    last_name = fields.String(validate=validate.Length(min=1, max=32))

    personalization_settings = fields.List(
        fields.Nested("PersonalizationSettingsSchema", exclude=("user",))
    )
