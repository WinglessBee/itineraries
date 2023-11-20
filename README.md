# Itineraries Sorting API

This is a REST API that can sort a given list of itineraries based on various sorting criteria:

- `cheapest`: Sort based on price, with the most affordable itineraries coming first.
- `fastest`: Sort by duration, with the shortest itineraries on top.
- `best`: Sort by duration and price, with optimal balance between them.

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.11 or higher
- [Poetry](https://python-poetry.org/docs/) (Python dependency management tool)
- [openexchangerates.org](https://openexchangerates.org/signup/free) account with `app_id`

### Installation

1. Clone the repository
   ```shell
   git clone <repo_url>
   ```

2. Navigate to the directory
   ```shell
   cd itineraries
   ```

3. Install the dependencies
   ```shell
   poetry install
   ```

### Running the application

1. Activate the virtual environment by running:
   ```shell
   poetry shell
   ```

2. Set `app_id` for [openexchangerates.org](https://openexchangerates.org/)
   ```shell
   EXPORT CONVERTOR_APP_ID=<app_id>
   ```

3. Start the API server:
   ```shell
   make run
   ```

4. Open the browser and navigate to http://localhost:8000/docs

### Local development and testing
With active `poetry shell` there are multiple make recipes available:

- Running all code quality tools 
   ```shell
   make c
   ```

- Running all tests
   ```shell
   make test
   ```

- More details
   ```shell
   make help
   ```
