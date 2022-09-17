def parse_cookie(query: str) -> dict:
    if not isinstance(query, str):
        raise TypeError\
            ('parse_cookie() argument must be a string')
    query_list = query.split(';')
    if len(query_list) > 0:
        query_dict = {x.split('=', 1)[0]: x.split('=', 1)[1] for x in query_list if '=' in x}
        return query_dict
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

