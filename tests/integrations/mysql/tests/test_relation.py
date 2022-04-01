import pytest
from prisma import Prisma

COUNTY_NAME = 'Some County'
COUNTY_FIPS = 123
AGENCY_NAME = 'Some Agency'


# @pytest.mark.asyncio
# async def test_nested(client: Prisma) -> None:
#
#     agency = await client.agency.create(
#         data={
#             "name":AGENCY_NAME,
#             "county": {
#                 "create": {
#                     "name": COUNTY_NAME,
#                 },
#             }
#         }
#     )
#     assert agency.name == AGENCY_NAME
#     assert agency.county.name == COUNTY_NAME


@pytest.mark.asyncio
async def test_not_nested(client: Prisma) -> None:
    county = await client.county.create(
        data={
            'name': COUNTY_NAME,
            'fips': COUNTY_FIPS,
        }
    )
    agency = await client.agency.create(
        data={
            'name': AGENCY_NAME,
            'county_fips': county.fips,
        }
    )
    assert agency.county_fips == county.fips
