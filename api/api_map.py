#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

from api.user_handler import (UserIndexHandler, UserFollowsHandler, UserFollowedHandler,
                              UserPlaylistHandler)
from api.song_handler import (SongCommnetsHandler, SongDetailHanlder, SongLyricHandler)
from api.playlist_handler import (PlayelistDetailHandler, PlaylistCommentsHandler)
from api.album_handler import (AlbumCommentsHandler, AlbumDetailHandler)
from api.artist_handler import (ArtistAlbumHandler, ArtistDetailHandler)

user_api_map = [
    (r"/api/v1/user/(?P<user_id>.*)/detail", UserIndexHandler),
    (r"/api/v1/user/(?P<user_id>.*)/follows/page/(?P<page>.*)", UserFollowsHandler),
    (r"/api/v1/user/(?P<user_id>.*)/fans/page/(?P<page>.*)", UserFollowedHandler),
    (r"/api/v1/user/(?P<user_id>.*)/playlist", UserPlaylistHandler),
]

song_api_map = [
    (r"/api/v1/song/(?P<song_id>.*)/detail", SongDetailHanlder),
    (r"/api/v1/song/(?P<song_id>.*)/comments/(?P<page>.*)", SongCommnetsHandler),
    (r"/api/v1/song/(?P<song_id>.*)/lyrics", SongLyricHandler)
]

playlist_api_map = [
    (r"/api/v1/playlist/(?P<playlist_id>.*)/detail", PlayelistDetailHandler),
    (r"/api/v1/playlist/(?P<playlist_id>.*)/comments/(?P<page>.*)", PlaylistCommentsHandler),
]

album_api_map = [
    (r"/api/v1/album/(?P<album_id>.*)/detail", AlbumDetailHandler),
    (r"/api/v1/album/(?P<album_id>.*)/comments/(?P<page>.*)", AlbumCommentsHandler),
]

artist_api_map = [
    (r"/api/v1/artist/(?P<artist_id>.*)/detail", ArtistDetailHandler),
    (r"/api/v1/artist/(?P<artist_id>.*)/albums", ArtistAlbumHandler),
]
