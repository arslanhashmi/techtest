from .api import PersonalizedSettingsResource

routes = [("/personalization_settings/<user_id>/", PersonalizedSettingsResource)]
