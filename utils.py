from db_manager import DatabaseManager

class UserManager:
    def __init__(self, db_path):
        self.db = DatabaseManager(db_path)

    def register(self, email, password):
        existing_user = self.db.fetch_query("SELECT * FROM users WHERE email = ?", (email,))
        if existing_user:
            return False
        self.db.execute_query("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        return True

    def login(self, email, password):
        user = self.db.fetch_query("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        return bool(user)

class EventManager:
    def __init__(self, db_path):
        self.db = DatabaseManager(db_path)

    def add_event(self, name, location, date):
        self.db.execute_query("INSERT INTO events (name, location, date) VALUES (?, ?, ?)", (name, location, date))

    def edit_event(self, event_id, new_name, new_location, new_date):
        self.db.execute_query("UPDATE events SET name = ?, location = ?, date = ? WHERE id = ?", (new_name, new_location, new_date, event_id))

    def delete_event(self, event_id):
        self.db.execute_query("DELETE FROM events WHERE id = ?", (event_id,))

class CourseManager:
    def __init__(self, db_path):
        self.db = DatabaseManager(db_path)

    def add_course(self, title, description, file_path):
        self.db.execute_query("INSERT INTO courses (title, description, file_path) VALUES (?, ?, ?)", (title, description, file_path))

    def edit_course(self, course_id, new_title, new_description):
        self.db.execute_query("UPDATE courses SET title = ?, description = ? WHERE id = ?", (new_title, new_description, course_id))

    def delete_course(self, course_id):
        self.db.execute_query("DELETE FROM courses WHERE id = ?", (course_id,))
