import mysql.connector


class Connection:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        database = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return database

    def insert_hentai(self, connect, link, date, id_admin, id_category):
        cursor = connect.cursor()
        sql = 'INSERT INTO photo(link, Date, id_admin, id_category) values (%s, %s, %s, %s)'
        param = (link, date, id_admin, id_category,)
        cursor.execute(sql, param)
        connect.commit()

        
    def select_nude(self, connect):
        cursor = connect.cursor()
        cursor.execute('SELECT link FROM photo where id_category = 1 ORDER BY RAND() LIMIT 1')
        result = cursor.fetchone()
        return result[0]

    def select_hentai(self, connect):
        cursor = connect.cursor()
        cursor.execute('SELECT link FROM photo where id_category = 2 ORDER BY RAND() LIMIT 1')
        result = cursor.fetchone()
        return result[0]

    def show_selected(self, connect):
        cursor = connect.cursor()
        cursor.execute('SELECT COUNT(*) FROM photo where id_category = 1')
        result = cursor.fetchone()
        return result[0]

    def show_command(self, connect):
        commands = []
        cursor = connect.cursor()
        cursor.execute('SELECT code, description FROM command')
        result = cursor.fetchall()
        for x in result:
            commands.append(f'`{x[0]} -> {x[1]}`')
            print(x)

        return '\n'.join(commands)


    def check_username(self, connect, username):
        cursor = connect.cursor()
        cursor.execute('SELECT username_discord from discord_user')
        result = cursor.fetchall()
        for x in result:
            if x[0] in username:
                return True
        return False

    def add_use(self, connect, username):
        cursor = connect.cursor()
        sql = 'INSERT INTO discord_user(username_discord, id_admin) values(%s, 1)'
        param = (username,)
        cursor.execute(sql, param)
        connect.commit()

    def status_lol(self, connect, username):
        cursor = connect.cursor()
        sql = "SELECT username_lol FROM lol_status LEFT JOIN discord_user ON discord_user.id = lol_status.id_discord where discord_user.username_discord = %s"
        val = (username,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def bot_afk(self, connect):
        cursor = connect.cursor()
        cursor.execute('select response from emote_bot_response where tag_id=2 ORDER BY RAND() limit 1')
        result = cursor.fetchone()
        return result[0]

    def status_lust(self, connect, username):
        cursor = connect.cursor()
        sql = "SELECT points from bot_points a LEFT JOIN discord_user b ON a.id_user = b.id where b.username_discord = %s"
        val = (username,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def general_status(self, connect, pattern):
        cursor = connect.cursor()
        sql = "SELECT distinct response.response from emote_bot_response response LEFT JOIN emote_bot_tag tag ON response.tag_id = tag.id LEFT JOIN emote_bot_patterns patterns ON patterns.tag_id = tag.id  where patterns.patterns = %s order by RAND() limit 1"
        val = (pattern,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return result[0]
        return ''

    def patterns_keys(self, connect, pattern):
        cursor = connect.cursor()
        sql = "SELECT distinct patterns.patterns from emote_bot_patterns patterns where patterns.patterns = %s"
        val = (pattern,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0

    def dex(self, connect, word, definition):
        cursor = connect.cursor()
        sql = 'INSERT INTO dex(word, definition) values(%s, %s)'
        val = (word, definition,)
        cursor.execute(sql, val)
        connect.commit()

    def check_dex(self, connect, word):
        cursor = connect.cursor()
        sql = 'SELECT word from dex where word = %s'
        val = (word,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return True
        return False

    def count_dex(self, connect):
        cursor = connect.cursor()
        sql = 'SELECT count(*) from dex'
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]

    def get_point_lust(self, connect, username):
        cursor = connect.cursor()
        sql = "SELECT points from bot_points b LEFT JOIN discord_user a ON a.id = b.id_user where a.username_discord = %s"
        val = (username,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def get_id_user(self, connect,id_user):
        cursor = connect.cursor()
        sql = 'SELECT id_user from bot_points b LEFT JOIN  discord_user a ON a.id = b.id_user where a.username_discord = %s'
        val = (id_user,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def update_points(self, connect, value, username):
        cursor = connect.cursor()
        sql = 'UPDATE bot_points set points = %s where id_user = %s'
        val = (value, username,)
        cursor.execute(sql, val)
        connect.commit()

    def select_function_code_by_id(self, connect, id):
        cursor = connect.cursor()
        sql = 'SELECT code from functions where id = %s'
        val = (id, )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def select_function_code_by_title(self, connect, title):
        cursor = connect.cursor()
        sql = 'SELECT code from functions where title = %s'
        val = (title, )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def select_function_description_by_id(self, connect, id):
        cursor = connect.cursor()
        sql = 'SELECT description from functions where id = %s'
        val = (id, )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def select_function_description_by_title(self, connect, title):
        cursor = connect.cursor()
        sql = 'SELECT description from functions where title = %s'
        val = (title, )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def select_function_title_by_id(self, connect, id):
        cursor = connect.cursor()
        sql = 'SELECT title from functions where id = %s'
        val = (id, )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]


    def select_function_title_by_title(self, connect, title):
        cursor = connect.cursor()
        sql = 'SELECT title from functions where title = %s'
        val = (title, )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]
