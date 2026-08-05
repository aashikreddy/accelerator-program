"""
Problem Statement:

A browser stores a website URL. Create a class that initializes
the URL using a constructor and extracts:

1. Protocol
2. Domain Name
3. Top-Level Domain

Input Format:
URL

Output Format:
Protocol
Domain
Extension

Sample Input:
https://www.google.com

Sample Output:
Protocol: https
Domain: google
Extension: com
"""
class Browser:
    def __init__(self, url):
        self.url = url

    def extract(self):
        parts = self.url.split("://")
        protocol = parts[0]

        domain_parts = parts[1].split(".")
        domain = domain_parts[-2]
        extension = domain_parts[-1]

        print("Protocol:", protocol)
        print("Domain:", domain)
        print("Extension:", extension)

url = input()

browser = Browser(url)
browser.extract()