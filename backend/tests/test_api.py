import pytest
from app import db
from app.models.personalization import (
    PersonalizationSettings,
    PersonalizationSettingsType,
)
from app.models.user import User


def get_settings(name, data):
    for settings in data:
        if settings["name"] == name:
            return settings


class TestV1API:
    """
    Test cases for v1 API.
    """

    def test_personalization_settings_retrieval_for_user(self, setup_data, client):
        """
        Test retrieval of personalized settings for a user.
        """
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
        settings_data = user_data["personalization_settings"]
        assert len(settings_data) == 4

        settings = get_settings(PersonalizationSettingsType.LINKEDIN_BIO, settings_data)
        assert settings["value"]
        assert not settings["is_disabled"]

        settings = get_settings(
            PersonalizationSettingsType.TOTAL_EXPERIENCE, settings_data
        )
        assert settings["value"]
        assert not settings["is_disabled"]

        settings = get_settings(
            PersonalizationSettingsType.LIST_OF_PAST_JOBS, settings_data
        )
        assert not settings["value"]
        assert not settings["is_disabled"]

        settings = get_settings(
            PersonalizationSettingsType.CURRENT_JOB_SPECIALTIES, settings_data
        )
        assert not settings["value"]
        assert settings["is_disabled"]

    def test_disable_personalization_settings(self, setup_data, client):
        """
        Test disable personalization settings.
        """
        settings_id = 1
        user = (
            db.session.query(User).filter_by(email="arslan@example.com").one_or_none()
        )
        settings = (
            db.session.query(PersonalizationSettings)
            .filter_by(id=settings_id, user_id=user.id)
            .one_or_none()
        )
        assert not settings.is_disabled

        response = client.delete(
            f"/personalization_settings/{user.id}/?settings_id={settings_id}"
        )
        assert response.status_code == 200

        settings = (
            db.session.query(PersonalizationSettings)
            .filter_by(id=settings_id, user_id=user.id)
            .one_or_none()
        )
        assert settings.is_disabled

    @pytest.mark.parametrize(
        "expected_settings_data,",
        [
            {"id": 1, "value": False, "is_disabled": True},
            {"id": 2, "value": False, "is_disabled": True},
            {"id": 2, "value": True, "is_disabled": False},
        ],
    )
    def test_update_personalization_settings(
        self, expected_settings_data, setup_data, client
    ):
        """
        Test updates to personalization settings.
        """
        user = (
            db.session.query(User).filter_by(email="arslan@example.com").one_or_none()
        )
        assert user.is_active

        response = client.post(
            f"/personalization_settings/{user.id}/", json=expected_settings_data
        )
        assert response.status_code == 200

        personalized_settings = (
            db.session.query(PersonalizationSettings)
            .filter_by(id=expected_settings_data["id"])
            .one_or_none()
        )

        settings = get_settings(
            personalized_settings.name, response.json["personalization_settings"]
        )
        # assert response
        assert settings["value"] == expected_settings_data["value"]
        assert settings["is_disabled"] == expected_settings_data["is_disabled"]
        # assert values set on settings instance
        assert personalized_settings.value == expected_settings_data["value"]
        assert (
            personalized_settings.is_disabled == expected_settings_data["is_disabled"]
        )
