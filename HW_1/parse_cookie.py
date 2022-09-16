def parse_cookie(query: str) -> dict:
    if not isinstance(query, str):
        raise TypeError\
            ('parse() argument must be a string')
    query_list = query.split(';')
    query_dict = {}
    for i in query_list:
        if i.count('name') == 1:
            query_dict.update({"name": i.lstrip('name=')})
        elif i.count('age') == 1:
            query_dict.update({"age": i.lstrip('age=')})
    if len(query_dict) == 0:
        print('The requested query parameters were not found')
    return query_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

