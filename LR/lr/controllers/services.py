#   Copyright 2011 Department of Defence

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lr.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ServicesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('services', 'services')

    def index(self, format='html'):
        """GET /services: All items in the collection"""
        import urllib2, json, time, os
        url = 'http://localhost:5984/node/services'
        response = urllib2.urlopen(url)
        data = json.load(response)
        data['timestamp'] = time.asctime()
        return json.dumps(data)
        # url('services')

    def create(self):
        """POST /services: Create a new item"""
        # url('services')

    def new(self, format='html'):
        """GET /services/new: Form to create a new item"""
        # url('new_services')

    def update(self, id):
        """PUT /services/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('services', id=ID),
        #           method='put')
        # url('services', id=ID)

    def delete(self, id):
        """DELETE /services/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('services', id=ID),
        #           method='delete')
        # url('services', id=ID)

    def show(self, id, format='html'):
        """GET /services/id: Show a specific item"""
        # url('services', id=ID)

    def edit(self, id, format='html'):
        """GET /services/id/edit: Form to edit an existing item"""
        # url('edit_services', id=ID)
