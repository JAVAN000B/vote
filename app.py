# Author1: FENGJIE GU (22268194)
# Author2: MINGHUI SUN (22140595)

# Compile using python3
# Our database file (data.db) was built in the project folder
# However, following the submission requirement, we put an additional data.db in the .zip file
# There is also another database file test.db in project folder using for unit_test
import flask_admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, session, flash
from sqlalchemy.sql.functions import current_user

from project import app
from flask_admin import Admin, AdminIndexView, expose
from project import db
from project import database


newAdmin = Admin(
    app,
    index_view=AdminIndexView(
        template='adminIndex.html',
        url='/admin'
    )
)
app.config['FLASK_ADMIN_SWATCH'] = 'Cosmo'


newAdmin.add_view(ModelView(database.game_info, db.session))
newAdmin.add_view(ModelView(database.log, db.session))
newAdmin.add_view(ModelView(database.user_info, db.session))
newAdmin.add_view(ModelView(database.voted_info, db.session))
newAdmin.add_view(ModelView(database.question_info, db.session))


app.debug = True
if __name__ == '__main__':
    app.run()
