#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
import asyncio
from itertools import chain

from tornado import web, httpserver
from tornado.options import define, options, parse_command_line
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado import ioloop

from api.origin_handler import OriginHanlder, OriginTestHandler
from api.api_map import (user_api_map, song_api_map, playlist_api_map,
                         album_api_map, artist_api_map)

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


def main():
    parse_command_line()

    AsyncIOMainLoop().install()
    app = web.Application(
        chain(user_api_map, song_api_map, playlist_api_map, album_api_map, artist_api_map),
        debug=options.debug,
    )
    app.listen(options.port)
    asyncio.get_event_loop().run_forever()


def origin_main():
    parse_command_line()
    app = web.Application(
        [
            (r"/", OriginHanlder),
            (r"/test", OriginTestHandler)
        ],
        debug=options.debug,
    )
    app.listen(options.port)
    ioloop.IOLoop.current().start()
