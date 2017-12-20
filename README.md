# PyCycle  -  Simple Condensed Python API starter code to get you quickly going!

## API
This is a minimialist starter code for a Python API with a MongoDB database. The sample
app used will be a simple API for a web forum with simple user analytics
## Usage (in irb shell for example)

```python
# Creating a user
fname = "sam"
lname = "geb"
username = "sgeb"
u = User(fname, lname, username)
u.save()
print("created user: " + str(u._id))
u = User().find_one({'_id':u._id})
print(u)
User().delete({'_id': u['_id']})
u = User().find({'fname':fname})
print(list(u))
```

## TODO
- [] Add user registration
- [] Add analytics
- [] Create Topic-Thread
- [] Reply to a post in a thread
- [] Track another user's posts
* Falcon - Python Framework
* pip install falcon mongodb
* Mongo - MongoDB library
* [https://falconframework.org] (Falcon Framework) - A very fast Python mimial frameworkgit st.
* [https://api.mongodb.com/python/current/]) (PyMongo) -  Python client for MongoDB

## License

    Copyright [2017] [Sabelo Mhlambi]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License
