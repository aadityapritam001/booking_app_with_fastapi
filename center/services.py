from center import core,schema


async def add_center(db,center_data):
    center_add_resp = await core.insert_center_data(db,center_data)
    return schema.Center.model_validate(center_add_resp.to_dict())
    

