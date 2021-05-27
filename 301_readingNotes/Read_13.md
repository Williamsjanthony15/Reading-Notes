Read 13


In your own words, describe what each group of status code represents:
100’s = These are informational status codes;

200’s = These are Success Codes

300’s = Redirection Codes

400’s = client Error Codes

500’s = Server Error Codes

What is a status code 202?
202 accepted - often used for asynchronous processing. Basically telling you the request was valide, but its processing will finish at a different time.

What is a status code 308?
Permanent Redirect - if we have nested resources and root resources it can make things easier to simply issue 308 redirects at the nested resources with the location header field pointed to the root resources so not every endpoint needs a delivery implementation. this should be done for GET requests. 

What code would you use if an update didn’t return data to a client?
204 No Content - a proper code for updates that dont return data to the client, IE: when just savinga currently edited document. 

What code would you use if a resource used to exist but no longer does?
308 Permanenet redirect. 

What is the ‘Forbidden’ status code?
403 - forbidden 
