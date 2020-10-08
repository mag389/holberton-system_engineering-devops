# Application servers

an application can be thought of as akin to a web server, but instead of serving web pages
or static data, an application server delivers dynamic content, usually interactable.

In the case of this project the dynamic content takes the form of an Airbnb clone running on a server.

For this project I use the Gunicorn application server program.`

additionally for starting multiple instances of gunicorn tmux is very useful.
for instance:
'tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
to create an instance for using the even or odd route with gunicorn.

since the instance is in the background pgrep becomes very useful.
for instance: if you started a tmux instance of gunicorn you can see them with 'pgrep gunicorn'
that returns a list of gunicorn pid's which can then be used to kill those processes.
