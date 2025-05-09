# secure-csv-api

Secure CSV API is a backend service designed to securely handle, process, and store CSV files. It leverages AWS infrastructure and the AWS CDK for deployment, ensuring scalability, security, and reliability.

## Features

- Secure and scalable storage of CSV files using AWS S3.
- RESTful API endpoints for uploading,  CSV files.
- Authentication and authorization mechanisms.
- Infrastructure as Code using AWS CDK.
- Multi-region deployment support.

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- [AWS CDK](https://aws.amazon.com/cdk/) installed (`npm install -g aws-cdk`)
- [Poetry](https://python-poetry.org/) for dependency management
- [Ruff](https://github.com/charliermarsh/ruff) for linting
- Python 3.12 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/secure-csv-api.git
   cd secure-csv-api
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Bootstrap your AWS environment for CDK:

   ```bash
   cdk bootstrap
   ```

4. Set up pre-commit hooks:

   ```bash
   pre-commit install
   ```

## Useful Commands

- **Deploy the application**:
  ```bash
  cdk deploy
  ```

- **Destroy the application**:
  ```bash
  cdk destroy
  ```

- **Run tests**:
  ```bash
  poetry run pytest
  ```

- **Lint the code with Ruff**:
  ```bash
  poetry run ruff check .
  ```

- **Fix linting issues with Ruff**:
  ```bash
  poetry run ruff check . --fix
  ```



- **Run pre-commit hooks manually**:
  ```bash
  pre-commit run --all-files
  ```

- **Update dependencies**:
  ```bash
  poetry update
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
