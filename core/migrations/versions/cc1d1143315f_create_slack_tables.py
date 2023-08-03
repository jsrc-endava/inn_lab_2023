"""create slack tables

Revision ID: cc1d1143315f
Revises: 
Create Date: 2023-08-01 22:02:46.978411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc1d1143315f'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade() -> None:
  op.create_table(
    'slack_messages',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('message_id', sa.String(50), nullable=False),
    sa.Column('channel_id', sa.String(50)),
    sa.Column('user_id', sa.String(50)),
    sa.Column('team_id', sa.String(50)),
    sa.Column('username', sa.String(50)),
    sa.Column('text', sa.Unicode(500), nullable=False),
  )


def downgrade() -> None:
  op.drop_table('slack_messages')
