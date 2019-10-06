import requests

def get_upload_server(group_id, access_token):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': group_id,
        'access_token': access_token,
        'v': 5.101
    }
    response = requests.get(url, params=params).json()
    if 'error' in response:
        raise requests.HTTPError
    return response['response']['upload_url']


def upload_photo_to_server(server_url, filename):
    with open(filename, 'rb') as f:
        url = server_url
        files = {
            'photo': f
        }
        response = requests.post(url, files=files).json()
        if 'error' in response:
            raise requests.HTTPError
        return response['server'], response['photo'], response['hash']


def upload_photo_to_album(server, photo, hash_vk, group_id, access_token):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'server': server,
        'photo': photo,
        'hash': hash_vk,
        'group_id': group_id,
        'access_token': access_token,
        'v': 5.101
    }
    response = requests.post(url, params=params).json()
    if 'error' in response:
        raise requests.HTTPError
    return response['response'][0]['id'], response['response'][0]['owner_id']


def post_photo(access_token, comment, group_id, media_id, owner_id):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': access_token,
        'v': 5.101,
        'message': comment,
        'owner_id': -(group_id),
        'from_group': 1,
        'attachments': f'photo{owner_id}_{media_id}'
    }
    response = requests.post(url, params=params)
    if 'error' in response:
        raise requests.HTTPError