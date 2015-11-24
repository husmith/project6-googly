#########################
#  Self-test invoked when module is run
#  as main program.
#########################
import main
from apiclient.discovery import build
from apiclient.http import HttpMock
import unittest
import nose.tools
import flask
import json
import pprint
#Bc_g0STIUXoBScCQl5k6MEc3
#calendarId=,singleEvents=True,timeMin=,timeMax=)

class TestApp(unittest.TestCase):

    def setUp(self):
        self.api_key = '166149220767-qnfht3ffmi3ub2pejchcas5p85qildsu.apps.googleusercontent.com'
        self.service = build('calendar', 'v3', developerKey='166149220767-qnfht3ffmi3ub2pejchcas5p85qildsu.apps.googleusercontent.com')

    def testGetCalendarList(self):
        # api_key = '166149220767-qnfht3ffmi3ub2pejchcas5p85qildsu.apps.googleusercontent.com'
        # service = build('calendar', 'v3', developerKey='166149220767-qnfht3ffmi3ub2pejchcas5p85qildsu.apps.googleusercontent.com')
        request = self.service.calendarList().list()
        http = HttpMock('calendar_ids.json', {'status': '200'})
        response = request.execute(http=http)
        self.assertEqual(len(response["items"]),3)
        # events = service.events().list(calendarId=cal,singleEvents=True,timeMin=flask.session['begin_date'],timeMax=flask.session['end_date']).execute()

    def testGetEventList(self):
        request = self.service.events().list(calendarId='primary',singleEvents=True,timeMin=flask.session['begin_date'],timeMax=flask.session['end_date']).execute()

if __name__ == '__main__':
    unittest.main()
