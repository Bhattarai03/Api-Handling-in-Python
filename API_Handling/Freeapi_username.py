import requests
def fetch_random_user_freeapi() :
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    content=response.json()

    if content["success"] and "data" in content:
        userdata=content["data"]
        username=userdata["login"]["username"]
        country=userdata["location"]["country"]
        return username,country
    else:
        raise Exception ("Failed to fetch user data")
    
def main():
    try:
        username,country = fetch_random_user_freeapi()
        print(f"Username : {username} \n Country :{country}")
    except Exception as e :
        print(str(e))

if __name__=="__main__":
    main()