import argparse
import re
import asyncio
import json
from aiohttp import web

async def scan(ip):
    process = await asyncio.create_subprocess_exec('nmap', '-sV', ip, stdout=asyncio.subprocess.PIPE)
    stdout, _ = await process.communicate()
    result = stdout.decode().strip()
    return result

async def handle(request):
    ip_scan = request.match_info.get('toScan', "127.0.0.1")
    to_return = ''
    to_return += await scan(ip_scan)
    return web.Response(text=str(to_return))

def main():
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('ipServer', help='HTTP Server IP')
    parser.add_argument('port', type=int, help='Listening port for HTTP Server')

    args = parser.parse_args()
    app = web.Application()
    app.router.add_get('/', lambda e: handle(e))
    web.run_app(app, port=(args.port), host=args.ipServer)

if __name__ == '__main__':
    main()

    #py ipmap1.py 127.0.0.1 8080