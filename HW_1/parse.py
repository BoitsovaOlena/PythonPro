def parse(query: str) -> dict:
    if not isinstance(query, str):
        raise TypeError\
            ('parse() argument must be a string')
    query = query.split('?', 1)
    if len(query) > 1:
        query_dict = {x.split('=', 1)[0]: x.split('=', 1)[1] for x in query[1].split('&') if '=' in x}
        return query_dict
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
