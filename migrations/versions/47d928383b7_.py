"""empty message

Revision ID: 47d928383b7
Revises: 
Create Date: 2019-09-30 11:22:38.472124

"""

#'ARRAY',
# 'BIGINT',
# 'BIT',
# 'BOOLEAN',
# 'BYTEA',
# 'CHAR',
# 'CIDR',
# 'DATE',
# 'DATERANGE',
# 'DOUBLE_PRECISION',
# 'ENUM',
# 'FLOAT',
# 'HSTORE',
# 'INET',
# 'INT4RANGE',
# 'INT8RANGE',
# 'INTEGER',
# 'INTERVAL',
# 'JSON',
# 'NUMERIC',
# 'NUMRANGE',
# 'OID',
# 'REAL',
# 'SMALLINT',
# 'TEXT',
# 'TIME',
# 'TIMESTAMP',
# 'TSRANGE',
# 'TSTZRANGE',
# 'TSVECTOR',
# 'UUID',
# 'VARCHAR',


# revision identifiers, used by Alembic.
revision = '47d928383b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
#    op.create_table(
#        'employees',
#        sa.Column('id', sa.Integer, primary_key=True),
#        sa.Column('email', VARCHAR(200), index=True),
#        sa.Column('username', VARCHAR(200), index=True, uniqe=True),
#        sa.Column('first_name', VARCHAR(200), index=True, uniqe=True),
#        sa.Column('last_name', VARCHAR(200), index=True),
#        sa.Column('password_hash', VARCHAR(200)),
#        sa.Column('is_admin', BOOLEAN, nullable=True),
#        sa.Column('department_id', sa.Integer, nullable=True),
#        sa.Column('role_id', sa.Integer, nullable=True),
#        sa.ForeignKeyConstraint(['department_id'], ['employees.id'], ondelete='CASCADE'),
#        sa.ForeignKeyConstraint(['role_id'], ['employees.id'], ondelete='CASCADE')
#        )
    #    id = db.Column(db.Integer, primary_key=True)
    #    email = db.Column(db.String(60), index=True, unique=True)
    #    username = db.Column(db.String(60), index=True, unique=True)
    #    first_name = db.Column(db.String(60), index=True)
    #    last_name = db.Column(db.String(60), index=True)
    #    password_hash = db.Column(db.String(128))
    #    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    #    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #    is_admin = db.Column(db.Boolean, default=False)
    pass
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
