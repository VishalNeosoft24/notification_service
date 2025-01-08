"""006_create_emailtemplate_model

Revision ID: 834a2ff9b2d2
Revises: 281fe118be6c
Create Date: 2024-12-10 18:12:57.939801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '834a2ff9b2d2'
down_revision: Union[str, None] = '281fe118be6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
