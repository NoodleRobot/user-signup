import webapp2

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">User Signup</a>
    </h1>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):

      add form = """
      <form method="post">
        <table>
            <tbody>
                <tr>
                    <td>
                        <label for="username">Username:</label>
                    </td>
                    <td>
                        <input type="text" name="username" value required/>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td>    
                        <label for="password">Password:</label>
                    </td>

                    <td>
                        <input type="text" name="password"/>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="confifm">Confirm password:</label>
                    </td>
                    <td>
                        <input type="text" name="confirm"/>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="email">Email (optional):</label>
                    </td>
                    <td>
                        <input type="text" name="email"/>
                        <span class="error"></span>
                    </td>
                </tr>
            </tbody>
        </table>
        <input type="submit">
      </form>

      




















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
