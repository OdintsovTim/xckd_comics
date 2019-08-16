import argparse
import os
import random


from load_image import get_image, get_image_url_filename_comment, get_last_comics_num
from upload_image_to_vk import get_upload_server, post_photo, upload_photo_to_album, upload_photo_to_server


def main():
    parser = argparse.ArgumentParser(description='This program uploads comics to group in VK')
    parser.add_argument('token')
    parser.add_argument('group_id')
    args = parser.parse_args()
    token = args.token

    group_id = int(args.group_id)
    last_comics_num = get_last_comics_num()
    random_comics_num = random.randint(1, last_comics_num)
    img_url, img_name, img_comment = get_image_url_filename_comment(random_comics_num)
    get_image(img_url, img_name)
    server_url = get_upload_server(group_id, token)
    server, photo, hash_vk =  upload_photo_to_server(server_url, img_name)
    media_id, owner_id = upload_photo_to_album(server, photo, hash_vk, group_id, token)
    post_photo(token, img_comment, group_id, media_id, owner_id)
    os.remove(img_name)


if __name__ == "__main__":
    main()
    
    
