# flask_flutter_server

Python flask application to serve flutter web builds.

Find the article explaining the project on Medium.

## Changing The Page Route 

This app sets the flutter application to be launched with the url: `[home_domain]/web` . This url can be changed to `[home_domain]/app` , `[home_domain]/home` or `[home_domain]/[foo]` where `foo` is any word of your choice.

The following 2 steps would have to be followed to get this to work.

### 1. Update index.html File

Locate the following line in your index.html. file.

```
<base href="/">
```

Replace this line with the following:

```
<base href="/[foo]/">
```

Remember `[foo]` should be a single word of your choice.


### 2. Update Controller Routes

Locate the functions in your controller file or your app.py file that serve te flutter application. This repository uses the following controller functions:

```py

@app.route('/web/')
def render_page_web():
    return render_template('index.html')


@app.route('/web/<path:name>')
def return_flutter_doc(name):

    datalist = str(name).split('/')
    DIR_NAME = FLUTTER_WEB_APP

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]

    return send_from_directory(DIR_NAME, datalist[-1])

```

Replace the `web` in the routes with `[foo]` and you're good to go.

You can now access your app via your custom url `[home_domain]/[foo]` the next time you run it locally or on a server.


