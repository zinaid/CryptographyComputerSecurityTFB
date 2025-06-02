# AUTH SECURITY - KNOWN ATTACKS AND SECURITY PRACTICES

## ENVIRONMENT SETUP

Create app.py file and templates folder with a file login.html. Login file should contain:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
</head>
<body>
  <h2>Login</h2>
  <form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br><br>

    <label>Password:</label>
    <input type="password" name="password" required><br><br>

    <button type="submit">Login</button>
  </form>
</body>
</html>
```

For backend we will use Flask - that is a minimal Python framework for creating simple web apps.

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"<h3>Welcome, {username}!</h3><p>Your password is: {password}</p>"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
```

## POTENTIAL THREATS

* Cross Site Scripting XSS
* Cross Site Forgery Request CSRF
* Session Hijacking
* Insecure Password storing
* SQL Injection
* Brute Force attack
* Credential Stuffing

### XSS

XSS (Cross-Site Scripting) is an attack where malicious JavaScript is injected into a website. If the site does not sanitize user input, this script will be executed by the browser of other users who visit the page.

What is a main point: Inject malicious javascript code through forms.

Example: Instead of username enter this code:

```js
<script>alert('XSS')</script>
```

Why is dangerous:
* Session Hijacking
* Key logging
* Fake Login Forms
* Browser Exploits or Worms

How to fix:

One thing that we can do is use Template Escaping. Popular library for Python is Jinja2 templates. They automatically escape special signs and characters.

Add this below form:
```html
{% if username %}
    <h3>Welcome, {{ username }}</h3>
{% endif %}
```

Change app.py

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    username = ""
    if request.method == "POST":
        username = request.form["username"]
    return render_template("login.html", username=username)
```

Try to avoid outputting html from python. Now if we try to enter:

```js
<script>alert('XSS')</script>
```

we have no problem.

1. Reflected XSS
Description:
Malicious input is reflected immediately in the response.

Example:

```js
https://yourapp.com/search?q=<script>alert('XSS')</script>
```
Danger:
Script runs instantly when the URL is visited.

2. Stored XSS
Description:
Malicious input is saved (e.g., in a comment) and shown to other users later.

Example Input:

```js
Great post! <script>alert('Hacked!')</script>
```
Danger:
Every visitor sees the attack and script execution.

3. XSS via Attributes
Example:

```html
<img src="x" onerror="alert('Image XSS')">
```
Danger:
Runs JavaScript when an image fails to load.

4. XSS via Inline Events
Example:

```html
<button onclick="alert('clicked')">Click me</button>
```
Danger:
JavaScript runs when the element is interacted with (e.g., click).

5. DOM-Based XSS
Example:

```js
const search = location.hash.substring(1);
document.body.innerHTML = search;
```
URL:
```html
https://yourapp.com/#<img src=x onerror=alert(1)>
```
Danger:
JavaScript reads untrusted data from the URL and injects it into the page.

Protection Tips
Always escape user input in templates (e.g., {{ username }} in Jinja2).

Sanitize any dynamic HTML before inserting it into the DOM.

Avoid using innerHTML unless absolutely necessary.

Never assume filtering out script tags is enough—other tags can also execute code.

### CSRF (Cross-Site Request Forgery) Attack and Protection

Cross-Site Request Forgery (CSRF) tricks a logged-in user into submitting a request (like a form) to your app without their consent, abusing browser behavior.

Example of an Insecure Flask Route
```py
@app.route("/transfer", methods=["POST"])
def transfer():
    to = request.form["to"]
    amount = request.form["amount"]
    # Process the transfer (no CSRF protection)
    return f"Transferred {amount} to {to}"
```

Insecure Form:
```html
<form action="/transfer" method="POST">
    <input type="text" name="to" placeholder="Recipient">
    <input type="text" name="amount" placeholder="Amount">
    <button type="submit">Transfer</button>
