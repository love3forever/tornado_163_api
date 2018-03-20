#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/19
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from data_collector.data_parser import (parse_index_data, parse_song_detail, parse_lyric_data,
                                        parse_playlist_data, parse_playlist_comment, parse_song_comments,
                                        parse_user_follows, parse_user_followed, parse_user_playlist,
                                        parse_user_index_page, parse_artist_index_page, parse_artist_album,
                                        parse_album_detail, parse_album_comments)


async def tester(loop):
    # data = await asyncio.ensure_future(parse_index_data())
    # print('index page content: {}'.format(data))
    #
    # playlist_data = await asyncio.ensure_future(parse_playlist_data(1))
    # print('playlist data: {}'.format(playlist_data))
    #
    # song_data = await asyncio.ensure_future(parse_song_detail(108390))
    # print('song data: {}'.format(song_data))
    #
    # lyric_data = await asyncio.ensure_future(parse_lyric_data(108390))
    # print('lyric data:{}'.format(lyric_data))
    #
    # playlist_comment_data = await asyncio.ensure_future(parse_playlist_comment(2))
    # print('playlist comments:{}'.format(playlist_comment_data))
    #
    # # 测试LRU_CACED是否起作用
    # playlist_comment_data2 = await asyncio.ensure_future(parse_playlist_comment(2))
    # print('playlist comments2:{}'.format(playlist_comment_data2))
    #
    # song_comment_data = await asyncio.ensure_future(parse_song_comments(108390))
    # print('song comments:{}'.format(song_comment_data))
    #
    # user_follows_data = await asyncio.ensure_future(parse_user_follows(77159064))
    # print('user_follows_data:{}'.format(user_follows_data))
    #
    # user_followed_data = await asyncio.ensure_future(parse_user_followed(77159064))
    # print('user followed by:{}'.format(user_followed_data))

    # user_playlist_data = await  asyncio.ensure_future(parse_user_playlist(77159064))
    # print('user playlist:{}'.format(user_playlist_data))

    user_index_page1 = asyncio.ensure_future(parse_user_index_page(77159064))
    user_index_page2 = asyncio.ensure_future(parse_user_index_page(77159064))
    user_index_page3 = asyncio.ensure_future(parse_user_index_page(77159064))
    print('user index page1:{}'.format(await user_index_page1))
    print('user index page2:{}'.format(await user_index_page2))
    print('user index page3:{}'.format(await user_index_page3))

    # artist_index_page = await asyncio.ensure_future(parse_artist_index_page(2738))
    # print('artist index page:{}'.format(artist_index_page))

    # artist_album_data = await asyncio.ensure_future(parse_artist_album(2738))
    # print('artist album data:{}'.format(artist_album_data))

    # album_detail_data = await asyncio.ensure_future(parse_album_detail(37886134))
    # print('album data:{}'.format(album_detail_data))

    # album_comments_data = await asyncio.ensure_future(parse_album_comments(37886134))
    # print('album comments:{}'.format(album_comments_data))

    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tester(loop))
