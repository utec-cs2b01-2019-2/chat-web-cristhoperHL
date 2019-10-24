

class Message(connector.Manager.Base):
    __tablename__='messages'
class Group(connector.Manager.Base):
    __tablename__= "groups"
    id=Column(Integer,Sequence('grouos_id_seq'),primary_key=True)
    name=Column(String(500))