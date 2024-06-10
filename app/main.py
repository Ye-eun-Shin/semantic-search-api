from flask import Flask, request, json, Response
from elasticsearch import Elasticsearch

from app.encoder import Encoder
from app.utils import create_es_index, es_search


hashtag_index_name = "hashtag"
review_index_name = "review"


es = Elasticsearch(["https://localhost:9200"],
                   http_auth=('elastic', '52hQvbxBQifRe7K2oezF'),
                   verify_certs=False)
es_indices1 = create_es_index(es, index=hashtag_index_name)
es_indices2= create_es_index(es, index=review_index_name)


encoder = Encoder("small", dimension=256)

app = Flask(__name__)


@app.route("/hashtag", methods=["POST"])
def search_hashtag():
    query = request.json["query"]
    es_result = es_search(es, hashtag_index_name, query)
    result = {
        "elastic": es_result,
    }
    json_string = json.dumps(result,ensure_ascii = False)
    response = Response(json_string,content_type="application/json; charset=utf-8" )
    return response


@app.route("/review", methods=["POST"])
def search_review():
    query = request.json["query"]
    es_result = es_search(es, review_index_name, query)
    result = {
        "elastic": es_result,
    }
    json_string = json.dumps(result,ensure_ascii = False)
    response = Response(json_string,content_type="application/json; charset=utf-8" )
    return response


@app.route("/")
def index():
    return "Hello, Semantic Search!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8018, threaded=False)
