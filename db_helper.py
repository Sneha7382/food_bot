import mysql.connector
global cnx
cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sneha@135",
        database="pandeyji_eatery"
    )
print("global function is exceuting")

def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query="insert into order_tracking (order_id,status) values (%s, %s)"


    cursor.execute(insert_query, (order_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()


def get_total_order_price(order_id):
    cursor=cnx.cursor()

    query=f"select get_total_order_price({order_id})"

    cursor.execute(query)

    result = cursor.fetchone()[0]

    cursor.close()
    return result

def insert_order_item(food_item, quantity, order_id):
    try:
        cursor=cnx.cursor()

        cursor.callproc('insert_order_item',(food_item, quantity, order_id))

        cnx.commit()

        cursor.close()

        print("order item inserted successfully")

        return 1
    except mysql.connector.Error as err:
        print(f"Error in inserting order item:{err}")

        cnx.rollback()
        return  -1

    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()

        return -1




def get_next_order_id():
    cursor=cnx.cursor()

    query="select MAX(order_id) from orders"
    cursor.execute(query)

    result = cursor.fetchone()[0]
    cursor.close()

    if result is None:
        return 1
    else:
        return result+1

# Function to call the MySQL stored procedure and insert an order item
def get_order_status( order_id:int):

    cursor=cnx.cursor()

    query=("select status from order_tracking where order_id=%s")

    cursor.execute(query,(order_id,))

    result=cursor.fetchone()

    cursor.close()


    if result is not None:
        return result[0]
    else:
        return None




