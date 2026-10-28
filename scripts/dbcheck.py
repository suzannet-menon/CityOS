import asyncio, os, asyncpg
from urllib.parse import urlsplit

s = urlsplit(os.environ["DATABASE_URL"])

async def m():
    c = await asyncpg.connect(host=s.hostname, port=s.port, user=s.username,
                              password=s.password, database="postgres", timeout=20)
    print("alembic:", await c.fetchval("select version_num from alembic_version"))
    rows = await c.fetch(
        "select impersonated_user_id is not null from pg_roles limit 0") if False else await c.fetch(
        "select column_name from information_schema.columns "
        "where table_name='road_segments' and column_name like '%shade%'")
    print("shade columns left:", rows)
    print("road_segments count:", await c.fetchval("select count(*) from road_segments"))
    n_shade = None
    try:
        n_shade = await c.fetchval("select count(*) from road_segments where shade_score is not null")
    except Exception as e:
        n_shade = f"(column absent: {type(e).__name__})"
    print("shade populated:", n_shade)
    cats = await c.fetch("select code from report_categories")
    print("report categories:", sorted(r[0] for r in cats))
    print("safety_zones count:", await c.fetchval("select count(*) from safety_zones"))
    print("incident_reports count:", await c.fetchval("select count(*) from incident_reports"))
    print("wards count:", await c.fetchval("select count(*) from wards"))
    obs = await c.fetch("select table_name from information_schema.tables where table_name ilike '%observ%' or table_name ilike '%comfort%'")
    print("comfort-ish tables:", obs)
    await c.close()

asyncio.run(m())
