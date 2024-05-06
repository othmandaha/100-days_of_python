import requests
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "OTHMANDAHA321"
USERNAME = "othman"

headers = {
    "X-USER-TOKEN": TOKEN
}
date = datetime.now() # the date 
date = date.strftime("%Y%m%d") # formating the date to be compliate with the requrement of Pixela (yyyymmdd)

#* POST an "Acount"
parameter = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}
# respons = requests.post(url=PIXELA_ENDPOINT, json=parameter)
# print(respons.text)


#* POST a graph (create)
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    'id': "graph1",
    'name': "Books",
    'unit': "Pages",
    'type': "int",
    'color': "momiji"
}
# respons = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(respons.text)


#* POST a pixel (create)
post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixelConfig = {
    'date': date,
    'quantity': "20"
}
# respons = requests.post(url=post_pixel_endpoint, json=pixelConfig, headers=headers)
# print(respons.text)


#* PUT a pixel (update)
put_pixel_endoint = f"{post_pixel_endpoint}/{date}"
put_pixel_config = {
    'quantity': "30"
}

# respons = requests.put(url=put_pixel_endoint, json=put_pixel_config, headers=headers)
# print(respons.text)


#* DELETE a pixel
delete_pixel_endpoint = put_pixel_endoint   # it is the same as the url for updating
respons = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(respons.text)


















