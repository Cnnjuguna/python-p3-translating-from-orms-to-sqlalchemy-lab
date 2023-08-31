from models import Dog


def create_table(Base, engine):
    # Create the database tables
    Base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()


def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass


def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    # return session.query(Dog).filter_by(breed=breed).first()
    session.commit()

    pass
