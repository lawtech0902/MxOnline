# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/3/1 下午8:55'
"""
from .models import CityDict, CourseOrg, Teacher

import xadmin


class CityDicyAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_nums']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums']
    list_filter = ['name', 'desc', 'click_num', 'fav_nums']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums',
                   'add_time']


xadmin.site.register(CityDict, CityDicyAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
