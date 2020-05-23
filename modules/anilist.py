import graphene
import requests
import json

class Anilist(graphene.ObjectType):

	def aniSearch(show):
		# query of info we want from AniList
		query = '''
		query ($id: Int, $search: String, $asHtml: Boolean) {
	        Media (id: $id, search: $search) {
	            id
	            title {
	                romaji
	            }
	            status
	            description(asHtml: $asHtml)
	            startDate {
	            	year
	            	month
	            	day
	            }
	            endDate {
	            	year
	            	month
	            	day
	            }
	            season
	            seasonYear
	            episodes
	            coverImage {
	            	large
	            }
	            bannerImage
	            genres
	            meanScore
	            popularity
	            siteUrl
	        }
		}
		'''

		variables = {
		    'search': show,
		    'asHtml': False
		}

		source = 'https://graphql.anilist.co'

		response = requests.post(source, json={'query': query, 'variables': variables})
		result = response.json();

		if response.status_code == 200:
			return result
		else:
			print('Response code: ' + str(response.status_code) + '\n\n' + str(result))
			return None

	def aniReg(user, aniUser): # WIP - To properly integrate this portion use the AniList API to save user-related information to the JSON file under their Discord user ID
		with open("./anilist/"+serverID+".json", 'r') as server_json:
			json_data = json.load(server_json)
			# changes the line to update in the json
			json_data[user] = aniUser
		# writes the changes to the json file
		with open("./anilist/"+serverID+".json", 'w') as server_json:
			server_json.write(json.dumps(json_data))
