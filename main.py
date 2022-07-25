from sqlalchemy import create_engine
engine = create_engine(
    "mysql+pymysql://root:123456@localhost:3306/sql_alchemy",
    echo=True
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
       
print (User.__table__ )

Base.metadata.create_all(engine)

# # ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# # print(ed_user.name)
# # print(ed_user.nickname)
# # print(str(ed_user.id))

# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# session.add(ed_user)

# our_user = session.query(User).filter_by(name='ed').first() 

# # print(our_user)
# # print(ed_user is our_user)

# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

# ed_user.nickname = 'eddie'
# # print(session.dirty)
# # print(session.new)

# session.commit()


# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship

# class Address(Base):
#     __tablename__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="addresses")
#     def __repr__(self):
#         return "<Address(email_address='%s')>" % self.email_address

# User.addresses = relationship(
#     "Address", order_by=Address.id, back_populates="user")

# # Base.metadata.create_all(engine)
# jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
# # print(jack.addresses)
# jack.addresses = [
#                 Address(email_address='jack@google.com'),
#                 Address(email_address='j25@yahoo.com')]
