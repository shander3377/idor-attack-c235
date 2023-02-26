import requests
for i in range(0,5000):
    url = "http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id="+str(i)
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(url)
        