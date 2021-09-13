from app import db




class Geo(db.Model):
    """
    Geo:
        Geo Model with base declarelation

    Args:
        db (SQLAlchemy): One is binding the instance to a very specific Flask application
        Base (declarative): Construct a base class for declarative class definitions

    Create an Geo table
    """

    __tablename__  = 'countries'
    __table_args__ = {'extend_existing': True}
    __bind_key__   = 'geodb'

    countryID            = db.Column(db.Integer, index = True, primary_key = True, nullable = False)
    country              = db.Column(db.String(255), index = True, nullable = False)
    abbr                 = db.Column(db.String(2), index = True, nullable = False)
    abbr3                = db.Column(db.String(3), index = True, nullable = False)
    country_numeric_code = db.Column(db.Integer, index = True, nullable = False)
    capital              = db.Column(db.String(255), index = True, nullable = False)
    country_demonym      = db.Column(db.String(100), index = True, nullable = False)
    total_area           = db.Column(db.Integer, index = True, nullable = False)
    population           = db.Column(db.Integer, index = True, nullable = True)
    idd_code             = db.Column(db.Integer, index = True, nullable = False)
    currency_code        = db.Column(db.String(3), index = True, nullable = True)
    currency_name        = db.Column(db.String(100), index = True, nullable = True)
    lang_code            = db.Column(db.String(3), index = True, nullable = False)
    lang_name            = db.Column(db.String(100), index = True, nullable = False)
    cctld                = db.Column(db.String(2), index = True, nullable = False)
    eu                   = db.Column(db.SmallInteger, index = True, nullable = True)
    eea	                 = db.Column(db.SmallInteger, index = True, nullable = True)
    schengen             = db.Column(db.SmallInteger, index = True, nullable = True)
    efta                 = db.Column(db.SmallInteger, index = True, nullable = True)
    commonwealth         = db.Column(db.SmallInteger, index = True, nullable = True)
    user                 = db.Column(db.String(255), index = True, nullable = False)
    timestamp            = db.Column(db.Integer, index = True, nullable = False)
    updated_at           = db.Column(db.Time, index = True, nullable = False)
