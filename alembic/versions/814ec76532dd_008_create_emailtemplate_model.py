"""008_create_emailtemplate_model

Revision ID: 814ec76532dd
Revises: 5281bde0cfd6
Create Date: 2024-12-10 18:14:40.446950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '814ec76532dd'
down_revision: Union[str, None] = '5281bde0cfd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
