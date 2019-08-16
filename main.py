import os
import random

from dotenv import load_dotenv
import requests

from load_image import get_image, get_image_url_filename_comment, get_last_comics_num
from upload_image_to_vk import get_upload_server, post_photo, upload_photo_to_album, upload_photo_to_server


load_dotenv()
TOKEN = os.getenv('ACCESS_TOKEN')
GROUP_ID = 185444788


def main():
    last_comics_num = get_last_comics_num()
    random_comics_num = random.randint(1, last_comics_num)
    img_url, img_name, img_comment = get_image_url_filename_comment(random_comics_num)
    get_image(img_url, img_name)
    server_url = get_upload_server(GROUP_ID, TOKEN)
    server, photo, hash_vk =  upload_photo_to_server(server_url, img_name)
    media_id, owner_id = upload_photo_to_album(server, photo, hash_vk, GROUP_ID, TOKEN)
    post_photo(TOKEN, img_comment, GROUP_ID, media_id, owner_id)
    os.remove(img_name)


if __name__ == "__main__":
    main()
    
    
