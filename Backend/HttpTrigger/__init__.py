import os
import azure.functions as func
from azure.data.tables import TableClient
from azure.core.exceptions import ResourceNotFoundError

def main(req: func.HttpRequest) -> func.HttpResponse:
    #fetch connection string from app settings
    connection_string = os.environ["CosmosDbConnectionString"]
    
    # Initialize the TableClient connection
    table_client = TableClient.from_connection_string(connection_string, table_name="Table1")
    
    # Retrieve the entity with PartitionKey="MyCount" and RowKey="CountValue"
    try:
        entity = table_client.get_entity(partition_key="MyCount", row_key="CountValue")
    except ResourceNotFoundError:
        # If the entity doesn't exist, create it with count=0
        entity = {"PartitionKey": "MyCount", "RowKey": "CountValue", "count": 0}
    
    # Increment the count value by 1
    entity["count"] += 1
    
    # Update the entity in the table
    table_client.update_entity(mode="replace", entity=entity)

    #return entity
    return func.HttpResponse(f"guest {entity['count']}")