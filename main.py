import webapp2 
import re
import cgi 

form="""
<form method="post">
    <h2>User Signup</h2>
    <table>
        <tbody>
            <tr>
                <td><label>Username: </label></td>
                <td>
                    <input type ="text" name="username" value="%(username)s">
                    <span style="color: red" class="error">%(u_error)s</span>
                </td>
            </tr>
            <tr>
                <td><label>Password: </label></td>
                <td>
                    <input type ="password" name="password" value="">
                    <span style="color: red" class="error">%(pw_error)s</span>
                </td>
            </tr>
            <tr>
                <td><label>Confirm password:</label></td>
                <td>
                    <input type="password" name="confirm" value="">
                    <span style="color: red" class="error">%(cf_error)s</span>
                </td>
            </tr>
            <tr>
                <td><label>Email (optional): </label></td>
                <td>
                    <input name="email" type="email" value="%(email)s">
                    <span style="color: red" class="error">%(em_error)s</span>
                </td>
            </tr>
        </tbody>
    </table>
    <input type="submit">
</form>
"""
def escape_html(s):
    return cgi.escape(s, quote=True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile("^.{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return username and USER_RE.match(username) #might not need username, ie: return USER-RE...

def valid_password(password):
    return password and PASS_RE.match(password)

def valid_confirm(confirm):
    return confirm and PASS_RE.match(confirm)

def valid_email(email):
    return email or EMAIL_RE.match(email)

user_err="Invalid username"
pass_err="Invalid password"
conf_err="Passwords no not match"
email_err="Invalid email address"
       
class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="", email="", u_error="", pw_error="", cf_error="", em_error="" ):  #function to write form
        self.response.out.write(form % {"username": escape_html(username),
                                        "email": escape_html(email),
                                        "u_error": u_error,
                                        "pw_error": pw_error,
                                        "cf_error": cf_error,
                                        "em_error":em_error}) 
    def get(self):
        self.write_form() #this is what draws the EMPTY form
                            #no error message(s) here, this is initial
                            #form writing

    def post(self): #gets called when posting to the URL / which...
                    #...is what happens when you submit a form
        username=self.request.get('username')
        password=self.request.get('password')
        confirm=self.request.get('confirm')
        email=self.request.get('email')
        
        have_username_error, have_password_error, have_confirm_error, have_email_error= False, False, False, False
        
        u_error, pw_error, cf_error, em_error= "","","",""

        if not valid_username(username):
            have_username_error=True
        if not valid_password(password):
            have_password_error=True
        if not valid_confirm(confirm):
            have_confirm_error=True
        if not valid_email(email) and email:
            have_email_error=True
        
        if password==confirm:
            match=True
        else:
            match=False

        if (not have_username_error and not have_password_error and not have_confirm_error and not have_email_error) and match:
            self.redirect("/thanks?username=" + username)
        else:
            if have_username_error:
                u_error=user_err
            if have_password_error:
                pw_error=pass_err
            if not match:
                cf_error=conf_err
            if have_email_error:
                em_error=email_err
                    
        
        self.write_form(username, email, u_error, pw_error, cf_error, em_error)
        
        

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        username=self.request.get('username')
        if valid_username(username):
            self.response.out.write("Thank you for signing up, %s" %username)
        else:
            self.redirect('/')


app = webapp2.WSGIApplication([('/', MainHandler), ('/thanks', ThanksHandler)], debug=True)


