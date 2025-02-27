#!/usr/bin/python3
import argparse
from sys import exit
from scripts import (
    HTTP,
    FastCGI,
    MySQL,
    PostgreSQL,
    DumpMemcached,
    PHPMemcached,
    PyMemcached,
    RbMemcached,
    Redis,
    SMTP,
    Zabbix,
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--exploit",
    help="http,\n"
    "https,\n"
    "mysql,\n"
    "postgresql,\n"
    "fastcgi,\n"
    "redis,\n"
    "smtp,\n"
    "zabbix,\n"
    "pymemcache,\n"
    "rbmemcache,\n"
    "phpmemcache,\n"
    "dmpmemcache",
)
args = parser.parse_args()


class Colors:
    reset = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"


if __name__ == '__main__':
    print(f"""{Colors.green}
    ________              .__
    /  _____/  ____ ______ |  |__   ___________ __ __  ______
    /   \  ___ /  _ \\____ \|  |  \_/ __ \_  __ \  |  \/  ___/
    \    \_\  (  <_> )  |_> >   Y  \  ___/|  | \/  |  /\___ \\
    \______  /\____/|   __/|___|  /\___  >__|  |____//____  >
            \/       |__|        \/     \/                 \/
{Colors.reset}
\t\t{Colors.blue}author: {Colors.orange}$_SpyD3r_${Colors.reset}
""")

    if not args.exploit:
        parser.print_help()
        exit()

    exploit_map = {
        "http": HTTP.Http,
        "https": HTTP.Http,
        "mysql": MySQL.MySQL,
        "postgresql": PostgreSQL.PostgreSQL,
        "fastcgi": FastCGI.FastCGI,
        "redis": Redis.Redis,
        "smtp": SMTP.SMTP,
        "zabbix": Zabbix.Zabbix,
        "dmpmemcache": DumpMemcached.DumpMemcached,
        "phpmemcache": PHPMemcached.PHPMemcached,
        "rbmemcache": RbMemcached.RbMemcached,
        "pymemcache": PyMemcached.PyMemcached,
    }

    if args.exploit in exploit_map:
        exploit_map[args.exploit]()
    else:
        parser.print_help()
