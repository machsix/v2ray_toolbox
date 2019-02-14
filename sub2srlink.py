#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import base64
import sys

def Str2Base64(txt):
    return base64.urlsafe_b64encode(txt.encode('utf-8')).decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="generate link for subscription in ShadowRocket")

    parser.add_argument('LINK', help='url of the html file, e.g.: http://admin:password@example.com/v2ray.html')

    ARGS = parser.parse_args()
    txt = 'sub://' + Str2Base64(ARGS.LINK) + '#'
    sys.stdout.write(txt)
