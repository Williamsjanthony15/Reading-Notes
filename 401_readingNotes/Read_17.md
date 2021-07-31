# Web Scraping

## Web scraping is a technique to automatically access and extract large amounts of information from a website, which can save a huge amount of time and effort. In this article, we will go through an easy example of how to automate downloading hundreds of files from the New York MTA. This is a great exercise for web scraping beginners who are looking to understand how to web scrape. Web scraping can be slightly intimidating, so this tutorial will break down the process of how to go about the process.


New York MTA Data
We will be downloading turnstile data from this site:
http://web.mta.info/developers/turnstile.html
Turnstile data is compiled every week from May 2010 to present, so hundreds of .txt files exist on the site. Below is a snippet of what some of the data looks like. Each date is a link to the .txt file that you can download.

It would be torturous to manually right click on each link and save to your desktop. Luckily, there’s web-scraping!
Important notes about web scraping:
Read through the website’s Terms and Conditions to understand how you can legally use the data. Most sites prohibit you from using the data for commercial purposes.
Make sure you are not downloading data at too rapid a rate because this may break the website. You may potentially be blocked from the site as well.
Inspecting the Website
The first thing that we need to do is to figure out where we can locate the links to the files we want to download inside the multiple levels of HTML tags. Simply put, there is a lot of code on a website page and we want to find the relevant pieces of code that contains our data. If you are not familiar with HTML tags, refer to W3Schools Tutorials. It is important to understand the basics of HTML in order to successfully web scrape.
On the website, right click and click on “Inspect”. This allows you to see the raw code behind the site.

Once you’ve clicked on “Inspect”, you should see this console pop up.

Console
Notice that on the top left of the console, there is an arrow symbol.

If you click on this arrow and then click on an area of the site itself, the code for that particular item will be highlighted in the console. I’ve clicked on the very first data file, Saturday, September 22, 2018 and the console has highlighted in blue the link to that particular file.
<a href=”data/nyct/turnstile/turnstile_180922.txt”>Saturday, September 22, 2018</a>
Notice that all the .txt files are inside the <a> tag following the line above. As you do more web scraping, you will find that the <a> is used for hyperlinks.
Now that we’ve identified the location of the links, let’s get started on coding!
Python Code
We start by importing the following libraries.
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
Next, we set the url to the website and access the site with our requests library.
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
If the access was successful, you should see the following output:

Next we parse the html with BeautifulSoup so that we can work with a nicer, nested BeautifulSoup data structure. If you are interested in learning more about this library, check out the BeatifulSoup documentation.
soup = BeautifulSoup(response.text, “html.parser”)
We use the method .findAll to locate all of our <a> tags.
soup.findAll('a')
This code gives us every line of code that has an <a> tag. The information that we are interested in starts on line 38 as seen below. That is, the very first text file is located in line 38, so we want to grab the rest of the text files located below.

subset of all <a> tags
Next, let’s extract the actual link that we want. Let’s test out the first link.
one_a_tag = soup.findAll(‘a’)[38]
link = one_a_tag[‘href’]
This code saves the first text file, ‘data/nyct/turnstile/turnstile_180922.txt’ to our variable link. The full url to download the data is actually ‘http://web.mta.info/developers/data/nyct/turnstile/turnstile_180922.txt’ which I discovered by clicking on the first data file on the website as a test. We can use our urllib.request library to download this file path to our computer. We provide request.urlretrieve with two parameters: file url and the filename. For my files, I named them “turnstile_180922.txt”, “turnstile_180901”, etc.
download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
Last but not least, we should include this line of code so that we can pause our code for a second so that we are not spamming the website with requests. This helps us avoid getting flagged as a spammer.
time.sleep(1)
Now that we understand how to download a file, let’s try downloading the entire set of data files with a for loop. The code below contains the entire set of code for web scraping the NY MTA turnstile data.


_________EXAMPLE FROM READING_____________

# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    if line_count >= 36: #code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
    line_count +=1
    
    
    ________EXAMPLE FROM READING_______________
    
    Taken from https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
    
    # How to Web Scrape without getting Blocked
    
    Web scraping is a task that has to be performed responsibly so that it does not have a detrimental effect on the sites being scraped. Web Crawlers can retrieve data much quicker, in greater depth than humans, so bad scraping practices can have some impact on the performance of the site. While most websites may not have anti-scraping mechanisms, some sites use measures that can lead to web scraping getting blocked, because they do not believe in open data access.

If a crawler performs multiple requests per second and downloads large files, an under-powered server would have a hard time keeping up with requests from multiple crawlers. Since web crawlers, scrapers or spiders (words used interchangeably) don’t really drive human website traffic and seemingly affect the performance of the site, some site administrators do not like spiders and try to block their access.

In this article, we will talk about the best web scraping practices to follow to scrape websites without getting blocked by the anti-scraping or bot detection tools.

