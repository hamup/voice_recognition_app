#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import xml.etree.ElementTree as ET
import subprocess

def main():
    host = 'localhost'
    port = 10500

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    try:
        data = ''
        while 1:
            if '</RECOGOUT>\n.' in data:
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
                for whypo in root.findall('./SHYPO/WHYPO'):
                    command = whypo.get('WORD')
                    score = float(whypo.get('CM'))

                    if command == u'ただいま' and score >= 0.9:
                        print("ただいま！")
                        p = subprocess.Popen(['python','musicPlay.py'])
                    elif command == u'おはよう' and score >= 0.9:
                        print("おはよう！")
                data = ''
            else:
                data = data + client.recv(1024)
    except KeyboardInterrupt:
        client.close()

if __name__ == "__main__":
    main()
