# Using the client on Google AppEngine


When using this fork of the Algolia Python client on Google AppEngine, it will default to `urlfetch` instead of using the `request` module.

Note however that urlfetch has some following described in https://cloud.google.com/appengine/docs/python/urlfetch/

To run unit tests on the AppEngine stub, you need to define a enviroment variable APPENGINE_RUNTIME with a defult value.