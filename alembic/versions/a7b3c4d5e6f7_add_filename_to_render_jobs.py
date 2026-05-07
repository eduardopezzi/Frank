"""add_filename_to_render_jobs

Revision ID: a7b3c4d5e6f7
Revises: 62260655d642
Create Date: 2026-05-02 19:43:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7b3c4d5e6f7'
down_revision: Union[str, None] = '62260655d642'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('render_jobs', sa.Column('original_filename', sa.String(), nullable=True))
    op.add_column('render_jobs', sa.Column('file_size', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('render_jobs', 'file_size')
    op.drop_column('render_jobs', 'original_filename')
