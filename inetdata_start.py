# Example File for retrieving data from the internet
import urllib.request

def main():
    webURL = urllib.request.urlopen('https://www.google.com')
    print("result code: " + str(webURL.getcode()))
    data = webURL.read()
    print(data)



if __name__ == "__main__":
    main() 