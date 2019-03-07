from models.relations import RelationsModel
from models.user import UserModel


class RelationsController():
    @classmethod
    def make_relation(cls, user_id, name, birth_year, is_deceased, gender, relation, notes, is_step, is_adopted):
        # if not UserModel.find_by_id(user_id):
        #     return "User with that id does not exist", 400, None
        try:
            new_relation = RelationsModel(user_id, name, birth_year, is_deceased, gender, relation, notes, is_step, is_adopted)
            new_relation.save_to_db()
        except:
            # cls.logger.exception("Error in creating new user")
            return "Internal Server Error.", 500, None
        return "", 201, None

    @classmethod
    def get_relations(cls, user_id):

        try:
            relations = RelationsModel.find_by_user_id(user_id)
            if relations is None:
                return "No relations found for the given user id", 400, None
            return "", 200, relations
        except:
            return "Error retrieving relations for user id",500, None