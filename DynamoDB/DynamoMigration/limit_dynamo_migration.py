import boto3    

def table_exists(dynamodb, table_name):    
    try:    
        dynamodb.Table(table_name).load()    
    except Exception as e:    
        if 'ResourceNotFoundException' in str(e):    
            return False    
        else:    
            raise    
    else:    
        return True    

def create_table(dest_dynamodb, table_name, key_schema, attribute_definitions, provisioned_throughput, global_secondary_indexes=None, local_secondary_indexes=None):      
    if table_exists(dest_dynamodb, table_name):      
        print(f"Table {table_name} already exists in destination. Skipping table creation.")      
    else:      
        try:      
            table_arguments = {      
                'TableName': table_name,      
                'KeySchema': key_schema,      
                'AttributeDefinitions': attribute_definitions,      
                'ProvisionedThroughput': provisioned_throughput,      
            }      
            if global_secondary_indexes:      
                table_arguments['GlobalSecondaryIndexes'] = [      
                    {      
                        'IndexName': idx['IndexName'],      
                        'KeySchema': idx['KeySchema'],      
                        'Projection': idx['Projection'],      
                        'ProvisionedThroughput': {      
                            'ReadCapacityUnits': idx['ProvisionedThroughput']['ReadCapacityUnits'],      
                            'WriteCapacityUnits': idx['ProvisionedThroughput']['WriteCapacityUnits']      
                        }      
                    } for idx in global_secondary_indexes      
                ]    
            if local_secondary_indexes:    
                table_arguments['LocalSecondaryIndexes'] = [    
                    {    
                        'IndexName': idx['IndexName'],    
                        'KeySchema': idx['KeySchema'],    
                        'Projection': idx['Projection']    
                    } for idx in local_secondary_indexes    
                ]    
            table = dest_dynamodb.create_table(**table_arguments)      
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)      
            print("Table created successfully.")      
        except Exception as e:      
            print(f"Error creating table: {e}")     

def copy_items(src_table, dest_table, item_limit):      
    paginator = src_table.meta.client.get_paginator('scan')      
    count = 0  
    for page in paginator.paginate(TableName=src_table.name):      
        for item in page['Items']:      
            try:       
                dest_table.put_item(Item=item)  
                count += 1  
                print(f"Copied item {count}")  
                if item_limit and count >= item_limit:  
                    return   
            except Exception as e:      
                print(f"Error putting item: {e}")  

def copy_table(src_dynamodb, dest_dynamodb, src_table_name, dest_table_name, item_limit):      
    try:      
        source_table = src_dynamodb.Table(src_table_name)      
        dest_table = dest_dynamodb.Table(dest_table_name)      

        key_schema = source_table.key_schema      
        attribute_definitions = source_table.attribute_definitions      
        provisioned_throughput = {      
            'ReadCapacityUnits': source_table.provisioned_throughput['ReadCapacityUnits'],      
            'WriteCapacityUnits': source_table.provisioned_throughput['WriteCapacityUnits']      
        }      
        global_secondary_indexes = source_table.global_secondary_indexes if source_table.global_secondary_indexes else None    
        local_secondary_indexes = source_table.local_secondary_indexes if source_table.local_secondary_indexes else None    

        create_table(dest_dynamodb, dest_table_name, key_schema, attribute_definitions, provisioned_throughput, global_secondary_indexes, local_secondary_indexes)      
        copy_items(source_table, dest_table, item_limit)      

    except Exception as e:      
        print(f"Error copying table: {e}")      

def check_pitr(src_dynamodb, table_name):    
    try:    
        pitr_status = src_dynamodb.meta.client.describe_continuous_backups(    
            TableName=table_name    
        )['ContinuousBackupsDescription']['PointInTimeRecoveryDescription']['PointInTimeRecoveryStatus']
        return pitr_status == 'ENABLED'    
    except Exception as e:    
        print(f"Error checking Point in Time Recovery status: {e}")    
        return False    

def enable_pitr(dest_dynamodb, table_name):    
    try:    
        dest_dynamodb.meta.client.update_continuous_backups(    
            TableName=table_name,    
            PointInTimeRecoverySpecification={    
                'PointInTimeRecoveryEnabled': True    
            }    
        )    
        print(f"Point in Time Recovery enabled for {table_name}.")    
    except Exception as e:    
        print(f"Error enabling Point in Time Recovery: {e}")    


source_profile_name = 'default'  
source_table_name = 'AppDB'  
source_region = 'us-west-2'  

destination_profile_name = 'default'  
destination_table_name = 'test_AppDB'  
destination_region = 'us-west-2'  

# Source session and DynamoDB resource      
src_session = boto3.Session(profile_name=source_profile_name, region_name=source_region)      
src_dynamodb = src_session.resource('dynamodb')      

# Destination session and DynamoDB resource      
dest_session = boto3.Session(profile_name=destination_profile_name, region_name=destination_region)      
dest_dynamodb = dest_session.resource('dynamodb')      

# Set item limit
#*Use None for copy all items
item_limit = 250

# Call the function      
copy_table(src_dynamodb, dest_dynamodb, source_table_name, destination_table_name, item_limit)      

if check_pitr(src_dynamodb, source_table_name):      
    enable_pitr(dest_dynamodb, destination_table_name)  
