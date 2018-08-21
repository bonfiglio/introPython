from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from flask_sqlalchemy import SQLAlchemy

# $ pip install flask_sqlalchemy
db = SQLAlchemy()


class Volo(db.Model):
    __tablename__ = "voli"
    id = Column(Integer, primary_key=True)
    origin = Column(String(20), nullable=False)
    destination = Column(String(20), nullable=False)
    duration = Column(Integer, nullable=False)


class Passeggero(db.Model):
    __tablename__ = "passeggeri"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    id_volo = Column(Integer, ForeignKey("voli.id"), nullable=False)

    def __repr__(self):
        return ('<Passeggero   %r - %i>' % (self.name, self.id))
