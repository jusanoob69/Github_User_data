import requests
USERNAME = ''


def search():
    print(USERNAME)
    
    api_url = f"https://api.github.com/users/{USERNAME}"
    response = requests.get(api_url)

    user_data = response.json() 
    print(user_data)

def main():
    global USERNAME 
    print('Welcome to the amazing Github user data puller thingy!')

    USERNAME = input("Who's data are you looking for today? ")
    print("Alright, looking for user: " + USERNAME + " Data!")
       


    response_code = requests.get('https://api.github.com/')
    if response_code.status_code != 200:
        print('There was a problem loading Github, please try again later.')
    else: 
        search()
    

main()
    


