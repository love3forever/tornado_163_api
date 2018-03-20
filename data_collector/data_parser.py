#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/19
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

from datetime import datetime
import json
from bs4 import BeautifulSoup

from .data_product import get, post
from .post_data_map import (get_playlist_comments_param, follow_and_fans_data, get_user_playlist_param,
                            album_comments)
from .encrypter import encrypted_request
from data_collector import url_map
import asyncio


def mapper_index_recommend_list(data):
    # 将推荐列表信息转为数组
    if data:
        # 获取歌单图片链接
        img = data.select('img')[0]['src']
        # 获取歌单链接和名称
        play_list_url = data.find_all('a', class_='msk')[0]['href']
        play_list_title = data.find_all('a', class_='msk')[0]['title']
        play_list_id = data.find_all('a', class_='msk')[0]['data-res-id']
        play_count = data.find_all('span', class_='nb')[0].string
        play_list_type = 'djradio' if 'dj' in play_list_url else 'playlist'

        return {
            'img': img,
            'playlistURL': host_url.format(play_list_url),
            'playlistTitle': play_list_title,
            'playTimes': play_count,
            'playlistID': play_list_id,
            'type': play_list_type
        }
    else:
        return None


async def parse_index_data():
    # 获取首页信息
    index_data = await get(url_map.index_url, content_type='text')
    index_content = index_data
    index_soup = BeautifulSoup(index_content, 'lxml')
    index_response = {}
    cvr_list = index_soup.find_all('ul', class_='m-cvrlst f-cb')
    # 获取推荐歌单列表
    if cvr_list:
        hottest_recommend_lis = cvr_list[0].select('li')
        recommend_data = map(mapper_index_recommend_list,
                             hottest_recommend_lis)
        index_response['recommendList'] = recommend_data
    else:
        print('no recommendList found')
        index_response['recommendList'] = None
    # 获取热门DJ列表
    hotdj_list = index_soup.select("#hotdj-list > li")
    if hotdj_list:
        hotdj_data_list = []
        for dj_li in hotdj_list:
            hotdj_data = {}
            dj_img = dj_li.select('img')[0]['src']
            dj_info = dj_li.select('.info > p')
            dj_link = dj_info[0].select('a')[0]['href']
            dj_name = dj_info[0].select('a')[0].string
            dj_desc = dj_info[1].string
            hotdj_data['img'] = dj_img
            hotdj_data['href'] = dj_link
            hotdj_data['name'] = dj_name
            hotdj_data['desc'] = dj_desc
            hotdj_data_list.append(hotdj_data)
        index_response['hotdj'] = hotdj_data_list
    else:
        print('no dj list data')
        index_response['hotdj'] = None
    # 获取榜单列表
    blk_list = index_soup.select('.blk')
    if blk_list:
        filted_blk = filter(lambda x: len(x.select('.top')) != 0, blk_list)
        blk_data_list = []
        for item in filted_blk:
            blk_data = {}
            blk_img = item.select('.cver > img')[0]['data-src']
            blk_href = item.select('.cver > a')[0]['href']
            blk_title = item.select('.cver > a')[0]['title']
            blk_data['img'] = blk_img
            blk_data['href'] = blk_href
            blk_data['title'] = blk_title

            blk_song_list = item.select('dd > ol > li')
            blk_songs = []
            if blk_song_list:
                for blk_song in blk_song_list:
                    blk_song_data = {}
                    blk_song_data['songName'] = blk_song.select('a')[0][
                        'title']
                    blk_song_data['songHref'] = blk_song.select('a')[0][
                        'href']
                    blk_songs.append(blk_song_data)
            blk_data['songs'] = blk_songs

            blk_data['more'] = item.select('.more > a')[0]['href']

            blk_data_list.append(blk_data)
        index_response['blk'] = blk_data_list
    else:
        print('no blk data')
        index_response['blk'] = None
    # 获取最新入驻歌手信息
    singer_list = index_soup.select('#singer-list > li')
    if singer_list:
        singer_data_list = []
        for singer in singer_list:
            singer_data = {}
            singer_data['href'] = singer.select('a')[0]['href']
            singer_data['img'] = singer.select('img')[0]['src']
            singer_data['name'] = singer.select('h4 > span')[0].string
            singer_data['desc'] = singer.select('p')[0].string
            singer_data_list.append(singer_data)
        index_response['newSinger'] = singer_data_list
    else:
        print('no singer data')
        index_response['newSinger'] = None
    # 获取最新专辑列表
    album_list = index_soup.select('.roll > ul')
    if album_list:
        album_data_list = []
        album_li_list = []
        album_li_list.extend(album_list[0].select('li'))
        album_li_list.extend(album_list[1].select('li'))
        for album_li in album_li_list:
            album_data = {}
            album_data['img'] = album_li.select('img')[0]['data-src']
            album_data['href'] = album_li.select('.f-thide > a')[0]['href']
            album_data['title'] = album_li.select('.f-thide > a')[0]['title']
            album_data['artistName'] = album_li.select('.s-fc3')[0].string
            album_data['artistHref'] = album_li.select('.tit > a')[0]['href']
            album_data_list.append(album_data)
        index_response['newAlbum'] = album_data_list
    else:
        print('no album data')
        index_response['newAlbum'] = None
    return index_response


