# Planets
This is your encyclopedia to get familiar with different planets around us!

## Development setup

Please follow the following steps in order to getting started with development.

```bash
# Clone project
git clone http://94.237.55.76:8888/git/techtest_journey.git
cd techtest_journey/

# IMPORTANT:
# A heads up! the IP in the git repository link above (`94.237.55.76:8888`)
# will be expired. So, please generate new link before cloning and use IP
# from that link.

# Install dependencies into development environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Start development server
bash start_server.sh

# Run unit tests
bash run_tests.sh

# Install precommit hooks with flake8, isort, black so that the best
# practices can be enforced on each commit you make.
pre-commit install
# Now, do some violation and try to commit ;)
```
