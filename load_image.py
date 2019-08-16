import requests


def get_last_comics_num():
    url = 'http://xkcd.com/info.0.json'
    response = requests.get(url).json()
    return response['num']


def get_image_url_filename_comment(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url).json()
    filename = f'{response["title"]}.png'
    file_url = response['img']
    comment = response['alt']
    return file_url, filename, comment

def get_image(url, filename):
    response_img = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response_img.content)