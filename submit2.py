import requests

location = "https://wsdmcupchallenge.blob.core.windows.net/mslll/results.tsv"
sas_url = '?sv=2015-02-21&sr=b&sig=zHKzALDF5OutQA%2F31a0Mf2ITJj7TniOq7h9HGvufg%2FM%3D&st=2015-08-07T07%3A00%3A00Z&se=2015-11-13T08%3A00%3A00Z&sp=wl'

url = location + sas_url
data = 'results.tsv'

files = {'file': open(data)}
headers = {"x-ms-blob-type": 'BlockBlob'}

response = requests.put(url, files=files, headers=headers)

print response.text