# Web API design

## Most modern web applications expose APIs that clients can use to interact with the application. A well-designed web API should aim to support:

## Platform independence. Any client should be able to call the API, regardless of how the API is implemented internally. This requires using standard protocols, and having a mechanism whereby the client and the web service can agree on the format of the data to exchange.

## Service evolution. The web API should be able to evolve and add functionality independently from client applications. As the API evolves, existing client applications should continue to function without modification. All functionality should be discoverable so that client applications can fully use it.


## Introduction to REST(Representational State Transfer (REST)
### REST is an architectural style for building distributed systems based on hypermedia.
A primary advantage of REST over HTTP is that it uses open standards, and does not bind the implementation of the API or the client applications to any specific implementation

## proposed the following maturity model for web APIs:

Level 0: Define one URI, and all operations are POST requests to this URI.
Level 1: Create separate URIs for individual resources.
Level 2: Use HTTP methods to define operations on resources.
Level 3: Use hypermedia (HATEOAS, described below)


## Define operations in terms of HTTP methods
The HTTP protocol defines a number of methods that assign semantic meaning to a request. The common HTTP methods used by most RESTful web APIs are:

### GET retrieves a representation of the resource at the specified URI. The body of the response message contains the details of the requested resource.

### POST creates a new resource at the specified URI. The body of the request message provides the details of the new resource. Note that POST can also be used to trigger operations that don't actually create resources.

### PUT either creates or replaces the resource at the specified URI. The body of the request message specifies the resource to be created or updated.

### PATCH performs a partial update of a resource. The request body specifies the set of changes to apply to the resource.

### DELETE removes the resource at the specified URI.
The effect of a specific request should depend on whether the resource is a collection or an individual item. The following table summarizes the common conventions adopted by most RESTful implementations using the e-commerce example. Not all of these requests might be implemented—it depends on the specific scenario.


A POST request creates a resource. The server assigns a URI for the new resource, and returns that URI to the client. In the REST model, you frequently apply POST requests to collections. The new resource is added to the collection. A POST request can also be used to submit data for processing to an existing resource, without any new resource being created.

A PUT request creates a resource or updates an existing resource. The client specifies the URI for the resource. The request body contains a complete representation of the resource. If a resource with this URI already exists, it is replaced. Otherwise a new resource is created, if the server supports doing so. PUT requests are most frequently applied to resources that are individual items, such as a specific customer, rather than collections. A server might support updates but not creation via PUT. Whether to support creation via PUT depends on whether the client can meaningfully assign a URI to a resource before it exists. If not, then use POST to create resources and PUT or PATCH to update.

A PATCH request performs a partial update to an existing resource. The client specifies the URI for the resource. The request body specifies a set of changes to apply to the resource. This can be more efficient than using PUT, because the client only sends the changes, not the entire representation of the resource. Technically PATCH can also create a new resource (by specifying a set of updates to a "null" resource), if the server supports this.

PUT requests must be idempotent. If a client submits the same PUT request multiple times, the results should always be the same (the same resource will be modified with the same values). POST and PATCH requests are not guaranteed to be idempotent.

## Notes Pulled from https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design 
