# Add Default Libraries
import falcon
import logging
import mongodb
import json

import forum as f

# App Entry Point
app = falcon.API()

# Use Cases: The user logs into app and searches
user = f.Users()
post = f.Posts()

app.add_route('/user', user)
app.add_route('/post', postgit s)
