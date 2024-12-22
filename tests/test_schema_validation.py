import pytest
from scripts.db_utils import get_connection, get_table_schema
import yaml

@pytest.fixture(scope="module")
def config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def test_schema_validation(config):
    tables = ["users", "orders"]  # Add your table names
    connections = {
        env: get_connection(config[env]) for env in ["dev", "test", "prod"]
    }
    schemas = {}

    for env, conn in connections.items():
        with conn.cursor() as cursor:
            schemas[env] = {table: get_table_schema(cursor, table) for table in tables}

    for table in tables:
        assert schemas["dev"][table] == schemas["test"][table], f"Schema mismatch in {table} between Dev and Test"
        assert schemas["dev"][table] == schemas["prod"][table], f"Schema mismatch in {table} between Dev and Prod"
