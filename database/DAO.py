from database.DB_connect import DBConnect
from model.objects import Object
from model.connessione import Connessione


class DAO:
    @staticmethod
    def getAllObjects():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM objects
                """
        cursor.execute(query, )
        for row in cursor:
            result.append(Object(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT eo1.object_id as obj1, eo2.object_id as obj2
                FROM exhibition_objects eo1, exhibition_objects eo2
                WHERE eo2.exhibition_id = eo1.exhibition_id
                AND eo1.object_id < eo2.object_id
                """
        cursor.execute(query)
        for row in cursor:
            result.append(Connessione(idMap[row['obj1']], idMap[row['obj2']]))
        cursor.close()
        conn.close()
        return result
