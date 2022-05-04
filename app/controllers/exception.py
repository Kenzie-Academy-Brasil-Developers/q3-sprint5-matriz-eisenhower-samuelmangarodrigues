
def excepts(data):
    if data['importance']!=1 or data['importance']!=2:

        return{
            "msg": {
                "valid_options": {
                "importance": [1, 2],
                "urgency": [1, 2]
                },
                "recieved_options": {
                "importance": data['importance'],
                "urgency": data['urgency']
                }
            }
        }


        
    if data['urgency']!=1 or data['urgency']!=2:

        return{
            "msg": {
                "valid_options": {
                "importance": [1, 2],
                "urgency": [1, 2]
                },
                "recieved_options": {
                "importance": data['importance'],
                "urgency": data['urgency']
                }
            }
        }
    if type(data['urgency']) != int:
        return {"msg":"Only integer values"}

    if type(data['importance']) != int:
        return {"msg":"Only integer values"}  
