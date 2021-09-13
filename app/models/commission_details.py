from app import db




class CommissionDetails(db.Model):
    """
    Create an CommissionDetails table
    """

    __tablename__ = 'commissionDetails'

    # Carrier ID	Product ID	parentID	Product Name	Class Name	Disabled?	Commission %

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    carrierID = db.Column(db.Integer, index=True, unique=True, nullable=False)
    productID = db.Column(db.Integer, index=True, unique=True, nullable=False)
    parentID = db.Column(db.Integer, index=True, unique=True, nullable=False)
    productName = db.Column(db.String(255), index=True)
    className = db.Column(db.String(255), index=True)
    isDisabled = db.Column(db.Boolean, nullable=False)
    commission = db.Column(db.Float, unique=True, nullable=False)