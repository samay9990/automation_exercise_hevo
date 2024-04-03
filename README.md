**Test Automation for Hevo Pipeline Validation**
-
This repository contains test automation scripts to validate the creation and functionality of a Hevo pipeline, including table creation, data transfer, and teardown.

**Setup** 
- 
1. Install the required dependencies:
      - Python (version >= 3.6) 
      - psycopg2 (for PostgreSQL database interaction) 
      - Selenium WebDriver (for programmatically creating the pipeline)
  
2. Clone this repository:
   - git clone https://github.com/samay9990/automation_exercise_hevo.git

3. Navigate to the project directory:
   - cd hevo-pipeline-validation

4. Configure the test parameters:
   - Open config.yaml file and provide the necessary information such as database connection details, API keys, etc.
   
5. Ensure that your PostgreSQL and MySQL databases are up and running, and accessible from the provided configuration.


**Test Execution**
-
1. Run the test setup script to create the source and destination tables:
   - python test_setup.py
2. Run the test automation script to programmatically create the Hevo pipeline using Selenium WebDriver:
   - python create_pipeline.py
3. After the pipeline finishes loading, run the validation script to validate the creation of the destination table and data equality between source and destination:
   - python validate_pipeline.py

**Teardown**
-
1. Once testing is complete, run the teardown script to drop the source and destination tables, Hevo pipeline, and any other temporary resources created during the test:
   - python test_teardown.py

**Notes**
-
- Ensure that you have proper permissions and access to the databases and Hevo API.
- Modify the configuration and scripts as per your environment and requirements.