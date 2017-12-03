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