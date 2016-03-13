from flask import Flask, jsonify, request
from bing_search import bing_search
app = Flask(__name__)


# @app.route('/news')
# def news():
# 	try:
# 		results = bing_search('Cardale Jones', 'News', None)
# 	except Exception as inst:
# 		print "exceptiom"
# 		print type(inst)
# 		print inst
# 	return jsonify(results)


@app.route('/news')
def news():
	# name = request.args.get('name')
	# results = bing_search('Cardale Jones', 'News', None)
	# return jsonify(results)
	return "hello"

if __name__ == '__main__':
    app.run()