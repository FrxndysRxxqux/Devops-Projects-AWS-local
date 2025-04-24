# DynamoDB Migration Tools

This repository contains scripts for migrating DynamoDB tables between AWS accounts or within the same account.

## Scripts Overview

### 1. dynamo_migration.py

A script that performs a complete migration of a DynamoDB table, including:

- Table structure replication
- Data copying
- Global Secondary Indexes (GSI) migration
- Local Secondary Indexes (LSI) migration
- Point-in-Time Recovery (PITR) configuration

Key features:
- Copies all items from source to destination table
- Preserves table configuration including provisioned throughput
- Maintains indexes structure
- Transfers PITR settings if enabled in source

### 2. limit_dynamo_migration.py

Similar to dynamo_migration.py but with the added capability to limit the number of items copied. Useful for:

- Testing migrations with a subset of data
- Staged migrations
- Development and QA environments

Additional features:
- Configurable item limit for migration
- Progress tracking with item count
- All other features from the base migration script

## Usage

### Configuration

Both scripts require the following configuration:

```python
source_profile_name = 'default'          # AWS profile for source
source_table_name = 'YourSourceTable'    # Source table name
source_region = 'us-west-2'              # Source region

destination_profile_name = 'default'      # AWS profile for destination
destination_table_name = 'YourDestTable'  # Destination table name
destination_region = 'us-west-2'         # Destination region
```

For limit_dynamo_migration.py, you can also set:

```python
item_limit = 250  # Set to None to copy all items
```

### Prerequisites
- Python 3.x
- boto3 library
- AWS credentials configured
- Appropriate IAM permissions for both source and destination
### Required Permissions
The AWS credentials need the following permissions:

- dynamodb:DescribeTable
- dynamodb:CreateTable
- dynamodb:PutItem
- dynamodb:Scan
- dynamodb:DescribeContinuousBackups
- dynamodb:UpdateContinuousBackups
## Functions Documentation
### Common Functions
- table_exists(dynamodb, table_name) : Checks if a table exists in DynamoDB
- create_table(...) : Creates a new table with the same schema as source
- copy_items(...) : Copies items from source to destination
- check_pitr(...) : Checks if PITR is enabled on source table
- enable_pitr(...) : Enables PITR on destination table
- copy_table(...) : Orchestrates the entire migration process
## Error Handling
Both scripts include comprehensive error handling for:

- Table creation failures
- Item copy failures
- PITR configuration issues
- Resource not found scenarios