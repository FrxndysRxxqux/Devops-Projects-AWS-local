import boto3  
import botocore.session  
import csv  
import os  

# Obtén la lista de todos los perfiles disponibles  
all_profiles = botocore.session.Session().available_profiles  
region_name = 'us-west-1'  # Cambia esto por la región que quieras usar  

# Itera sobre cada perfil  
for profile_name in all_profiles:  
    session = boto3.Session(profile_name=profile_name, region_name=region_name)  
    dynamodb = session.client('dynamodb')  

    response = dynamodb.list_tables()  
    tables = response['TableNames']  

    max_indexes = 0  
    for table in tables:  
        table_info = dynamodb.describe_table(TableName=table)  
        try:  
            index_count = len(table_info['Table']['GlobalSecondaryIndexes'])  
            if index_count > max_indexes:  
                max_indexes = index_count  
        except KeyError:  
            pass  

    # Define la carpeta donde quieres guardar el archivo  
    folder_name = 'Reportes'  
    current_directory = os.getcwd()  
    folder_path = os.path.join(current_directory, folder_name)  

    # Crea la carpeta si no existe  
    if not os.path.exists(folder_path):  
        os.makedirs(folder_path)  

    # Asegúrate de cambiar el nombre del archivo CSV para que sea único por perfil  
    with open(os.path.join(folder_path, f'{profile_name}_{region_name}_dynamodb_tables.csv'), 'w', newline='') as file:  
        writer = csv.writer(file)  

        index_headers = []  
        for i in range(max_indexes):  
            index_headers.append(f"Índice secundario global {i+1}")  
            index_headers.append(f"Índice {i+1} - NumberOfDecreasesToday")  
            index_headers.append(f"Índice {i+1} - ReadCapacityUnits")  
            index_headers.append(f"Índice {i+1} - WriteCapacityUnits")  

        writer.writerow(["Nombre de la tabla", "Fecha de creación", "Cantidad de ítems", "NumberOfDecreasesToday", "ReadCapacityUnits", "WriteCapacityUnits", "Tamaño en bytes", "Backups", "Recuperación punto a punto"] + index_headers)  

        for table in tables:  
            table_info = dynamodb.describe_table(TableName=table)  

            backups = dynamodb.list_backups(TableName=table)  
            pitr = dynamodb.describe_continuous_backups(TableName=table)  

            if pitr['ContinuousBackupsDescription']['PointInTimeRecoveryDescription']['PointInTimeRecoveryStatus'] == 'ENABLED':  
                pitr_status = 'HABILITADO'  
            else:  
                pitr_status = 'DESHABILITADO'  

            provisioned_throughput = table_info['Table']['ProvisionedThroughput']  

            index_info = []  
            try:  
                for index in table_info['Table']['GlobalSecondaryIndexes']:  
                    index_info.append(index['IndexName'])  
                    index_info.append(index['ProvisionedThroughput']['NumberOfDecreasesToday'])  
                    index_info.append(index['ProvisionedThroughput']['ReadCapacityUnits'])  
                    index_info.append(index['ProvisionedThroughput']['WriteCapacityUnits'])  
            except KeyError:  
                pass  

            while len(index_info) < max_indexes * 4:  
                index_info.append('N/A')  

            writer.writerow([table,  
                            table_info['Table']['CreationDateTime'].strftime("%Y-%m-%d %H:%M:%S"),  
                            table_info['Table']['ItemCount'],  
                            provisioned_throughput['NumberOfDecreasesToday'],  
                            provisioned_throughput['ReadCapacityUnits'],  
                            provisioned_throughput['WriteCapacityUnits'],  
                            table_info['Table']['TableSizeBytes'],  
                            len(backups['BackupSummaries']),  
                            pitr_status] + index_info)  