bypass-antiscraping

Web Scraping best practices to follow to scrape without getting blocked
Respect Robots.txt
Make the crawling slower, do not slam the server, treat websites nicely
Do not follow the same crawling pattern
Make requests through Proxies and rotate them as needed
Rotate User Agents and corresponding HTTP Request Headers between requests
Use a headless browser like Puppeteer, Selenium or Playwright
Beware of Honey Pot Traps
Check if Website is Changing Layouts
Avoid scraping data behind a login
Use Captcha Solving Services
How can websites detect web scraping?
How do you find out if a website has blocked or banned you ?
Basic Rule: “Be Nice”
An overarching rule to keep in mind for any kind of web scraping is
BE GOOD AND FOLLOW A WEBSITE’S CRAWLING POLICIES
Here are the web scraping best practices you can follow to avoid getting web scraping blocked:
Respect Robots.txt
Web spiders should ideally follow the robot.txt file for a website while scraping. It has specific rules for good behavior such as how frequently you can scrape, which pages allow scraping, and which ones you can’t. Some websites allow Google to scrape their websites, by not allowing any other websites to scrape. This goes against the open nature of the Internet and may not seem fair but the owners of the website are within their rights to resort to such behavior. 

You can find the robot.txt file on websites. It is usually the root directory of a website – http://example.com/robots.txt.

If it contains lines like the ones shown below, it means the site doesn’t like and does not want to be scraped.

User-agent: *

Disallow:/ 

However, since most sites want to be on Google, arguably the largest scraper of websites globally, they do allow access to bots and spiders. 

What if you need some data, that is forbidden by Robots.txt. You could still go and scrape it. Most anti-scraping tools block web scraping when you are scraping pages that are not allowed by Robots.txt.

What do these tools look for – is this client a bot or a real user. And how do they find that? By looking for a few indicators that real users do and bots don’t.  Humans are random, bots are not. Humans are not predictable, bots are.

Here are a few easy giveaways that you are bot/scraper/crawler –

scraping too fast and too many pages, faster than a human ever can
following the same pattern while crawling. For example – go through all pages of search results, and go to each result only after grabbing links to them. No human ever does that.
too many requests from the same IP address in a very short time
not identifying as a popular browser. You can do this by specifying a ‘User-Agent’.
using a user agent string of a very old browser
The points below should get you past most of the basic to intermediate anti-scraping mechanisms used by websites to block web scraping.

Make the crawling slower, do not slam the server, treat websites nicely


Web scraping bots fetch data very fast, but it is easy for a site to detect your scraper as humans cannot browse that fast. The faster you crawl, the worse it is for everyone. If a website gets too many requests than it can handle it might become unresponsive.

Make your spider look real, by mimicking human actions. Put some random programmatic sleep calls in between requests, add some delays after crawling a small number of pages and choose the lowest number of concurrent requests possible. Ideally put a delay of 10-20 seconds between clicks and not put much load on the website, treating the website nice.

Use auto throttling mechanisms which will automatically throttle the crawling speed based on the load on both the spider and the website that you are crawling. Adjust the spider to an optimum crawling speed after a few trials runs. Do this periodically because the environment does change over time.

Learn More: How to send anonymous requests using TorRequests and Python

Do not follow the same crawling pattern
Humans generally will not perform repetitive tasks as they browse through a site with random actions. Web scraping bots tend to have the same crawling pattern because they are programmed that way unless specified. Sites that have intelligent anti-crawling mechanisms can easily detect spiders by finding patterns in their actions and can lead to web scraping getting blocked.

Incorporate some random clicks on the page, mouse movements and random actions that will make a spider look like a human.

Make requests through Proxies and rotate them as needed
When scraping, your IP address can be seen. A site will know what you are doing and if you are collecting data. They could take data such as – user patterns or experience if they are first time users.

Multiple requests coming from the same IP will lead you to get blocked, which is why we need to use multiple addresses. When we send requests from a proxy machine, the target website will not know where the original IP is from, making the detection harder.

Create a pool of IPs that you can use and use random ones for each request. Along with this, you have to spread a handful of requests across multiple IPs.

There are several methods can be used to change your outgoing IP.

TOR
VPNs
Free Proxies
Shared Proxies – the least expensive proxies, shared by many users. Chances to get blocked are high.
Private Proxies – usually used only by you, and lower chances of getting blocked if you keep the frequency low.
Data Center Proxies, if you need a large number of IP Address and faster proxies, larger pools of IPs. They are cheaper than residential proxies and coulde be detected easily.
Residential Proxies, if you are making a huge number of requests to websites that block to actively. These are very expensive (and could be slower, as they are real devices). Try everything else before getting a residential proxy.
In addition, various commercial providers also provide services for automatic IP rotation. A lot of companies now provide residential IPs to make scraping even easier – but most are expensive.

