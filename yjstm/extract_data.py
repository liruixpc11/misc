# coding=UTF-8

import csv
import types
import jinja2

import cnsort


def write_php(f, var_name, data):
    result = ['$' + var_name + ' = array(']
    if isinstance(data, (types.ListType, types.TupleType)):
        for entry in cnsort.cn_sort(data):
            result.append('    "' + str(entry) + '",')
    elif isinstance(data, types.DictType):
        for entry in cnsort.cn_sort(data.keys()):
            result.append('    "' + str(entry) + '" => array(')
            for item in cnsort.cn_sort(data[entry]):
                result.append('        "' + str(item) + '",')
            result.append('    ),')
    else:
        raise Exception("unknown type " + str(type(data)))
    result.append(');')
    f.write('\n'.join(result))
    f.write('\n\n')


def write_js(f, var_name, data):
    if isinstance(data, (types.ListType, types.TupleType)):
        result = ['' + var_name + ' = [']
        for i, entry in enumerate(cnsort.cn_sort(data)):
            result.append('    "' + str(entry) + '"' + ('' if i + 1 == len(data) else ','))
        result.append('];')
    elif isinstance(data, types.DictType):
        result = ['' + var_name + ' = {']
        for i, entry in enumerate(cnsort.cn_sort(data.keys())):
            result.append('    "' + str(entry) + '": [')
            for j, item in enumerate(cnsort.cn_sort(data[entry])):
                result.append('        "' + str(item) + '"' + ('' if j + 1 == len(data[entry]) else ','))
            result.append('    ]' + ('' if i + 1 == len(data) else ','))
        result.append('};')
    else:
        raise Exception("unknown type " + str(type(data)))
    f.write('\n'.join(result))
    f.write('\n\n')


def read_ieu_data(filename):
    result = dict()
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=';')
        first = True
        for row in reader:
            if first:
                first = False
                continue
            major = item_string(row[5]) + "-" + item_string(row[6])
            direction = item_string(row[8]) + "-" + item_string(row[9])
            if major in result:
                result[major].append(direction)
            else:
                result[major] = [direction]
    return result


def item_string(item):
    return item.decode('GBK').encode('UTF-8').strip()


def read_items(filename, index=-1, converter=None):
    result = []
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=';')
        first = True
        for row in reader:
            if first:
                first = False
                continue
            if not converter:
                item = row[index].decode('GBK').encode('UTF-8').strip()
                result.append(item)
            else:
                result.append(converter(row))
    return result



if __name__ == '__main__':
    php = open("/Users/lirui/PhpstormProjects/XDZS/yjstm-web/schoolData.inc.php", 'wb')
    php.write("<?php\n")
    js = open("/Users/lirui/PhpstormProjects/XDZS/yjstm-web/assets/schoolData.js", 'wb')

    data = read_ieu_data("/Users/lirui/PhpstormProjects/XDZS/data/20150914/123.csv")
    write_php(php, "ieuMajorList", data)
    write_js(js, "ieuMajorList", data)

    data = read_items("/Users/lirui/PhpstormProjects/XDZS/data/20150914/1234.csv", 1)
    write_php(php, "schoolList", data)
    write_js(js, "schoolList", data)

    data = read_items("/Users/lirui/PhpstormProjects/XDZS/data/20150914/12345.csv", 5)
    write_php(php, "majorList", data)
    write_js(js, "majorList", data)

    php.close()
    js.close()
