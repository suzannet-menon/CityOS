"""Remove heat and shade observation categories

The comfort/heat/shade concept (step 8) was removed from the project.
This migration is a no-op on fresh databases and purges the categories on
databases that still carry them.

Revision ID: 0007
Revises: 0006
Create Date: 2026-10-28
"""

from alembic import op

revision = "0007"
down_revision = "0006"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        DELETE FROM report_categories
        WHERE code IN (
            'no_shade',
            'shade_obstruction',
            'heat_stress',
            'cool_spot'
        );
        """
    )


def downgrade():
    pass
