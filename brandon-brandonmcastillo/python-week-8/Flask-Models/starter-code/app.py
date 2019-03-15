from flask import Flask, g
from flask import render_template, flash, redirect, url_for
# This import makes our connection to the models 
import models
from forms import SubForm, PostForm, CommentForm


DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'
# Connect Database before Request
@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
# After request close the database and give a response
@app.after_request
def after_request(response):
     g.db.close()
     return response


@app.route('/', methods=['GET', 'POST'])
def index():
    # a form variable representing the SubForm
    form = SubForm()
    # check if the form submission is valid
    if form.validate_on_submit():
    # if it is, create a new sub and redirect user
        models.Sub.create(
            name = form.name.data.strip(),
            description = form.description.data.strip())
        
        return redirect('/r')

    # if it isnt, send them back to the form
    return render_template('new_sub.html', title="New Sub",form=form)

# Sub Routes
@app.route('/r')
@app.route('/r/<sub>', methods=['GET', 'POST'])

def r(sub=None):
    form = PostForm()
    if sub == None:
        # get all subs
        subs = models.Sub.select().limit(100)
        #send the retrieved subs to our subs.html template
        return render_template('subs.html', subs=subs)
    else:
        # use the <sub> ID to find the right sub
        sub_id = int(sub)
        sub = models.Sub.get(models.Sub.id == sub_id)
        posts = sub.posts
        # Define a post form
        if form.validate_on_submit():
            models.Post.create(
                user=form.user.data.strip(),
                title=form.title.data.strip(), 
                text=form.text.data.strip(), 
                sub=sub)
    # Redirect back to the subreddit where the post was created
            return redirect("/r/{}".format(sub_id))
        # send our found sub to the template
        return render_template("sub.html", sub=sub, posts=posts, form=form)

# Post Routes
@app.route('/posts', methods=['GET', 'POST'])
@app.route('/posts/<id>', methods=['GET', 'POST'])

def posts(id=None):
    form = CommentForm()
    if id == None:
        posts = models.Post.select().limit(100)
        return render_template('posts.html', posts=posts)
    else:
        post_id = int(id)
        post = models.Post.get(models.Post.id == post_id)
        comments = post.comments
        # Define a post form
        if form.validate_on_submit():
            models.Comment.create(
                title=form.title.data.strip(), 
                text=form.text.data.strip(), 
                post=post)
            return redirect("/posts/{}".format(post_id))
        return render_template('post.html', post=post, comments=comments, form=form)

# Comment Routes
@app.route('/comments', methods=['GET', 'POST'])
@app.route('/comments/<id>', methods=['GET', 'POST'])

def comments(id=None):
    if id == None:
        comments = models.Comment.select().limit(100)
        return render_template('comments.html', comments=comments)
    else:
        comment_id = int(id)
        comment = models.Comment.get(models.Comment.id == comment_id)
        return render_template('comment.html', comment=comment)
# Initialize connection before app runs
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
