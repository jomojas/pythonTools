import requests
import os

# Full URL of the audio file
audio_url = "https://www.liustar.cn/upload/202401/24/202401240935106562.mp3"

# Specify the path where you want to save the file
# Example: saving the file to a directory called 'audio_files' in the current working directory
save_path = "C:/Users/Jomo/Desktop/listingSourceFiles/31-L2.mp3"

# Ensure the directory exists, create it if it doesn't
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Send an HTTP GET request to the audio URL
response = requests.get(audio_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content as an audio file in the specified path
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"Audio file has been downloaded and saved to {save_path}")
else:
    print(f"Failed to download the audio file. HTTP Status code: {response.status_code}")
