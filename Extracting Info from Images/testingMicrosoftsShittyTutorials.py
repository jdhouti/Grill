import http.client, urllib.request, urllib.parse, urllib.error, base64
import json, csv
import codecs

reader = codecs.getreader("utf-8")

headers = {
    # Request headers. Replace the key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'fd0b9f206a584fc5b5353ba4fbed6451',
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories',
    'details': 'Celebrities',
    'language': 'en',
})

# Replace the three dots below with the URL of a JPEG image of a celebrity.
body = "{'url':'https://pbs.twimg.com/profile_images/659040352507039744/1tw770Qo.jpg'}"

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()      # this is in bytes. we want this as a string.
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
else:       # we don't like json files, so we're converting this one to a .csv file.
    work_with = json.loads(reader(data))
    work_data = work_with['categories']
    write_data = open('/load_me.csv', 'w')
    csvwriter = csv.writer(write_data)

    count = 0

    for emp in work_data:
          if count == 0:
              header = emp.keys()
              csvwriter.writerow(header)
              count += 1

          csvwriter.writerow(emp.values())

    write_data.close()