from flask import Flask
from routes.test1 import router as test1_router
from routes.test2 import router as test2_router

app = Flask(__name__)
app.register_blueprint(test1_router, url_prefix='/test1')
app.register_blueprint(test2_router, url_prefix='/test2')

app.run()