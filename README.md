# pytaigaclient

A Python client library for interacting with the [Taiga API](https://docs.taiga.io/api.html). This library provides a simple and intuitive interface for accessing Taiga functionality programmatically.

## What is Taiga?

[Taiga](https://taiga.io/) is an open-source project management platform for agile teams. It features support for Scrum and Kanban methodologies, issue tracking, and project management. The Taiga API allows for programmatic access to all Taiga features, enabling automation and integration with other tools.

For detailed API documentation, visit the [official Taiga API documentation](https://docs.taiga.io/api.html).

## Installation

### Using uv (recommended)

```bash
uv pip install pytaigaclient
```

### Using pip

```bash
pip install pytaigaclient
```

## Basic Usage

### Authentication

```python
from pytaigaclient import TaigaClient

# Initialize with username and password
client = TaigaClient(url="https://api.taiga.io/api/v1")
client.login(username="your-username", password="your-password")

# Or initialize with an existing auth token
client = TaigaClient(url="https://api.taiga.io/api/v1", token="your-auth-token")
```

### Working with Projects

```python
# Get all projects you have access to
projects = client.get_projects()

# Get a specific project by slug
project = client.get_project(slug="your-organization/your-project")

# Get project by ID
project = client.get_project(id=123456)

# Create a new project
new_project = client.create_project(
    name="New Project",
    description="Project description",
    is_private=True
)
```

### Managing User Stories

```python
# Get all user stories in a project
stories = client.get_user_stories(project_id=123456)

# Get a specific user story
story = client.get_user_story(id=654321)

# Create a user story
new_story = client.create_user_story(
    project_id=123456,
    subject="Implement new feature",
    description="As a user, I want to...",
    status=1,  # New status
    priority=3  # Normal priority
)

# Update a user story
updated_story = client.update_user_story(
    id=654321,
    subject="Updated subject",
    description="Updated description",
    status=2  # In progress
)
```

### Working with Tasks

```python
# Get all tasks in a project
tasks = client.get_tasks(project_id=123456)

# Get tasks for a specific user story
story_tasks = client.get_tasks(user_story_id=654321)

# Create a new task
new_task = client.create_task(
    project_id=123456,
    subject="Implement API endpoint",
    description="Create the REST API endpoint for...",
    status=1,  # New status
    assigned_to=789  # User ID
)
```

### Managing Issues

```python
# Get all issues in a project
issues = client.get_issues(project_id=123456)

# Create a new issue
new_issue = client.create_issue(
    project_id=123456,
    subject="Bug in login page",
    description="When attempting to login with correct credentials...",
    type=1,  # Bug
    priority=4,  # High
    severity=3  # Normal
)
```

### Handling Attachments

```python
# Upload an attachment to a user story
attachment = client.upload_attachment(
    object_id=654321,
    object_type="userstory",
    filename="screenshot.png",
    content="file_binary_content"
)
```

## Development

### Setup Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/talhaorak/pytaigaclient.git
   cd pytaigaclient
   ```

2. Create a virtual environment using uv:

   ```bash
   uv venv --python=cpython-3.13.2-macos-aarch64-none .venv
   ```

3. Activate the virtual environment:

   ```bash
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

4. Install development dependencies:

   ```bash
   uv pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest
```

### Code Formatting and Linting

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Type checking
mypy src
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
