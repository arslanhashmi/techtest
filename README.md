# Personalization
This lets you personalize users settings through Flask REST APIs.

## Development setup

Please follow the following steps in order to getting started with development.

```bash

# 1) Change your current directory to project root directory
cd techtest/

# 2) Start development server which should be accessible at `localhost:5001` after the containers are up and running
docker-compose up --build

# This doesn't come with any user information already added to the database, in order to test this – I have build the test cases that are covering all the API endpoints so please run those tests to observe how the APIs are behaving.

# Run unit tests (pytests)
docker compose exec web /bin/bash scripts/run_tests.sh

# SSH into the flask webapp container
docker compose exec web /bin/bash
```

## Contributing

Install precommit hooks with flake8, isort, black so that the best practices can be enforced on each commit you make:
```bash
pre-commit install
```
Now, do some violation and try to commit ;)

# API Docs
The following APIs are documented with their response which can be tried in console via cURL utility.

## Retrieve Personalized Settings
```python
❯ curl --location 'http://localhost:5001/personalization_settings/1/'

# Sample Response
{
  "id": 1,
  "email": "arslan@example.com",
  "is_active": true,
  "first_name": "Muhammad",
  "last_name": "Arslan",
  "personalization_settings": [
    {
      "id": 1,
      "name": "LINKEDIN_BIO",
      "description": "Enable LinkedIn Bio",
      "value": true,
      "is_disabled": false
    },
    {
      "id": 2,
      "name": "TOTAL_EXPERIENCE",
      "description": "Year of Experience",
      "value": true,
      "is_disabled": false
    },
    {
      "id": 3,
      "name": "CURRENT_EXPERIENCE",
      "description": "Current Experience",
      "value": true,
      "is_disabled": false
    },
    {
      "id": 4,
      "name": "LIST_OF_PAST_JOBS",
      "description": "List of Past Jobs",
      "value": false,
      "is_disabled": false
    },
    {
      "id": 5,
      "name": "CURRENT_JOB_DESCRIPTION",
      "description": "Current Job Description",
      "value": false,
      "is_disabled": true
    },
    {
      "id": 6,
      "name": "CURRENT_JOB_SPECIALTIES",
      "description": "Current Job Specialties",
      "value": false,
      "is_disabled": true
    }
  ]
}
```
## Update Personalized Settings
```python
❯ curl --location 'http://localhost:5001/personalization_settings/1/' \
--header 'Content-Type: application/json' \
--data '{
    "id": 1,
    "value": false,
}'

# Sample Response
{
    "id": 1,
    "email": "arslan@example.com",
    "is_active": true,
    "first_name": "Muhammad",
    "last_name": "Arslan",
    "personalization_settings": [
        {
            "id": 1,
            "name": "LINKEDIN_BIO",
            "description": "Enable LinkedIn Bio",
            "value": false,
            "is_disabled": false
        },
        {
            "id": 2,
            "name": "TOTAL_EXPERIENCE",
            "description": "Year of Experience",
            "value": true,
            "is_disabled": false
        },
        {
            "id": 3,
            "name": "CURRENT_EXPERIENCE",
            "description": "Current Experience",
            "value": true,
            "is_disabled": false
        },
        {
            "id": 4,
            "name": "LIST_OF_PAST_JOBS",
            "description": "List of Past Jobs",
            "value": false,
            "is_disabled": false
        },
        {
            "id": 5,
            "name": "CURRENT_JOB_DESCRIPTION",
            "description": "Current Job Description",
            "value": false,
            "is_disabled": true
        },
        {
            "id": 6,
            "name": "CURRENT_JOB_SPECIALTIES",
            "description": "Current Job Specialties",
            "value": false,
            "is_disabled": true
        },
    ]
}
```

## Disable/Delete Personalized Settings
```python
❯ curl --location --request DELETE 'http://localhost:5001/personalization_settings/1/?settings_id=1'

# Sample response
{
    "success": true
}

# Now, try to retrieve the setting with ID=1, you should find `is_disabled` True for that setting.
```