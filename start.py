from sber import app, db
from sber import routes
from inner_db import inner

db.create_all()
inner()
app.run(debug=True, host="0.0.0.0", port="3000")
