from peewee import  *
import datetime

db = SqliteDatabase("orders.db", pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    phone = CharField()
    hostel = CharField()
    room_number = CharField()
    access_pin = CharField()
    username = CharField()



class Food(BaseModel):
    name = CharField(unique=True)
    is_available = BooleanField(default=True)
    price = CharField()


class Order(BaseModel):
    user = ForeignKeyField(User, backref="orders")
    date = DateField(default=datetime.date.today())
    closed = BooleanField(default=False)

class OrderItem(BaseModel):
    order = ForeignKeyField(Order, backref='orderItems')
    food = ForeignKeyField(Food, backref="foods")
    quantity = IntegerField()

def create_db():
    with db:
        try:
            db.create_tables([User, Food, Order, OrderItem])
        except db.DatabaseError as e:
            print(f"{e}")
        