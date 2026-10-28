"""Remove shade columns from road_segments

The tree-canopy shade concept (step 7) was removed from the project.
This migration is a no-op on fresh databases and drops the columns on
databases that still carry them.

Revision ID: 0006
Revises: 0005
Create Date: 2026-10-28
"""

from alembic import op

revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE road_segments DROP COLUMN IF EXISTS shade_updated_at;")
    op.execute("ALTER TABLE road_segments DROP COLUMN IF EXISTS shade_source;")
    op.execute("ALTER TABLE road_segments DROP COLUMN IF EXISTS shade_score;")


def downgrade():
    pass
