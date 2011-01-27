import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lr.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PolicyController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('policy', 'policy')

    def index(self, format='html'):
        """GET /policy: All items in the collection"""
        import urllib2, json, time, os
        url = 'http://localhost:5984/node/policy'
        response = urllib2.urlopen(url)
        data = json.load(response)
        data['timestamp'] = time.asctime()
        return json.dumps(data)
        # url('policy')

    def create(self):
        """POST /policy: Create a new item"""
        # url('policy')

    def new(self, format='html'):
        """GET /policy/new: Form to create a new item"""
        # url('new_policy')

    def update(self, id):
        """PUT /policy/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('policy', id=ID),
        #           method='put')
        # url('policy', id=ID)

    def delete(self, id):
        """DELETE /policy/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('policy', id=ID),
        #           method='delete')
        # url('policy', id=ID)

    def show(self, id, format='html'):
        """GET /policy/id: Show a specific item"""
        # url('policy', id=ID)

    def edit(self, id, format='html'):
        """GET /policy/id/edit: Form to edit an existing item"""
        # url('edit_policy', id=ID)