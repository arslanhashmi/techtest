from .api import PersonalizationSettingsResource

routes = [("/personalization_settings/<user_id>/", PersonalizationSettingsResource)]