async def parse_playlist_data(playlist_id=None):
    # 获取歌单数据
    url = url_map.playlist_detail_url.format(playlist_id)
    playlist_data = await get(url)
    return playlist_data


async def parse_playlist_comment(playlist_id=None, page=1):
    # 获取歌单评论
    url = url_map.playlist_comments_url.format(playlist_id)
    post_param = get_playlist_comments_param(playlist_id)
    post_param['offset'] = str((page - 1) * 20)
    post_param['limit'] = str(20)
    encrtyed_param = encrypted_request(json.dumps(post_param))
    playlist_comments_data = await post(url, data=encrtyed_param, content_type='text')
    return playlist_comments_data


async def parse_song_detail(song_id=None):
    # 获取歌曲详情
    url = url_map.song_detail_url.format(song_id)
    song_data = await get(url, content_type='text')
    return json.loads(song_data)


async def parse_song_comments(song_id, page=1):
    # 获取歌曲评论数据
    url = url_map.song_comments_url.format(song_id, song_id, 20 * (page - 1))
    song_comments_data = await get(url, content_type='text')
    return song_comments_data


def convert_lyric(lyric):
    if lyric:
        lyric_data = lyric.split('\n')
        lyric_pure = [x[10:] for x in lyric_data[1:]]
        lyric_result = '\n'.join(lyric_pure)
        return lyric_result
    else:
        return None


async def parse_lyric_data(song_id):
    # 获取歌词数据
    url = url_map.song_lyric_url.format(song_id)
    response_data = await get(url, content_type='text')
    lyric_data = json.loads(response_data)
    if lyric_data:
        # 修改歌词和翻译歌词
        try:
            lyric = lyric_data['lrc']['lyric']
        except Exception as e:
            print(str(e))
        else:
            lyric_str = convert_lyric(lyric)
            lyric_data['lrc']['lyric'] = lyric_str

        try:
            tlyric = lyric_data['tlyric']['lyric']
        except Exception as e:
            print(str(e))
        else:
            tlyric_str = convert_lyric(tlyric)
            lyric_data['tlyric']['lyric'] = tlyric_str
        return lyric_data
    else:
        return None


async def parse_user_follows(user_id, page=1):
    # 获取用户关注数据
    url = url_map.user_follows_url.format(user_id)
    post_data = follow_and_fans_data
    post_data['userId'] = user_id
    post_data['limit'] = 20
    post_data['offset'] = (page - 1) * post_data['limit']
    encrtyed_param = encrypted_request(json.dumps(post_data))
    user_follows_data = await post(url, data=encrtyed_param, content_type='text')
    return json.loads(user_follows_data)


async def parse_user_followed(user_id, page=1):
    # 获取用户粉丝数据
    url = url_map.user_fans_url.format(user_id)
    post_data = follow_and_fans_data
    post_data['userId'] = user_id
    post_data['limit'] = 20
    post_data['offset'] = (page - 1) * post_data['limit']
    encrtyed_param = encrypted_request(json.dumps(post_data))
    user_followed_data = await post(url, data=encrtyed_param, content_type='text')
    return json.loads(user_followed_data)


async def parse_user_playlist(user_id, page=1):
    # 获取用户歌单
    post_data = get_user_playlist_param(user_id)
    post_data['offset'] = (page - 1) * 36
    encrypted_param = encrypted_request(json.dumps(post_data))
    user_playlist_data = await post(url_map.user_playlist_url, data=encrypted_param)
    user_playlist_data = user_playlist_data['playlist']
    if user_playlist_data:
        user_playlist_result = {
            'own': [],
            'other': []
        }
        creator = None
        for playlist in user_playlist_data:
            convert_data = {
                'name': playlist['name'],
                'playCount': playlist['playCount'],
                'playlistId': playlist['id'],
                'coverImgUrl': playlist['coverImgUrl']
            }
            if str(playlist['userId']) == str(user_id):
                user_playlist_result['own'].append(convert_data)
                if not creator:
                    creator = playlist['creator']['nickname']
            else:
                user_playlist_result['other'].append(convert_data)

        return user_playlist_result, creator
    else:
        return None


