"""005_create_emailtemplate_model

Revision ID: 281fe118be6c
Revises: c4472aa49f8b
Create Date: 2024-12-10 17:10:59.929692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '281fe118be6c'
down_revision: Union[str, None] = 'c4472aa49f8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
