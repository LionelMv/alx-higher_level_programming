#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)

    try:
        json_dic = r.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if json_dic:
            if 'id' in json_dic and 'name' in json_dic:
                print(f"[{json_dic['id']}] {json_dic['name']}")
        else:
            print("No result")
    # try:
    #     json_dic = r.json()
    #     if json_dic:
    #         print("[{}] {}".format(json_dic.get('id'), json_dic.get('name')))
    #     else:
    #         print("No result")
    # except ValueError as e:
    #     print("Not a valid JSON")