async def parse_user_index_page(user_id):
    # 解析用户首页数据
    index_url = url_map.user_index_url.format(user_id)
    index_data = await get(index_url, content_type='text')
    if index_data:
        index_content = index_data
        index_soup = BeautifulSoup(index_content, 'lxml')
        index_box = index_soup.select('#head-box')[0]
        index_data = {}
        img_tag = index_box.select('#ava > img')
        if len(img_tag):
            index_data.setdefault(
                'img', img_tag[0]['src'])
        wrapper_tag = index_box.select('#j-name-wrap')
        if len(wrapper_tag):
            index_name_wrapper = wrapper_tag[0]
            index_name = index_name_wrapper.select('.tit')[0].string
            index_data.setdefault('name', index_name)
            index_level = index_name_wrapper.select('.lev')[0].next
            index_data.setdefault('level', index_level)
            genders = {
                "u-icn-00": "unknown",
                "u-icn-01": "male",
                "u-icn-02": "female"
            }
            index_gender = ''
            for item in genders.keys():
                if len(index_name_wrapper.select('.{}'.format(item))):
                    index_gender = genders[item]
                    break
            index_data.setdefault('gender', index_gender)
        events_tag = index_box.select('#event_count')
        if len(events_tag):
            index_events = events_tag[0].string
            index_data.setdefault('events', index_events)
        follow_tag = index_box.select('#follow_count')
        if len(follow_tag):
            index_follows = follow_tag[0].string
            index_data.setdefault('follows', index_follows)
        fans_tag = index_box.select('#fan_count')
        if len(fans_tag):
            index_fans = index_box.select('#fan_count')[0].string
            index_data.setdefault('fans', index_fans)
        age_tag = index_box.select('#age')
        if len(age_tag):
            index_location = age_tag[0]
            location_tag = index_location.find_previous_siblings("span")
            if len(location_tag):
                index_location_detail = location_tag[0].string
                index_data.setdefault('location', index_location_detail)
        networks_tag = index_box.select('.u-logo')
        if len(networks_tag):
            index_networks = networks_tag[0]
            index_social_networks = {}
            for item in index_networks.select('li > a'):
                index_social_networks.setdefault(item['title'], item['href'])
            index_data.setdefault('social_networks', index_social_networks)
        return index_data
    else:
        return None


async def parse_artist_index_page(artist_id):
    # 获取歌手首页数据
    index_url = url_map.artist_index_url.format(artist_id)
    index_data = await get(index_url, content_type='text')
    index_info = {}
    if index_data:
        index_soup = BeautifulSoup(index_data, 'lxml')
        top_50_songs = index_soup.select('#song-list-pre-cache > textarea')
        if top_50_songs:
            songs = top_50_songs[0].string
            index_info.setdefault('top50', json.loads(songs))
        pic_info = index_soup.select('.n-artist > img')
        index_info.setdefault('img', pic_info[0]['src'] or None)
        try:
            artist_name = index_soup.select('#artist-name')[0].string
            artist_alias = index_soup.select('#artist-alias')[0].string
        except Exception as e:
            print(str(e))
        else:
            index_info.setdefault('artist_name', artist_name)
            index_info.setdefault('artist_alias', artist_alias)
        return index_info
    else:
        return None


async def parse_artist_album(artist_id):
    # 获取歌手相关专辑
    album_url = url_map.artist_album_url.format(artist_id)
    album_data = await get(album_url, content_type='text')
    if album_data:
        album_soup = BeautifulSoup(album_data, 'lxml')
        album_list = album_soup.select('ul[id="m-song-module"] > li')
        album_result = []
        for album in album_list:
            img = album.select('img')[0]
            img_url = img['src']
            title = album.select('.s-fc0')[0].string
            time = album.select('.s-fc3')[0].string
            album_id = album.select('.s-fc0')[0]['href'][10:]
            album_info = {
                'img': img_url,
                'name': title,
                'time': time,
                'id': album_id
            }
            album_result.append(album_info)
        return album_result
    else:
        return None


async def parse_album_detail(album_id):
    # 获取专辑信息
    album_url = url_map.album_detail_url.format(album_id)
    album_data = await get(album_url, content_type='text')
    if album_data:
        album_soup = BeautifulSoup(album_data, 'lxml')
        song_list = album_soup.select('#song-list-pre-cache > textarea')
        song_desc_all = album_soup.select('#album-desc-more > .f-brk')
        if len(song_desc_all) == 0:
            song_desc_all = album_soup.select('.n-albdesc > .f-brk')
        album_desc = ' '.join([x.string for x in song_desc_all])
        album_blk = album_soup.select('.topblk > .intr')
        album_singer = album_blk[0].select('a')[0]
        album_singer_name = album_singer.string
        album_singer_id = album_singer['href'][11:]
        album_publish_time = album_blk[1].select('b')[0].next_sibling
        album_publish_company = album_blk[2].select('b')[0].next_sibling
        if song_list:
            detail_data = json.loads(song_list[0].string)
            result_data = detail_data[0]['album']
            result_data.setdefault('alias', detail_data[0]['alias'])
            for item in detail_data:
                del item['album']
                del item['alias']
            result_data.setdefault('songs', detail_data)
            result_data.setdefault('singer', album_singer_name)
            result_data.setdefault('singer_id', album_singer_id)
            result_data.setdefault('publish_time', album_publish_time)
            result_data.setdefault('publish_company', album_publish_company)
            result_data.setdefault('desc', album_desc)
            return result_data
        else:
            return None
    else:
        return None


async def parse_album_comments(album_id, page=1):
    # 获取专辑评论信息
    url = url_map.album_comments_url.format(album_id)
    post_data = album_comments
    post_data['rid'] = post_data['rid'].format(album_id)
    post_data['offset'] = (page - 1) * post_data['limit']
    encrypted_param = encrypted_request(json.dumps(post_data))
    album_comments_data = await post(url, data=encrypted_param, content_type='text')
    if album_comments_data:
        return json.loads(album_comments_data)
    return None
