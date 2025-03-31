# pytaigaclient

A Python client library for interacting with the Taiga API. This library provides a simple and intuitive interface for accessing Taiga functionality programmatically.

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

```python
from pytaigaclient import TaigaClient

# Initialize the client
client = TaigaClient(url="https://api.taiga.io/api/v1", token="your-auth-token")

# Example usage
projects = client.get_projects()
```

## Development

### Setup Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pytaigaclient.git
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

