import os
import requests
#import urllib.parse
import json
# from spotify_environment import set_apikey


# set_apikey()


class SpotifyClient():

	def __init__(self, api_token):

		self.api_token = api_token
	


	def search_song(self, query, type ):

		query = f"{query}&type={type}"
		url = f"https://api.spotify.com/v1/search?q={query}"

		headers = {

			"Accept": "application/json", 
			"Content-Type": "application/json", 
			"Authorization": f"Bearer {self.api_token}"


		}


		response = requests.get(url, headers=headers)

		response	= response.json()
		results = response['tracks']['items']

		if results:
			return results[0]['id']
		else:
			raise(f"no track found for {type} = {query} ")


	def create_playlist(self, spotify_id, name, description, public=False):


		headers = {

			"Accept": "application/json", 
			"Content-Type": "application/json", 
			"Authorization": f"Bearer {self.api_token}"


		}

		request_body= {
		"name" :f"{name}",
		"description":f"{description}",
		"public":f"{public}"
		}

		request_body = json.dumps(request_body)

		url = f"https://api.spotify.com/v1/users/{spotify_id}/playlists"

		response = requests.post(url, data =request_body, headers= headers )

		results = response.json()


		if results:

				self.playlist_id = results['id']
				return results['id']

		else:
				raise(f"No user exists with username:{spotify_id}")


	def  add_to_playlist(self, playlist_id, track_id):

		headers = {		
			"Content-Type": "application/json", 
			"Authorization": f"Bearer {self.api_token}"
		}

		uri_data = f"spotify:track:{track_id}"
		url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={uri_data}"

		
		response = requests.post(url, headers = headers)

		results = response.json()

		if results:
			return results['snapshot_id']

		else:
			raise("Couldn't add track to playlists")



	def  get_playlist(self, playlist_id):


		headers = {
    	"Authorization": f"Bearer {self.api_token}",
    	"Content-Type": "application/json", 
    	"Accept": "application/json"
    	}




		url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
		print(url)

		response = requests.get(url, headers = headers)


		print(response)

		results =  response.json()

		results = results['description']

		#return response

		if results:

			print(results)


		else:

			raise("No playlists exists for given playlist_id")










		




