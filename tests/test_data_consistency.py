import pytest
from scripts.db_utils import get_connection, get_row_count
import yaml

@pytest.fixture(scope="module")
def config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def test_row_count_consistency(config):
    tables = ["users", "orders"]  # Add your table names
    connections = {
        env: get_connection(config[env]) for env in ["dev", "test", "prod"]
    }
    row_counts = {}

    for env, conn in connections.items():
        with conn.cursor() as cursor:
            row_counts[env] = {table: get_row_count(cursor, table) for table in tables}

    for table in tables:
        assert row_counts["dev"][table] == row_counts["test"][table], f"Row count mismatch in {table} between Dev and Test"
        assert row_counts["dev"][table] == row_counts["prod"][table], f"Row count mismatch in {table} between Dev and Prod"
