import psycopg2

class PostgreSQLPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        port = '5432'
        database = 'sreality'
        username = 'postgres'
        password = ''

        self.connection = psycopg2.connect(
            host=hostname,
            port=port,
            dbname=database,
            user=username,
            password=password
        )
        self.cursor = self.connection.cursor()
        query = "TRUNCATE TABLE offers RESTART IDENTITY;"
        self.cursor.execute(query)
       
        self.connection.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        query = "INSERT INTO offers (title, locality, images) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (item['title'], item['locality'], item['images_url']))
       
        self.connection.commit()

        return item
