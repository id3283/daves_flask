from flask import Flask, request

app = Flask(__name__)


# Accessing with /search?q=flask will call search with query set to 'flask'
# http://127.0.0.1:5000/search?q=flask
@app.route('/search')
def search():
    # Get the query string parameter `q`
    query = request.args.get('q', '')
    return f'Search query: {query}'


# Accessing /user/john/posts?page=2 will call user_posts with username set to 'john' and page set to 2
@app.route('/user/<username>/posts')
def user_posts(username):
    # Get the query string parameter `page`
    page = request.args.get('page', 1, type=int)
    return f'User: {username}, Page: {page}'

if __name__ == '__main__':
    app.run(debug=True)


# Use Path Variables When:
# 	1.	Resource Identification: When the variable is part of the unique identifier for a resource.
# 	•	Example: /user/john where john identifies a specific user.
# 	2.	Hierarchical Data: When the data is part of a natural hierarchy.
# 	•	Example: /user/john/posts/42 where john is a user and 42 is a specific post belonging to that user.
# 	3.	RESTful URLs: When following RESTful principles, where URL structure represents resource relationships.
# 	•	Example: /products/1234/reviews where 1234 identifies a specific product, and reviews is a resource related to the product.

# Use Query Strings When:
# 	1.	Filtering, Sorting, and Searching: When you need to filter, sort, or search through a list of resources.
# 	•	Example: /products?category=books&sort=price where category and sort are used to filter and sort the list of products.
# 	2.	Optional Parameters: When the parameter is optional or has a default value.
# 	•	Example: /search?q=flask where q is the search query, which is optional.
# 	3.	Pagination: When implementing pagination to navigate through pages of data.
# 	•	Example: /posts?page=2 where page indicates which page of results to display.