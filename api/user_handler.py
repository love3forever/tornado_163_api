#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
import asyncio
from tornado import web

from data_collector.data_parser import (parse_user_index_page, parse_user_playlist, parse_user_followed,
                                        parse_user_follows)
from api.helper import common_parse


class UserIndexHandler(web.RequestHandler):
    async def get(self, user_id):
        await common_parse(self, parse_user_index_page, user_id)


class UserFollowsHandler(web.RequestHandler):
    async def get(self, user_id, page=1):
        await common_parse(self, parse_user_follows, user_id, page=int(page))


class UserFollowedHandler(web.RequestHandler):
    async def get(self, user_id, page=1):
        await common_parse(self, parse_user_followed, user_id, page=int(page))


class UserPlaylistHandler(web.RequestHandler):
    async def get(self, user_id):
        await common_parse(self, parse_user_playlist, user_id)
