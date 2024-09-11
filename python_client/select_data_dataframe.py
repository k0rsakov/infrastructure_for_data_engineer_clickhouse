import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    username='click',
    password='click',
)

df = client.query_df(
    '''
    SELECT * FROM test_table
    ''',
)

print(df)
