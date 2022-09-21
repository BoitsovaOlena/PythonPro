import requests


def check_request(url, content_type):
    """
    The response to the url request is being checked. If the status of the response is within 200s and the type of
    content corresponds to the one specified in the arguments, the function returns the response. Otherwise None.
    :param url:
    :type url: str
    :param content_type: The value should correspond to the 'Content-Type' from the headers of the response.
    :type content_type: str
    :return: A response received from the server that satisfies our requirements.
    :rtype: requests.models.Response|None
    """
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    else:
        if 300 > resp.status_code >= 200:
            if resp.headers.get('Content-Type') == content_type:
                return resp
        return None
