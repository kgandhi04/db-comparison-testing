# Database Comparison Testing

This repository contains a framework for testing and validating database consistency across development, test, and production environments.

---

## Features

- Schema validation to ensure structure consistency.
- Data consistency checks for row counts, sample rows, and null values.
- Configurable database connections through `config.yaml`.
- Automated testing using `pytest` with HTML reporting.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/db-comparison-testing.git
   cd db-comparison-testing
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update `config/config.yaml` with your database details.

---

## Running Tests

1. Run all tests:
   ```bash
   pytest --html=reports/html/report.html
   ```

2. View the report in the `reports/html/` directory.

---

## Contributing

Contributions are welcome!

---

## License

This project is licensed under the MIT License.
