from django.conf import settings
from stravalib import Client
import requests


class StravaClient(object):
    """
    Object used to access Strava API
    """
    
    def get_token(self, client_id, client_secret, redirect_uri, code):
        client = Client()
        #data = {"client_id": client_id, "client_secret": client_secret, "code": code}
        #TODO: suprask šitą
        url = client.authorization_url(client_id=client_id,
                               redirect_uri=redirect_uri)
        
        token_response = client.exchange_code_for_token(client_id=client_id,
                                              client_secret=client_secret,
                                              code=code)
        access_token = token_response['access_token']
        refresh_token = token_response['refresh_token']  # You'll need this in 6 hours
        
        #r = requests.post("%s/oauth/token" % self.api_endpoint, data=data)

                
        # TODO: Error handling 
        #response = r.json()
        
        return access_token


