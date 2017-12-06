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