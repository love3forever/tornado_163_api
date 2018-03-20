#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
import asyncio
from tornado import web

from data_collector.data_parser import (parse_user_index_page, parse_user_playlist, parse_user_followed,
                                        parse_user_follows)


class UserIndexHandler(web.RequestHandler):
    async def get(self, user_id):
        try:
            user_index_data = await asyncio.ensure_future(parse_user_index_page(user_id))
        except:
            self.send_error(status_code=500, reason="server error")
        else:
            if not user_index_data:
                self.send_error(404)
            response = {
                'user': user_id,
                'code': 200,
                'detail': user_index_data
            }
            self.write(response)


class UserFollowsHandler(web.RequestHandler):
    async def get(self, user_id, page=1):
        try:
            user_follows_data = await asyncio.ensure_future(parse_user_follows(user_id, page=int(page)))
        except:
            self.send_error()
        else:
            if not user_follows_data:
                self.send_error(404)
            response = {
                'user': user_id,
                'follows': user_follows_data['follow'],
                'code': 200
            }
        self.write(response)


class UserFollowedHandler(web.RequestHandler):
    async def get(self, user_id, page=1):
        try:
            user_followed_data = await asyncio.ensure_future(parse_user_followed(user_id, page=int(page)))
        except:
            self.send_error()
        else:
            response = {
                'user': user_id,
                'follows': user_followed_data['followeds'],
                'code': 200
            }
            self.write(response)


class UserPlaylistHandler(web.RequestHandler):
    async def get(self, user_id):
        try:
            creator, user_playlist_data = await asyncio.ensure_future(parse_user_playlist(user_id))
        except:
            self.send_error()
        else:
            response = {
                'user': user_id,
                'nickname': creator,
                'playlist': user_playlist_data,
                'code': 200
            }
            self.write(response)
