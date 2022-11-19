from flask import jsonify
from flask_restful import Resource
from flask_simplelogin import login_required

class ProductResource(Resource):
    def get(self):
        return jsonify({"products": ""})

    @login_required(basic=True, username="admin")
    def post(self):
        """
        Creates a new product.

        Only admin user authenticated using basic auth can post
        Basic takes base64 encripted username:password.

        # curl -XPOST localhost:5000/api/v1/product/ \
        #  -H "Authorization: Basic Y2h1Y2s6bm9ycmlz" \
        #  -H "Content-Type: application/json"
        """
        return NotImplementedError(
            "Someone please complete this example and send a PR :)"
        )

class ProductItemResource(Resource):
    def get(self, product_id):
        return {""}
