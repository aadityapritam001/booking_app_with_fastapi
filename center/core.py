import sqlalchemy
from fastapi import status, HTTPException
from center.models import Center
from center import schema

async def insert_center_data(db, center_data):
    try:
        new_center =  Center(
            id = center_data.id,
            name = center_data.name,
            location = center_data.location,
            description = center_data.description,
            amenities = center_data.amenities,
            timing = center_data.timing,
            is_occupied = False
        )
        db.add(new_center)
        db.commit()

    except sqlalchemy.exc.IntegrityError:
       db.rollback()
       raise HTTPException(
           status_code = 409,
           detail = "Center already exist !"
       )

    except Exception as ex:
        db.rollback()
        raise HTTPException(
           status_code = 409,
           detail = f"Error in inserting new center: {ex}"
       )
    
    else:
        return new_center
        
