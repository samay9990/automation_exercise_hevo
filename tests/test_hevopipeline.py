import psycopg2
import requests
import json


class HevoAutomation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def create_pipeline(self, source_type, source_config, destination_type, destination_config, destination_prefix):
        # Connection to MySQL as the Source
        source_response = self.create_source(source_type, source_config)
        source_id = source_response['id']

        # Connection to PgSQL as the Destination
        destination_response = self.create_destination(destination_type, destination_config)
        destination_id = destination_response['id']

        # Creation of Pipeline in HEVO DATA
        pipeline_config = {
            "name": f"{destination_prefix}_pipeline",
            "source_id": source_id,
            "destination_id": destination_id
        }
        pipeline_response = self.create_pipeline_request(pipeline_config)

        return pipeline_response

    def create_source(self, source_type, source_config):
        url = 'https://in.hevodata.com/v1/sources'
        payload = {
            "source_type": source_type,
            "config": source_config
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def create_destination(self, destination_type, destination_config):
        url = 'https://in.hevodata.com/v1/destinations'
        payload = {
            "destination_type": destination_type,
            "config": destination_config
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def create_pipeline_request(self, pipeline_config):
        url = 'https://in.hevodata.com/v1/pipelines'
        response = requests.post(url, headers=self.headers, json=pipeline_config)
        return response.json()

    def teardown(self, source_config, destination_config, pipeline_id, source_table_name, destination_table_name):
        # Dropping Source and Destination tables
        source_connection = psycopg2.connect(
            host=source_config["host"],
            port=source_config["port"],
            database=source_config["database"],
            user=source_config["username"],
            password=source_config["password"]
        )
        destination_connection = psycopg2.connect(
            host=destination_config["host"],
            port=destination_config["port"],
            database=destination_config["database"],
            user=destination_config["username"],
            password=destination_config["password"]
        )
        source_cursor = source_connection.cursor()
        destination_cursor = destination_connection.cursor()

        source_cursor.execute(f"DROP TABLE IF EXISTS {'Automation_Test'}")
        destination_cursor.execute(f"DROP TABLE IF EXISTS {'samay_thakkar_Automation_Test'}")

        source_connection.commit()
        destination_connection.commit()

        source_connection.close()
        destination_connection.close()

        # Delete Hevo Pipeline
        pipeline_url = f"https://in.hevodata.com/v1/pipelines/{pipeline_id}"
        response = requests.delete(pipeline_url, headers=self.headers)
        if response.status_code == 204:
            print("Hevo Pipeline deleted successfully")
        else:
            print("Error deleting Hevo Pipeline")


if __name__ == "__main__":
    api_key = 'LENL0DJGTW'
    hevo_automation = HevoAutomation(api_key)

    source_type = 'mysql'
    source_config = {
        "host": "mysql-database-1.cx08aukg2czn.eu-north-1.rds.amazonaws.com",
        "port": 3306,
        "database": "automation",
        "username": "admin",
        "password": "Chocolatecake123*"
    }

    destination_type = 'pgsql'
    destination_config = {
        "host": "postgresql-database-1.cx08aukg2czn.eu-north-1.rds.amazonaws.com",
        "port": 5432,
        "database": "postgres",
        "username": "postgres",
        "password": "Chocolatecake123*"
    }

    destination_prefix = 'samay_thakkar'
    source_table_name = "Automation_Test"
    destination_table_name = "samay_thakkar_Automation_Test"

    pipeline_response = hevo_automation.create_pipeline(source_type, source_config, destination_type,
                                                        destination_config, destination_prefix)
    print("Pipeline created successfully:", pipeline_response)

    # Assertion of the tables
    destination_table_exists = hevo_automation.create_pipeline(destination_config, destination_prefix)
    assert destination_table_exists, "Destination table not created in PgSQL database"

    destination_table = f"{destination_prefix}"
    data_equality = hevo_automation.create_destination(source_config, destination_config, source_table_name,
                                                       destination_table)
    assert data_equality, "Data in source and destination is not equal"

    # pipeline ID from the response
    pipeline_id = pipeline_response['id']

    # Perform teardown
    hevo_automation.teardown(source_config, destination_config, pipeline_id, source_table_name, destination_table_name)
