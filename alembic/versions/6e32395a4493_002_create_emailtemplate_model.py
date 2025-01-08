"""002_create_emailtemplate_model

Revision ID: 6e32395a4493
Revises: 258084e05dd4
Create Date: 2024-12-10 16:09:46.130293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e32395a4493'
down_revision: Union[str, None] = '258084e05dd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
