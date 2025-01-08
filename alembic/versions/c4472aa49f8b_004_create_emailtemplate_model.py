"""004_create_emailtemplate_model

Revision ID: c4472aa49f8b
Revises: 440f3481db37
Create Date: 2024-12-10 17:10:32.954540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4472aa49f8b'
down_revision: Union[str, None] = '440f3481db37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
