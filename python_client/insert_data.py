import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    username='click',
    password='click',
)

client.query(
    '''
    INSERT INTO test_table
    VALUES
    (1, 'name1'),
    (2, 'name2'),
    (3, 'name3'),
    (4, 'name4'),
    (5, 'name5'),
    (6, 'name6'),
    (7, 'name7'),
    (8, 'name8'),
    (9, 'name9'),
    (10, 'name10')
    '''
)