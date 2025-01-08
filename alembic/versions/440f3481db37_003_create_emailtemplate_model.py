"""003_create_emailtemplate_model

Revision ID: 440f3481db37
Revises: 6e32395a4493
Create Date: 2024-12-10 17:09:11.196095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '440f3481db37'
down_revision: Union[str, None] = '6e32395a4493'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
