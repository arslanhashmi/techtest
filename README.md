# Personalization Settings
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

## API Docs

```python
GET localhost:5001/personalization_settings/<user_id>/

{
  'id': 1,
  'email': 'arslan@example.com',
  'is_active': True,
  'first_name': 'Muhammad',
  'last_name': 'Arslan',
  'personalization_settings': [
    {
      'id': 1,
      'name': 'LINKEDIN_BIO',
      'description': 'Enable LinkedIn Bio',
      'value': True,
      'is_disabled': False
    },
    {
      'id': 2,
      'name': 'TOTAL_EXPERIENCE',
      'description': 'Year of Experience',
      'value': True,
      'is_disabled': False
    },
    {
      'id': 3,
      'name': 'LIST_OF_PAST_JOBS',
      'description': 'List of Past Jobs',
      'value': False,
      'is_disabled': False
    },
    {
      'id': 4,
      'name': 'CURRENT_JOB_SPECIALTIES',
      'description': 'List of Past Jobs',
      'value': False,
      'is_disabled': True
    }
  ]
}
```
