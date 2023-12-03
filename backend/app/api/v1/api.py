from app import db
from app.models.personalization import (
    PersonalizationSettings,
    PersonalizationSettingsSchema,
)
from app.models.user import User, UserSchema
from flask import request
from flask_restful import Resource


class PersonalizationSettingsResource(Resource):
    schema = UserSchema(
        exclude=(
            "created_date",
            "modified_date",
            "personalization_settings.created_date",
            "personalization_settings.modified_date",
        )
    )

    def get(self, user_id):
        user = db.session.query(User).filter_by(id=user_id).one_or_none()
        user = db.get_or_404(User, user_id)
        response = self.schema.dump(user)
        return response

    def post(self, user_id):
        user = db.get_or_404(User, user_id)
        settings_schema = PersonalizationSettingsSchema(
            only=("id", "description", "value", "is_disabled")
        )
        settings_schema.load(data=request.get_json(), partial=True, session=db.session)
        return self.schema.dump(user)

    def delete(self, user_id):
        user = db.get_or_404(User, user_id)
        settings = (
            db.session.query(PersonalizationSettings)
            .filter_by(id=request.args.get("settings_id"), user_id=user.id)
            .one_or_none()
        )
        settings.is_disabled = True
        db.session.commit()
        return {"success": True}
