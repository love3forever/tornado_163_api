#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/19
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
import aiohttp
import async_timeout

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'
accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
connection = "keep-alive"
cache_control = "no-cache"
upgrade_insecure_requests = 1
host = 'music.163.com'
headers = {
    'User-Agent': agent,
    'Host': host,
    'Accept': accept,
    'Cache-Control': cache_control,
    'Connection': connection,
}

post_headers = {
    'User-Agent': agent,
    'Host': host,
    'Accept': accept,
    'Cache-Control': cache_control,
    'Connection': connection,
    'Content-Type': 'application/x-www-form-urlencoded'
}


async def get(url, content_type='json'):
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(5):
            async with session.get(url, headers=headers) as response:
                if content_type == 'json':
                    return await response.json()
                if content_type == 'text':
                    return await response.text()


async def post(url, data, content_type='json'):
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(5):
            post_data = aiohttp.FormData()
            for k, v in data.items():
                post_data.add_field(k, v)
            async with session.post(url, data=post_data, headers=post_headers) as response:
                if content_type == 'json':
                    return await response.json()
                if content_type == 'text':
                    return await response.text()
