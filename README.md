# v2ray subscription toolbox

This toolbox contains python scripts to generate files that can be used in [v2rayN](https://github.com/2dust/v2rayN) to subscribe [v2ray](https://github.com/v2ray) servers and also qrcode for [ShadowRocket](https://itunes.apple.com/us/app/shadowrocket/id932747118). It follows the format introduced in [v2rayN wiki](https://github.com/2dust/v2rayN/wiki/%E5%88%86%E4%BA%AB%E9%93%BE%E6%8E%A5%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E(ver-2)). It only supports http\websocket\kcp\http2 but not quic.

### Requirement
- python3
- urllib

### Tutorial
1. Prepare the configuration files of your v2ray servers, for example `config.json` and `config2.json`. Put them in the same folder of these python scripts
2. Run the following commands to generate v2rayN format configuration file
```bash
python3 conf2vmess.py -c config.json -s example.com -p 443 -o vmess.json
python3 conf2vmess.py -c config2.json -s example2.com -p 8443 -o vmess.json -a
```
The file `vmess.json` looks like the following:
```json
[
    {
        "v": "2",
        "ps": "",
        "add": "example.com",
        "port": "443",
        "id": GUID,
        "aid": "64",
        "net": "ws",
        "type": "none",
        "host": "",
        "path": "/",
        "tls": "tls"
    },
    {
        "v": "2",
        "ps": "",
        "add": "example2.com",
        "port": "8443",
        "id": "GUID",
        "aid": "64",
        "net": "ws",
        "type": "none",
        "host": "",
        "path": "/",
        "tls": "tls"
    }
]
```
3. Edit `vmess.json` manually if you need. (E.g. add unique labels to the `ps` field of each server)
4. Run the following command to generate  v2rayN format vmess link `vmess_v2rayN.lnk` and html file for subscription `vmess_v2rayN.html`
```bash
python3 vmess2sub.py vmess.json vmess_v2rayN.html -l vmess_v2rayN.lnk
```
The file `vmess_v2rayN.lnk` looks like the following:
```txt
vmess://XXX
vmess://XXX
```
5. Run the following command to generate  ShadowRocket format vmess link `vmess_sr.lnk` and html file for subscription `vmess_sr.html`
```bash
python3 vmess2sub.py vmess.json vmess_sr.html -l vmess_sr.lnk -t sr
```
6. Upload the two html files to some location of your server, for example `http://example.com/vmess_v2rayN.html` and `http://example.com/vmess_sr.html`
7. For v2rayN, you can directly use `http://example.com/vmess_v2rayN.html`
8. For ShadowRocket, you can run the following command to generate a qrcode
```bash
qrencode -l H -o qrcode.png $(python3 sub2srlink.py http://admin:password@example.com/vmess_sr.html)
``` 
9. Share the qrcode


### Usage
- conf2vmess.py
```
usage: conf2vmess.py [-h] [-c CONFIG] [-s SERVER] [-p PORT [PORT ...]]
                     [-o OUTPUT] [-a]

Script to generate v2rayN format configuration file based on https://github.co
m/2dust/v2rayN/wiki/%E5%88%86%E4%BA%AB%E9%93%BE%E6%8E%A5%E6%A0%BC%E5%BC%8F%E8%
AF%B4%E6%98%8E(ver-2)

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        path of configuration file for v2ray server (default:
                        config.json)
  -s SERVER, --server SERVER
                        domain or IP address of v2ray server (default: IP of
                        current host 67.230.177.23)
  -p PORT [PORT ...], --port PORT [PORT ...]
                        ports that v2ray server listens to (default: the ones
                        defined in configuration file)
  -o OUTPUT, --output OUTPUT
                        name of v2rayN format configuration file (default:
                        STDOUT)
  -a, --append          append to output file (default: False)
```
- vmess2sub.py
```
usage: vmess2sub.py [-h] [-l LINK] [-t {v2rayN,sr}] CONF OUTPUT

generate vmess links from v2rayN configuration file

positional arguments:
  CONF                  v2rayN configration file
  OUTPUT                HTML file for subscription

optional arguments:
  -h, --help            show this help message and exit
  -l LINK, --link LINK  file to store vmess links (default: STDOUT)
  -t {v2rayN,sr}        type of vmess link (default: v2rayN)
```
- sub2srlink.py
```
usage: sub2srlink.py [-h] LINK

generate link for subscription in ShadowRocket

positional arguments:
  LINK        url of the html file, e.g.:
              http://admin:password@example.com/v2ray.html

optional arguments:
  -h, --help    show this help message and exit
  -l, --label   a label to distinguish different subscription links served on the same server
```

### Liscense
GPL3.0
