import requests


def get_last_comics_num():
    url = 'http://xkcd.com/info.0.json'
    response = requests.get(url).json()
    response.raise_for_status()
    return response['num']


def get_image_url_filename_comment(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url).json()
    response.raise_for_status()
    filename = f'{response["title"]}.png'
    file_url = response['img']
    comment = response['alt']
    return file_url, filename, comment

def get_image(url, filename):
    response_img = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response_img.content)