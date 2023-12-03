from app import db
from app.models.personalization import PersonalizationSettingsType
from app.models.user import User


class TestV1API:
    """
    Test cases for v1 API.
    """

    def test_personalized_settings_retrieval_for_user(self, client):
        user = (
            db.session.query(User).filter_by(email="arslan@example.com").one_or_none()
        )
        assert user

        response = client.get(f"/personalization_settings/{user.id}/")
        assert response.status_code == 200

        # Assert user information
        user_data = response.json
        assert user_data["id"] == user.id
        assert user_data["email"] == "arslan@example.com"
        assert user_data["first_name"] == "Muhammad"
        assert user_data["last_name"] == "Arslan"
        assert user_data["is_active"]
        assert user.verify_password("123")

        # Assert personalized settings information
        personalization_settings = user_data["personalization_settings"]
        assert len(personalization_settings) == 4
        for settings in personalization_settings:
            if settings["name"] == PersonalizationSettingsType.LINKEDIN_BIO:
                assert settings["value"]
                assert not settings["is_disabled"]
            elif settings["name"] == PersonalizationSettingsType.TOTAL_EXPERIENCE:
                assert settings["value"]
                assert not settings["is_disabled"]
            elif settings["name"] == PersonalizationSettingsType.LIST_OF_PAST_JOBS:
                assert not settings["value"]
                assert not settings["is_disabled"]
            elif (
                settings["name"] == PersonalizationSettingsType.CURRENT_JOB_SPECIALTIES
            ):
                assert not settings["value"]
                assert settings["is_disabled"]