Learn More:
How To Rotate Proxies and IP Addresses using Python 3
How to make anonymous requests using TorRequests and Python
Rotate User Agents and corresponding HTTP Request Headers between requests
A user agent is a tool that tells the server which web browser is being used. If the user agent is not set, websites won’t let you view content. Every request made from a web browser contains a user-agent header and using the same user-agent consistently leads to the detection of a bot. You can get your User-Agent by typing ‘what is my user agent’ in Google’s search bar. The only way to make your User-Agent appear more real and bypass detection is to fake the user agent. Most web scrapers do not have a User Agent by default, and you need to add that yourself.

You could even pretend to be the Google Bot: Googlebot/2.1 if you want to have some fun! (http://www.google.com/bot.html)

Now, just sending User-Agents alone would get you past most basic bot detection scripts and tools. If you find your bots getting blocked even after putting in a recent User-Agent string, you should add some more request headers.

Most browsers sends more headers to the websites than just the User-Agent. For example, here is a set of headers a browser sent to Scrapeme.live (Our Web Scraping Test Site). It would be ideal to send these common request headers too.



The most basic ones are:

User-Agent
Accept
Accept-Language
Referer
DNT
Updgrade-Insecure-Requests
Cache-Control
Do not send cookies unless your scraper depends on Cookies for functionality.

You can find the right values for these by inspecting your web traffic using Chrome Developer Tools, or a tool like MitmProxy or Wireshark. You can also copy a curl command to your request from them. For example

curl 'https://scrapeme.live/shop/Ivysaur/' \
-H 'authority: scrapeme.live' \
-H 'dnt: 1' \
-H 'upgrade-insecure-requests: 1' \
-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' \
-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
-H 'sec-fetch-site: none' \
-H 'sec-fetch-mode: navigate' \
-H 'sec-fetch-user: ?1' \
-H 'sec-fetch-dest: document' \
-H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
--compressed
You can get this converted to any language using a tool like https://curl.trillworks.com

Here is how this was converted to python

import requests
headers = {
'authority': 'scrapeme.live',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
response = requests.get('https://scrapeme.live/shop/Ivysaur/', headers=headers)
You can create similar header combinations for multiple browsers and start rotating those headers between each request to reduce the chances of getting your web scraping blocked.

Learn More: How to fake and rotate User Agents using Python 3 
Use a headless browser like Puppeteer, Selenium or Playwright
If none of the methods above works, the website must be checking if you are a REAL browser.

The simplest check is if the client (web browser) can render a block of JavaScript. If it doesn’t, then it pretty much flags the visitor to be a bot. While it is possible to block running JavaScript in the browser, most of the Internet sites will be unusable in such a scenario and as a result, most browsers will have JavaScript enabled.

Once this happens, a real browser is necessary in most cases to scrape the data. There are libraries to automatically control browser such as

Selenium
Puppeteer and Pyppeteer
Playwright
Anti Scraping tools are smart and are getting smarter daily, as bots feed a lot of data to their AIs to detect them. Most advanced Bot Mitigation Services use Browser Side Fingerprinting (Client Side Bot Detection)  by more advanced methods than just checking if you can execute Javascript.

Bot detection tools look for any flags that can tell them that the browser is being controlled through an automation library.

Presence of bot specific signatures
Support for nonstandard browser features
Presence of common automation tools such as Selenium, Puppeteer, Playwright, etc.
Human-generated events such as randomized Mouse Movement, Clicks, Scrolls, Tab Changes etc.
All this information is combined to construct a unique client-side fingerprint that can tag one as bot or human.

Here are a few workarounds or tools which could help your headless browser-based scrapers from getting banned.

Puppeteer Extra  – Puppeteer Stealth Plugin
Patching Selenium/ Phantom JS – Stack OverFlow Answer on Patching Selenium with Chrome Driver
Fingerprint Rotation – Microsoft Paper on Fingerprint Rotation
But as you might have guessed, just like Bots, Bot Detection companies are getting smarter. They have been improving their AI models and look for variables, actions, events, etc that can still give away the presence of an automation library leading to web scraping getting blocked.

Web scraping tutorial using a headless browser:

Web Scraping Hotel Prices using Selenium and Python 
 How to build a Web Scraper using Puppeteer and Node.Js
Beware of Honey Pot Traps
Honeypots are systems set up to lure hackers and detect any hacking attempts that try to gain information. It is usually an application that imitates the behavior of a real system. Some websites install honeypots, which are links invisible to normal users but can be seen by web scrapers.

When following links always take care that the link has proper visibility with no nofollow tag. Some honeypot links to detect spiders will have the CSS style display:none or will be color disguised to blend in with the page’s background color.

This detection is obviously not easy and requires a significant amount of programming work to accomplish properly, as a result, this technique is not widely used on either side – the server side or the bot or scraper side.

Learn More: XPath and their relevance in Web Scraping 
Check if Website is Changing Layouts
Some websites make it tricky for scrapers, serving slightly different layouts.

For example, in a website pages 1-20 will display a layout, and rest of the pages may display something else. To prevent this, check if you are getting data scraped using XPaths or CSS selectors. If not, check how the layout is different and add a condition in your code to scrape those pages differently.

Avoid scraping data behind a login
Login is basically permission to get access to web pages. Some websites like Indeed and Facebook do not allow permission.

If a page is protected by login, the scraper would have to send some information or cookies along with each request to view the page. This makes it easy for the target website to see requests coming from the same address. They could take away your credentials or block your account which can in turn lead to your web scraping efforts being blocked.

Its generally preferred to avoid scraping websites that have a login as you will get blocked easily, but one thing you can do is imitate human browsers whenever authentication is required you get the target data you need.

Use Captcha Solving Services
Many websites use anti web scraping measures. If you are scraping a website on a large scale, the website will eventually block you. You will start seeing captcha pages instead of web pages. There are services to get past these restrictions such as 2Captcha or Anticaptcha.

If you need to scrape websites that use Captcha, it is better to resort to captcha services. Captcha services are relatively cheap, which is useful when performing large scale scrapes.

Learn More: How to Solve Simple Captchas using Python Tesseract 
How can websites detect and block web scraping?
how-do-websites-detect-web-scraping

Websites can use different mechanisms to detect a scraper/spider from a normal user. Some of these methods are enumerated below:

Unusual traffic/high download rate especially from a single client/or IP address within a short time span.
Repetitive tasks performed on the website in the same browsing pattern – based on an assumption that a human user won’t perform the same repetitive tasks all the time.
Checking if you are real browser – A simple check is to try and execute javascript. Smarter tools can go a lot more and check your Graphic cards and CPUs 😉 to make sure you are coming from real browser.
Detection through honeypots – these honeypots are usually links which aren’t visible to a normal user but only to a spider. When a scraper/spider tries to access the link, the alarms are tripped.
Learn more about how websites detect and block web scrapers

How do Websites detect and block bots using Bot Mitigation Tools
How to address this detection and avoid web scraping getting blocked? 

Spend some time upfront and investigate the anti-scraping mechanisms used by a site and build the spider accordingly, it will provide a better outcome in the long run and increase the longevity and robustness of your work.

How do you find out if a website has blocked or banned you?
website-blocked-scraping

If any of the following signs appear on the site that you are crawling, it is usually a sign of being blocked or banned.

CAPTCHA pages
Unusual content delivery delays
Frequent response with HTTP 404, 301 or 50x errors
Frequent appearance of these HTTP status codes is also indication of blocking

301 Moved Temporarily
401 Unauthorized
403 Forbidden
404 Not Found
408 Request Timeout
429 Too Many Requests
503 Service Unavailable
Here is what Amazon.com tells you when you are blocked.

To discuss automated access to Amazon data please contact api-services-support@amazon.com.
For information about migrating to our APIs refer to our Marketplace APIs at <link>  or our Product Advertising API at  <link> for advertising use cases.
Sorry! Something went wrong!
With pictures of cute dog of Amazon.
You may also see response or message from website like these ones from some popular anti scraping tools.

We want to make sure it is actually you that we are dealing with and not a robot

Please check the box below to access the site

<reCaptcha>

Why is this verification required? Something about the behaviour of the browser has caught our attention.

There are various possible explanations for this:

you are browsing and clicking at a speed much faster than expected of a human being
something is preventing Javascript from working on your computer
there is a robot on the same network (IP address) as you
Having problems accessing the site? Contact Support

Authenticate your robot

or

Please verify you are a human 

<Captcha> 

Access to this page has been denied because we believe you are using automation tools to browse the website

This may happen as a result of the following: 

Javascript is disabled or blocked by an extension (ad blockers for example) 
Your browser does not support cookies 
Please make sure that Javascript and cookies are enabled on your bowser and that you are not blocking them from loading 

or

Pardon our interruption

As you were browsing <website> something about your browser made us think you were a bot. There are few reasons this might happen

You’re a power user using moving through this website with super-human speed 
You’ve disabled JavaScript in your web browser 
A third-party bowser plugin such as Ghostery or NoScript, is preventing Javascript from running. Additional information is available in this support article.
After completing the CAPTCHA below, you will immediately regain access to <website>

or

Error 1005 Ray ID: <hash> • <time>
Access denied

What happened?

The owner of this website (<website>) has banned the autonomous system number (ASN) your IP address is in (<number>) from accessing this website.

A comprehensive list of HTTP return codes (successes and failures) can be found here. It will be worth your time to read through these codes and be familiar with them.

taken from https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/


_________________________________________________

