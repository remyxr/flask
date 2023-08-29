from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
      <body> 
        <h1>Home Page!</h1>
        <p>Welcome to my simple app!</p>
        <a href='/hello'>Go to Hello Page</a> 
        <br>
        <a href='/goodbye'>Go to Goodbye Page</a>
        <br>
        <a href='/search'>Go to Search Page</a>
        <br>
        <a href='/add-comment'>Add A Comment</a>
      </body>
    </html>
    """
    return html

@app.route('/hello')
def say_hello():
   return render_template("hello.html")

@app.route('/goodbye')
def say_bye():
  html = """
  <html>
    <body> 
      <h1>Goodbye World!</h1>
      <p>This is the farewell page</p>
      <a href='/'>Return to home page</a/
    </body>
  </html>
    """
  return html

@app.route('/search')
def search():
   term = request.args['term']
   return f"<h1>Searching for {term}</h1>"

@app.route('/add-comment')
def add_comment_form():
   return"""
   <h1>Add Comment</h1>
   <form method="POST">
     <input type='text' placeholder='comment' name='comment'/>
     <input type='text' placeholder='username' name='username'/>
     <button>Submit</button>
   </form>
   """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
      <li>Comment: {comment}</li>
      <li>Posted By: {username}</li>
    </ul>
    """

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
   return f"<h1>Browsing The {subreddit} Subreddit</h1>"

@app.route("/r/<subreddit>/comments/<iny:post_id>")
def show_comments(subreddit, post_id):
   return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} subreddit</h1>"

POSTS = {
   1: "I like chicken tenders",
   2: "I hate fat people",
   3: "Double rainbow all the way",
   4: "YOLO OMG (kill me)"
}

@app.route('/posts/<int:id>')
def find_post(id):
   post = POSTS.get(id, "Post not found")
   return f"<p>{post}</p>"