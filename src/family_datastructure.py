"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": last_name,
            "age":33,
            "gender":"male",
            "lucky_numbers":[7, 13, 22]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id']=self._generateId()
        self._members.append(member)

        return member

    def delete_member(self, id):
        # fill this method and update the return
        self._members = list(filter(lambda member: member['id']!=id,self._members))

        return None

    def update_member(self, id, member):
        # fill this method and update the return
        return None

    def get_member(self, id):
        # fill this method and update the return
        member= next(filter(lambda member: member['id']==id,self._members),None)

        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        respuesta={}
        respuesta['members']=self._members
        respuesta['family_name']=self.last_name
        respuesta['lucky_numbers']=[]
        respuesta['sum_of_lucky']=''
        suma=0
        for x in self._members:

            for num in x['lucky_numbers']:

                    respuesta['lucky_numbers'].append(num)
                    suma=suma+num
            respuesta['sum_of_lucky']=suma

        return respuesta