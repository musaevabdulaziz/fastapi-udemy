from fastapi import APIRouter, Depends
from TodoApp.company.dependencies import get_token_header


router = APIRouter(prefix="/companyapis",
                   tags=["companyapis"],
                   responses={418: {"description": "Internal Use Only"}},
                   dependencies=[Depends(get_token_header)])


@router.get("/")
async def get_company_name():
    return {"company name": "Example Company, LLC"}


@router.get("/employees")
async def get_number_of_employees():
    return 2300
