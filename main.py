import webapp2 
import re

form="""
<form method="post">
    <h2>User Signup</h2>
    <table>
        <tbody>
            <tr>
                <td>
                    <label>Username: </label>
                </td>
                <td>
                    <input type ="text" name="username" value="%(username)s">
                    
                </td>
                <td>
                    <div style="color: red" class="username_error">%(username_error)s</div>
                </td>
            </tr>
        </tbody>
    </table>
    <input type="submit">
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

       
class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="", username_error=""):  #function to write form
        self.response.out.write(form % {"username": username,
                                        "username_error": username_error}) 
    def get(self):
        self.write_form() #this is what draws the EMPTY form
                            #no error message here, this is initial
                            #form writing

    def post(self): #gets called when posting to the URL / which...
                    #...is what happens when you submit a form
        user_name=self.request.get('username')
        
        uname=valid_username(user_name)

        if not uname:
            self.write_form(user_name, "no bueno") #draws form w/ error message
        else: #if true, thank you message
            self.response.out.write("Thank you for signing up!")


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)


