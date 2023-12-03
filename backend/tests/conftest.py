import pytest
from app import app as flask_app
from app import db
from app.models.personalization import (
    PersonalizationSettings,
    PersonalizationSettingsType,
)
from app.models.user import User


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


@pytest.fixture
def setup_data():
    with flask_app.app_context():
        # DB cleanup before running a test.
        db.drop_all()
        db.create_all()

        # Add a sample user
        user = User(
            first_name="Muhammad",
            last_name="Arslan",
            email="arslan@example.com",
            is_active=True,
        )
        user.set_password("123")
        db.session.add(user)
        db.session.flush()

        # Add a few personalization settings
        linkedin_setting = PersonalizationSettings(
            user=user,
            name=PersonalizationSettingsType.LINKEDIN_BIO,
            description="Enable LinkedIn Bio",
            value=True,
        )
        db.session.add(linkedin_setting)

        exp_setting = PersonalizationSettings(
            user=user,
            name=PersonalizationSettingsType.TOTAL_EXPERIENCE,
            description="Year of Experience",
            value=True,
        )
        db.session.add(exp_setting)

        current_experience = PersonalizationSettings(
            user=user,
            name=PersonalizationSettingsType.CURRENT_EXPERIENCE,
            description="Current Experience",
            value=True,
        )
        db.session.add(current_experience)

        past_jobs = PersonalizationSettings(
            user=user,
            name=PersonalizationSettingsType.LIST_OF_PAST_JOBS,
            description="List of Past Jobs",
            value=False,
        )
        db.session.add(past_jobs)

        current_job_description = PersonalizationSettings(
            user=user,
            name=PersonalizationSettingsType.CURRENT_JOB_DESCRIPTION,
            description="Current Job Description",
            value=False,
            is_disabled=True,
        )
        db.session.add(current_job_description)

        past_jobs_setting = PersonalizationSettings(
            user=user,
            name=PersonalizationSettingsType.CURRENT_JOB_SPECIALTIES,
            description="Current Job Specialties",
            value=False,
            is_disabled=True,
        )
        db.session.add(past_jobs_setting)

        db.session.commit()
        yield
