# android-restme
Playground for Android Rest code generator

# Setup
create a new virtualenv myenv using PyCharm or manualy

```virtualenv myenv```

install dependency with PyCharm
open any file that imports jinja2, a notification will showup asking you to install everything

# Running
Right click on the app.py then Run 'app'/Debug with PyCharm or
In the "Scripts parameters" paste the full path of the working directory.

```python app.py MyWorkingDir``` Ensure you have loaded the virtualenv
where MyWorkingDir is the full path of the Android project location i.e:
../samples/RestTest

# Demo REST server
in the rest_demo directory

```npm install```

```npm start```

Can be accessed from:

- http://localhost:3004/greetings
- http://0.0.00:3004/greetings

Outside only (like for Android) in a LAN:
- http://192.168.0.100:3004/greetings - Replace it with your computer's IP

# Reference

## Jinja2
- http://jinja.pocoo.org/docs/2.9/templates/
- http://jinja.pocoo.org/docs/2.9/templates/#builtin-filters
- https://pythonadventures.wordpress.com/2014/02/25/jinja2-example-for-generating-a-local-file-using-a-template/

## Rest template
- https://spring.io/guides/gs/consuming-rest-android/
- http://docs.spring.io/spring-android/docs/2.0.0.M3/reference/html/
- http://docs.spring.io/spring-android/docs/2.0.0.M3/reference/html/rest-template.html#d5e154
