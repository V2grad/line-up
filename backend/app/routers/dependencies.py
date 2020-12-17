from fastapi import Header, HTTPException

'''
    We will retrieve user info here
'''


async def get_token_header(x_token: str = Header(...)):
    if x_token != "user-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
