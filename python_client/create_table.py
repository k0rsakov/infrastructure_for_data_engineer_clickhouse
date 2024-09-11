import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    username='click',
    password='click',
)

client.query(
    '''
    CREATE TABLE IF NOT EXISTS test_table 
    (
        id UInt8,
        name String
    ) 
    ENGINE = MergeTree()
    ORDER BY id
    '''
)
