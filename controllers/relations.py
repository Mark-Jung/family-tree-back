from models.relations import RelationsModel
from models.user import UserModel

from datetime import datetime

class RelationsController():
    @classmethod
    def make_relation(cls, user_id, first, last, death_year, is_deceased, gender, relation, notes, is_step, is_adopted, birth_date, birth_year, lives_in, nickname):
        # if not UserModel.find_by_id(user_id):
        #     return "User with that id does not exist", 400, None
        if birth_year and birth_date:
            birth_total_str = birth_year + " " + birth_date
            birth_date = datetime.strptime(birth_total_str, '%Y %m/%d')
        elif birth_year:
            birth_date = datetime.strptime(birth_year, '%Y')
        elif birth_date:
            birth_total_str = "1000" + " " + birth_date
            birth_date = datetime.strptime(birth_total_str, '%Y %m/%d')
        else:
            birth_date = None

        if death_year:
            death_year = datetime.strptime(death_year, '%Y')
        else:
            death_year = None
        
        rln = relation[0]
        related_to = relation[1] #id
        related_to = RelationsModel.find_by_id(related_to).relation #relation
        relation_out = ""

        if rln == "self":
            relation_out == "self"

        if rln == "parent":
            if related_to == "self" or related_to == "brother" or related_to == "sister" or related_to == "sibling":
                if gender == "Male":
                    relation_out = "father"
                elif gender == "Female":
                    relation_out = "mother"
                elif gender == "Other":
                    relation_out = "parent"
            elif related_to == "parent" or related_to == "mother" or related_to == "father" or related_to == "aunt" or related_to == "uncle" or related_to == "aunt/uncle":
                if gender == "Male":
                    relation_out = "grandfather"
                elif gender == "Female":
                    relation_out = "grandmother"
                elif gender == "Other":
                    relation_out = "grandparent"
            elif related_to == "grandmother" or related_to == "grandfather" or related_to == "grandparent" or related_to == "grandaunt" or related_to == "granduncle" or related_to == "grandaunt/granduncle":
                if gender == "Male":
                    relation_out = "great-grandfather"
                elif gender == "Female":
                    relation_out = "great-grandmother"
                elif gender == "Other":
                    relation_out = "great-grandparent"
            elif related_to == "cousin":
                if gender == "Male":
                    relation_out = "uncle"
                elif gender == "Female":
                    relation_out = "aunt"
                elif gender == "Other":
                    relation_out = "aunt/uncle"
               
        elif rln == "child":
            if related_to == "self":
                if gender == "Male":
                    relation_out = "son"
                elif gender == "Female":
                    relation_out = "daughter"
                elif gender == "Other":
                    relation_out = "child"
            elif related_to == "brother" or related_to == "sister" or related_to == "sibling" or related_to == "cousin":
                if gender == "Male":
                    relation_out = "nephew"
                elif gender == "Female":
                    relation_out = "niece"
                elif gender == "Other":
                    relation_out = "niece/nephew"
            elif related_to == "parent" or related_to == "mother" or related_to == "father":
                if gender == "Male":
                    relation_out = "brother"
                elif gender == "Female":
                    relation_out = "sister"
                elif gender == "Other":
                    relation_out = "sibling"
            elif related_to == "aunt" or related_to == "uncle" or related_to == "aunt/uncle":
                relation_out = "cousin"
            elif related_to == "grandmother" or related_to == "grandfather" or related_to == "grandparent" or related_to == "grandaunt" or related_to == "granduncle":
                if gender == "Male":
                    relation_out = "uncle"
                elif gender == "Female":
                    relation_out = "aunt"
                elif gender == "Other":
                    relation_out = "aunt/uncle"
            elif related_to == "great-grandmother" or related_to == "great-grandfather" or related_to == "great-grandparent":
                if gender == "Male":
                    relation_out = "granduncle"
                elif gender == "Female":
                    relation_out = "grandaunt"
                elif gender == "Other":
                    relation_out = "grandaunt/granduncle"            

        elif rln == "sibling":
            if related_to == "self":
                if gender == "Male":
                    relation_out = "brother"
                elif gender == "Female":
                    relation_out = "sister"
                elif gender == "Other":
                    relation_out = "sibling"
            elif related_to == "brother" or related_to == "sister" or related_to == "sibling":
                if gender == "Male":
                    relation_out = "brother"
                elif gender == "Female":
                    relation_out = "sister"
                elif gender == "Other":
                    relation_out = "sibling"
            elif related_to == "cousin":
                relation_out = "cousin"
            elif related_to == "parent" or related_to == "mother" or related_to == "father" or related_to == "aunt" or related_to == "uncle" or related_to == "aunt/uncle":
                if gender == "Male":
                    relation_out = "uncle"
                elif gender == "Female":
                    relation_out = "aunt"
                elif gender == "Other":
                    relation_out = "aunt/uncle"
            elif related_to == "grandmother" or related_to == "grandfather" or related_to == "grandparent" or related_to == "grandaunt" or related_to == "granduncle" or related_to == "grandaunt/granduncle":
                if gender == "Male":
                    relation_out = "granduncle"
                elif gender == "Female":
                    relation_out = "grandaunt"
                elif gender == "Other":
                    relation_out = "grandaunt/granduncle"
            elif related_to == "niece" or related_to == "nephew" or related_to == "niece/nephew":
                if gender == "Male":
                    relation_out = "nephew"
                elif gender == "Female":
                    relation_out = "niece"
                elif gender == "Other":
                    relation_out = "niece/nephew"
                
        else:
            if related_to == "self":
                if gender == "Male":
                    relation_out = "husband"
                elif gender == "Female":
                    relation_out = "wife"
                elif gender == "Other":
                    relation_out = "partner"
            elif related_to == "brother" or related_to == "sister" or related_to == "sibling":
                if gender == "Male":
                    relation_out = "brother-in-law"
                elif gender == "Female":
                    relation_out = "sister-in-law"
                elif gender == "Other":
                    relation_out = "sibling-in-law"
            elif related_to == "cousin":
                relation_out = "cousin-in-law"
            elif related_to == "parent" or related_to == "mother" or related_to == "father":
                if gender == "Male":
                    relation_out = "father"
                elif gender == "Female":
                    relation_out = "mother"
                elif gender == "Other":
                    relation_out = "parent"
            elif related_to == "aunt" or related_to == "uncle" or related_to == "aunt/uncle":
                if gender == "Male":
                    relation_out = "uncle"
                elif gender == "Female":
                    relation_out = "aunt"
                elif gender == "Other":
                    relation_out = "aunt/uncle"               
            elif related_to == "grandmother" or related_to == "grandfather" or related_to == "grandparent":
                if gender == "Male":
                    relation_out = "grandfather"
                elif gender == "Female":
                    relation_out = "grandmother"
                elif gender == "Other":
                    relation_out = "grandparent"
            elif related_to == "grandaunt" or related_to == "granduncle" or related_to == "grandaunt/granduncle":
                if gender == "Male":
                    relation_out = "granduncle"
                elif gender == "Female":
                    relation_out = "grandaunt"
                elif gender == "Other":
                    relation_out = "grandaunt/granduncle"
            elif related_to == "niece" or related_to == "nephew" or related_to == "niece/nephew":
                if gender == "Male":
                    relation_out = "nephew-in-law"
                elif gender == "Female":
                    relation_out = "niece-in-law"
                elif gender == "Other":
                    relation_out = "niece-in-law/nephew-in-law"    
        if relation_out == "":
            relation_out = "unknown"     
            
        new_relation = None
        try:
            new_relation = RelationsModel.valid_construction(user_id, first, last, death_year, is_deceased, gender, relation_out, notes, is_step, is_adopted, birth_date, lives_in, nickname)
            new_relation.save_to_db()
        except:
            if not new_relation:
                return "ill-formed request", 400, None
            # cls.logger.exception("Error in creating new user")
            return "Internal Server Error.", 500, None
        return "", 201, new_relation.id

    @classmethod
    def get_relations(cls, user_id):

        try:
            relations = RelationsModel.find_by_user_id(user_id)
            if relations == []:
                return "No relations found for the given user id", 400, None
            return "", 200, relations
        except:
            return "Error retrieving relations for user id",500, None