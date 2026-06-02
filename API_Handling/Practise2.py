import requests 
def fetch_data_from_public_api():
    endpoints="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response=requests.get(endpoints)
    content=response.json()

    if content["success"] and content["data"]:
        userid=content["data"]["id"]
        joke=content["data"]["content"]
        return userid,joke
    else:
        raise Exception ("Failed to fetch a joke")
    
def main():
    try:
        userid,joke=fetch_data_from_public_api()
        print(f"UserID:{userid} \n Joke={joke}")

    except Exception as e :
        print(str(e))

if __name__=="__main__":
    main()
