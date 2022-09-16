def parse(query: str) -> dict:
    if not isinstance(query, str):
        raise TypeError\
            ('parse() argument must be a string')
    query_position = query.find('?')
    if query_position == -1:
        print('URL has no query parameters')
        return {}
    query_list = query[query_position+1:].split('&')
    query_dict = {}
    for i in query_list:
        if i.count('name') == 1:
            query_dict.update({"name": i.lstrip('name=')})
        elif i.count('color') == 1:
            query_dict.update({"color": i.lstrip('color=')})
    if len(query_dict) == 0:
        print('The requested query parameters were not found')
    return query_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
