
from .ext.restapi.api import app
from .ext.restapi.api import *

if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True, port=5000)
