# v2ray subscription toolbox

This toolbox contains two python scripts to generate files that can be used in [v2rayN](https://github.com/2dust/v2rayN) to subscribe [v2ray](https://github.com/v2ray) servers. It follows the format introduced in [v2rayN wiki](https://github.com/2dust/v2rayN/wiki/%E5%88%86%E4%BA%AB%E9%93%BE%E6%8E%A5%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E(ver-2)). It only supports http\websocket\kcp\http2 but not quic.

### Requirement
- python3
- urllib

### Tutorial
1. Prepare the configuration files of your v2ray servers, for example `config.json` and `config2.json`. Put them in the same folder of these python scripts
2. Run the follwing commands to generate v2rayN format configuration file
```bash
python3 conf2vmess.py -c config.json -s example.com -p 443 -o vmess.json
python3 conf2vmess.py -c config2.json -s example.com -p 443 >> vmess.json
#(For windows user, replace the second one by `python3 conf2vmess.py -c config2.json -s example.com -p 443 | out-file -Append -FilePath vmess.json -encoding UTF8`)
```
3. Edit `vmess.json` manually to correct redundant square bracket, and also add unique labels to the `ps` field of each server if you want.
4. Run the following command to generate html file `vmess.html` and `vmess.lnk`
```bash
python3 vmess2sub.py vmess.json vmess.html -l vmess.lnk
```
5. You can now upload `vmess.html` to the root of your `www` folder and use `http://example.com/vmess.html` as the subscription link. Or, you can directly use the `vmess://***` links in `vmess.lnk` file.


### Usage
- conf2vmess.py
```
usage: conf2vmess.py [-h] [-c CONFIG] [-s SERVER] [-p PORT [PORT ...]]
                     [-o OUTPUT]

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
                        current host 184.184.115.53)
  -p PORT [PORT ...], --port PORT [PORT ...]
                        ports that v2ray server listens to (default: the ones
                        defined in configuration file)
  -o OUTPUT, --output OUTPUT
                        name of v2rayN format configuration file (default:
                        STDOUT)
```
- vmess2sub.py
```
usage: vmess2sub.py [-h] [-l LINK] CONF OUTPUT

generate html file from v2rayN configuration file

positional arguments:
  CONF                  v2rayN configration file
  OUTPUT                HTML file for subscription

optional arguments:
  -h, --help            show this help message and exit
  -l LINK, --link LINK  file to store vmess links (default: STDOUT)
```

### Liscense
GPL3.0