from flask import Flask
import requests


# if __name__ == '___main___':
#     app = create_app()
#     app.run(port=8000, debug = True)

# @app.route('/hello')
# def hello():
r = requests.get('https://backflipp.wishabi.com/flipp/items/search?locale=en-ca&postal_code=L4J5K2&q=banana')
print(r.text)
