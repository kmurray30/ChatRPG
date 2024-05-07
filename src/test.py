import urllib.request
import os
import webbrowser

filename = os.path.splitext(os.path.basename(__file__))[0]
if __name__ == "__main__" or __name__ == filename: # If the script is being run directly
    from Utilities.Utilities import get_path_from_project_root
else: # If the script is being imported
    from .Utilities.Utilities import get_path_from_project_root

image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-HfuTJ02W7MMFVgygxGVaCDTt/user-znmLbOfX97nI5jmApfx0GRtf/img-oYNcW3G43CpxsTIkZbq3UfoN.png?st=2024-05-06T17%3A17%3A09Z&se=2024-05-06T19%3A17%3A09Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-05T21%3A39%3A49Z&ske=2024-05-06T21%3A39%3A49Z&sks=b&skv=2021-08-06&sig=HaYdi%2Bv%2BFKH3Xm6o2ZiUQNevn4R/Q2wNGyc5z5mkhaQ%3D"
file_path = get_path_from_project_root("gnerated/temp/test.png")

def save_image_from_url(url, file_path):
    urllib.request.urlretrieve(url, file_path)


save_image_from_url(image_url, file_path)
webbrowser.open(f"file:///{file_path}")