from fastapi import Header, HTTPException


async def get_token_header(internal_header: str = Header()):
    if internal_header != "allowed":
        raise HTTPException(status_code=400, detail="Internal-Token header invalid")