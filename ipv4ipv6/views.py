#-*- coding: utf-8 -*-

import json
from netaddr import IPAddress
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    return {}


@view_config(route_name='get_version')
def get_version(request):
    func = request.GET.get('func', '')
    remote_addr = IPAddress(request.remote_addr)
    data = {
        'address': remote_addr.format(),
        'version': remote_addr.version,
        'ipv4_mapped': remote_addr.is_ipv4_mapped(),
    }
    return Response(
            body='%s(%s);' % (func, json.dumps(data)),
            content_type='text/javascript')
