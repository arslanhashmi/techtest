from app import db
from app.models.user import User, UserSchema
from flask_restful import Resource


class PersonalizedSettingsResource(Resource):
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
        return self.schema.dump(user)

    def delete(self, user_id):
        user = db.get_or_404(User, user_id)
        user.is_active = False
        db.session.commit()
        return {"success": True}
