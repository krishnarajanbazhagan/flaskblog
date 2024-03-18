"""
This file contains the main function
"""

from modules import currentTimeStamp
from modules import Flask
from routes.post import postBlueprint  
from routes.user import userBlueprint  
from routes.index import indexBlueprint  
from routes.login import loginBlueprint  
from routes.about import aboutBlueprint  
from routes.signup import signUpBlueprint  
from routes.logout import logoutBlueprint  
from routes.search import searchBlueprint  
from routes.category import categoryBlueprint  
from routes.editPost import editPostBlueprint  
from routes.searchBar import searchBarBlueprint  
from routes.dashboard import dashboardBlueprint  
from routes.verifyUser import verifyUserBlueprint  
from routes.adminPanel import adminPanelBlueprint  
from routes.createPost import createPostBlueprint  
from routes.privacyPolicy import privacyPolicyBlueprint  
from routes.passwordReset import passwordResetBlueprint  
from routes.changeUserName import changeUserNameBlueprint  
from routes.changePassword import changePasswordBlueprint  
from routes.adminPanelUsers import adminPanelUsersBlueprint  
from routes.adminPanelPosts import adminPanelPostsBlueprint  
from routes.accountSettings import accountSettingsBlueprint  
from routes.returnPostBanner import returnPostBannerBlueprint  
from routes.adminPanelComments import adminPanelCommentsBlueprint  
from routes.changeProfilePicture import changeProfilePictureBlueprint  
from flask_wtf.csrf import CSRFProtect, CSRFError  
from utils.dbChecker import dbFolder, usersTable, postsTable, commentsTable
from modules import (
    DEBUG_MODE, APP_NAME, APP_HOST, APP_PORT, SESSION_PERMANENT,
    APP_VERSION, APP_ROOT_PATH, STATIC_FOLDER, CUSTOM_LOGGER, APP_SECRET_KEY,
    TEMPLATE_FOLDER, WERKZEUG_LOGGER, RECAPTCHA, RECAPTCHA_SITE_KEY,
    RECAPTCHA_SECRET_KEY, RECAPTCHA_VERIFY_URL, RECAPTCHA_BADGE, DEFAULT_ADMIN,
    LOG_IN, REGISTRATION, DEFAULT_ADMIN_USERNAME, DEFAULT_ADMIN_PASSWORD,
    DEFAULT_ADMIN_PROFILE_PICTURE,
)
from modules import (
    RECAPTCHA_LOGIN, RECAPTCHA_COMMENT, RECAPTCHA_SIGN_UP, RECAPTCHA_POST_EDIT,
    RECAPTCHA_POST_DELETE, RECAPTCHA_VERIFY_USER, RECAPTCHA_DELETE_USER,
    RECAPTCHA_POST_CREATE, RECAPTCHA_COMMENT_DELETE, RECAPTCHA_PASSWORD_RESET,
    RECAPTCHA_PASSWORD_CHANGE, RECAPTCHA_USERNAME_CHANGE, RECAPTCHA_PROFILE_PICTURE_CHANGE,
)
from utils.errorHandlers.notFoundErrorHandler import notFoundErrorHandler
from utils.errorHandlers.csrfErrorHandler import csrfErrorHandler
from utils.errorHandlers.unauthorizedErrorHandler import unauthorizedErrorHandler
from utils.afterRequest import afterRequestLogger
from modules import isLogin, recaptchaBadge, isRegistration, returnUserProfilePicture

app = Flask(
    import_name=APP_NAME,
    root_path=APP_ROOT_PATH,
    static_folder=STATIC_FOLDER,
    template_folder=TEMPLATE_FOLDER,
)

app.secret_key = APP_SECRET_KEY
app.config["SESSION_PERMANENT"] = SESSION_PERMANENT

csrf = CSRFProtect(app)

app.context_processor(isLogin)
app.context_processor(recaptchaBadge)
app.context_processor(isRegistration)
app.context_processor(returnUserProfilePicture)

if not WERKZEUG_LOGGER:
    from logging import getLogger
    getLogger("werkzeug").disabled = False

if not CUSTOM_LOGGER:
    pass

dbFolder()
usersTable()
postsTable()
commentsTable()

@app.errorhandler(404)
def notFound(e):
    return notFoundErrorHandler(e)

@app.errorhandler(401)
def unauthorized(e):
    return unauthorizedErrorHandler(e)

@app.errorhandler(CSRFError)
def csrfError(e):
    return csrfErrorHandler(e)

@app.after_request
def afterRequest(response):
    return afterRequestLogger(response)

app.register_blueprint(postBlueprint)  
app.register_blueprint(userBlueprint)  
app.register_blueprint(indexBlueprint)  
app.register_blueprint(aboutBlueprint)  
app.register_blueprint(loginBlueprint)  
app.register_blueprint(signUpBlueprint)  
app.register_blueprint(logoutBlueprint)  
app.register_blueprint(searchBlueprint)  
app.register_blueprint(categoryBlueprint)  
app.register_blueprint(editPostBlueprint)  
app.register_blueprint(dashboardBlueprint)  
app.register_blueprint(searchBarBlueprint)  
app.register_blueprint(adminPanelBlueprint)  
app.register_blueprint(createPostBlueprint)  
app.register_blueprint(verifyUserBlueprint)  
app.register_blueprint(privacyPolicyBlueprint)  
app.register_blueprint(passwordResetBlueprint)  
app.register_blueprint(changeUserNameBlueprint)  
app.register_blueprint(changePasswordBlueprint)  
app.register_blueprint(adminPanelUsersBlueprint)  
app.register_blueprint(adminPanelPostsBlueprint)  
app.register_blueprint(accountSettingsBlueprint)  
app.register_blueprint(returnPostBannerBlueprint)  
app.register_blueprint(adminPanelCommentsBlueprint)  
app.register_blueprint(changeProfilePictureBlueprint)  

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT)