</form>
```
How an Attack Works
A malicious site could include:

```html
<img src="https://yourapp.com/transfer?to=hacker&amount=1000">
```

The browser automatically sends the user's cookies/session, performing the transfer without their consent.

Fixing CSRF with Flask-WTF
1. Install Flask-WTF:
```
pip install Flask-WTF
```
2. Define a Secure Form:

```py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TransferForm(FlaskForm):
    to = StringField('To', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
```
3. Set up the app:
```bash
app.config['SECRET_KEY'] = 'your-secret-key'
```

4. Use in Template:

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.to.label }} {{ form.to() }}
    {{ form.amount.label }} {{ form.amount() }}
    <button type="submit">Transfer</button>
</form>
```

{{ form.hidden_tag() }} automatically includes a CSRF token.

Key Points

CSRF tricks the browser into making unauthorized requests.

Always include a token in your forms that the attacker cannot predict.

Flask-WTF provides automatic CSRF protection with form.hidden_tag().

### SESSION HIJACKING

Session hijacking is when an attacker steals or guesses a valid session identifier (session ID) to impersonate a user and take over their session.

The attacker does not need your password—just your session cookie to act as if they were you.

How It Happens:

Session ID in URLs
If session IDs are passed in the URL (e.g., /profile?sessionid=abc123), they can be leaked via:

* Browser history

* Referer headers

* Server logs

* Insecure Cookies (No HTTPS)

If your app is not using secure cookies (missing Secure and HttpOnly flags), session IDs can be:

* Sniffed over insecure networks (e.g., public Wi-Fi)

* Cross-Site Scripting (XSS)

XSS can allow an attacker to read cookies if HttpOnly is not set.

* Physical Access
If someone has access to your device, they can steal session cookies from your browser.

Example Attack (Sniffing Cookies)

If your app is using HTTP (not HTTPS):

The attacker sets up a packet sniffer (like Wireshark).

You log in; your session cookie is sent unencrypted.

The attacker grabs the cookie and uses it to hijack your session.

Flask Example of an Insecure Session
```py
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    return redirect('/dashboard')
```

Without HTTPS and proper cookie flags, this is vulnerable to session hijacking.

How to Protect Against Session Hijacking
* Always Use HTTPS

* Force all connections to use HTTPS:

```py
@app.before_request
def before_request():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"))
```

* Set Secure Cookie Flags

* Configure session cookies securely:

```py
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,  # Prevent JavaScript access
    SESSION_COOKIE_SECURE=True,    # Only over HTTPS
    SESSION_COOKIE_SAMESITE='Lax'  # Prevent cross-site requests
)
```

* Regenerate Session IDs

Regenerate session ID after login to prevent session fixation:

```py
from flask import session

@app.route('/login', methods=['POST'])
def login():
    session.clear()
    username = request.form['username']
    session['username'] = username
    return redirect('/dashboard')
```

* Short Session Lifetimes

* Limit session duration:

```py
from datetime import timedelta

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
```

Security Tips

* Never pass session IDs in URLs.

* Always use HTTPS.

* Set cookies to Secure + HttpOnly + SameSite.

* Regenerate session IDs after login.

* Limit session duration.

### Insecure Password Storing

#### What Is It?

Insecure password storing happens when passwords are **saved in plain text** or using **weak hashing algorithms** in a database.

If your database is breached, attackers can immediately see or easily crack user passwords.

---

#### Why Is It Dangerous?

- **Plaintext passwords** expose every user immediately.
- **Weak hashes** (like MD5 or SHA1) are fast to compute, allowing attackers to brute-force them quickly.
- Users often **reuse passwords** across services—breaching one service can lead to wider compromise.

---

#### Example of Insecure Password Storing

```python
# Insecure: storing password as plaintext
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User(username=username, password=password)  # BAD
    db.session.add(user)
    db.session.commit()
    return 'User registered'
```

Or using a weak hash:


```py
import hashlib

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.md5(password.encode()).hexdigest()  #  BAD
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return 'User registered'
```

How to Store Passwords Securely

* Use a Strong Password Hashing Algorithm

Recommended: werkzeug.security (built-in with Flask) or bcrypt.

Example using werkzeug.security:

```py
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return 'User registered'

```

* Verify Passwords Correctly

Example:

```py
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Login success
        return 'Logged in'
    else:
        return 'Invalid credentials'

```

Why This Works
* pbkdf2:sha256 is a slow, computationally expensive hash.

* Salting makes each password hash unique, even if two users have the same password.

* Using standard, battle-tested libraries reduces risk of errors.

Bonus Tips
* Rate-limit login attempts to prevent brute-force attacks.

* Enforce strong password policies (minimum length, complexity).

Security Tips
* Never store passwords in plaintext.

* Never use fast hashes like MD5 or SHA1.

* Always use slow, salted hashes like pbkdf2:sha256, bcrypt, or argon2.

* Use trusted libraries for hashing and verification.