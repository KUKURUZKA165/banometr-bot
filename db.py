import sqlite3


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id, user_tag):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        self.cursor.execute("UPDATE users SET user_tag == ? WHERE user_id = ?", (user_tag, user_id))
        return self.conn.commit()

    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def change_ban(self, user_id, ban):
        self.cursor.execute("UPDATE users SET ban == ? WHERE user_id = ?", (ban, user_id))
        return self.conn.commit()

    def check_ban(self, user_id):
        result = self.cursor.execute("SELECT `ban` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]
