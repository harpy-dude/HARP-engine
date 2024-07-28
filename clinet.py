import requests, subprocess, os, time, sys

# Function to update the player's code from the GitHub repository
def update_player_code():
    local_filename = "downloaded_dis.py"
    if os.path.isfile(local_filename):
        os.remove(local_filename)
        print(f"Previous file {local_filename} removed.")
    else:
        print(f"Error: {local_filename} not found.")

    # Replace 'bug-free-tribble' with your desired repository name and use https://raw.githubusercontent.com/user/repo/folder/file url structure 
    github_raw_url = "https://raw.githubusercontent.com/harpy-dude/bug-free-tribble/main/dis.py"
    

    response = requests.get(github_raw_url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {local_filename}")
        
        try:
            subprocess.run(['python', local_filename], check=True)
            print("File executed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error executing the file: {e}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

if __name__ == '__main__':
    update_player_code()



