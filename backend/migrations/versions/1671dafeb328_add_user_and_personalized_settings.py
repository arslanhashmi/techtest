"""Add user and personalized settings

Revision ID: 1671dafeb328
Revises: 
Create Date: 2023-12-02 21:07:38.035872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1671dafeb328'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personalization_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_disabled', sa.Boolean(), nullable=False),
    sa.Column('name', sa.Enum('LINKEDIN_BIO', 'TOTAL_EXPERIENCE', 'CURRENT_EXPERIENCE', 'LIST_OF_PAST_JOBS', 'CURRENT_JOB_DESCRIPTION', 'CURRENT_JOB_SPECIALTIES', name='settings_type'), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('value', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personalization_settings')
    op.drop_table('users')
    # ### end Alembic commands ###
