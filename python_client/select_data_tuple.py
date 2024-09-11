import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    username='click',
    password='click',
)

with client.query_rows_stream('SELECT * FROM test_table') as stream:
    for row in stream:
        print(row)
