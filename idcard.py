# -*- encoding: utf-8 -*-
"""
@date: 2020/12/24 10:38 下午
@author: xuehuiping
"""

# 代码清单9-4
# 身份证字段匹配

import re
import datetime


class Matcher(object):
    def __init__(self, str_regex, fields):
        self.regex = re.compile(str_regex)
        if not isinstance(fields, list):
            fields = [fields]
        self.fields = fields
        self.matched = False

    def match(self, line):
        m = self.regex.match(line)
        if m:
            self.matched = True
            groups = [m.group(i + 1) for i in range(len(self.fields))]
        else:
            groups = [None] * len(self.fields)
        return zip(self.fields, groups)


MATCHERS = [
    Matcher('姓名(.+)', 'name'),
    Matcher('性别([男女])民族(.+)', ['sex', 'ethnicity']),
    Matcher('出生([0-9]{4})年([0-9]{1,2})月([0-9]{1,2})日', ['y', 'm', 'd']),
    Matcher('住址(.+)', 'address'),
    Matcher('公民身份号码([0-9X]{18})', 'id_number')
]


def format_date(y, m, d):
    if y and m and d:
        try:
            date = datetime.date(int(y), int(m), int(d))
            return date.strftime('%Y%m%d')
        except ValueError:
            return None


def match_idcard(lines):
    rv = {}
    for line in lines:
        for matcher in MATCHERS:
            if not matcher.matched:
                rv.update(matcher.match((line)))
    rv['birthdate'] = format_date(rv.pop('y'), rv.pop('m'), rv.pop('d'))
    return rv


if __name__ == "__main__":
    lines = ["姓名薛会萍", "性别女民族汗", "出生1990年11月13日", "住址北京市海淀区", "公民身份号码142701199001014567"]
    r = match_idcard(lines)
    print (r)
