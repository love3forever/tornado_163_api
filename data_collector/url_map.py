#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/19
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

host_url = 'https://music.163.com{}'
index_url = 'https://music.163.com/discover'
playlist_url = 'https://music.163.com/playlist?id={}'
user_index_url = 'http://music.163.com/user/home?id={}'
user_follows_url = 'http://music.163.com/weapi/user/getfollows/{}?csrf_token='
user_fans_url = 'http://music.163.com/weapi/user/getfolloweds?csrf_token='
user_playlist_url = 'http://music.163.com/weapi/user/playlist?csrf_token='
user_playrecord_url = 'http://music.163.com/weapi/v1/play/record?csrf_token='
playlist_comments_url = 'https://music.163.com/weapi/v1/resource/comments/A_PL_0_{}?csrf_token='
playlist_detail_url = 'http://music.163.com/api/playlist/detail?id={}'
song_comments_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}/?rid=R_SO_4_{}&offset={}&total=true&limit=20'
song_detail_url = 'http://music.163.com/api/song/detail?ids=[{}]'
song_lyric_url = 'http://music.163.com/api/song/lyric?id={}&lv=-1&tv=-1'
artist_index_url = 'http://music.163.com/artist?id={}'
artist_album_url = 'http://music.163.com/artist/album?id={}&limit=200'
album_detail_url = 'http://music.163.com/album?id={}'
album_comments_url = 'http://music.163.com/weapi/v1/resource/comments/R_AL_3_{}'
djradio_comments_url = 'http://music.163.com/weapi/v1/resource/comments/A_DJ_1_{}?csrf_token='
djradio_detail_url = 'http://music.163.com/dj?id={}'