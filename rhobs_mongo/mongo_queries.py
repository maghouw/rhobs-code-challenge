def get_number_of_genders(collection):
    """
        This function returns a list of dictionaries representing the number of individuals in the collection for each gender.

        Args:
        collection (pymongo.collection.Collection): The collection for which the gender count should be obtained.

        Returns:
        list: A list of dictionaries with two keys:
            - _id (str): The gender.
            - sex (int): The number of individuals with that gender.
    """
    return list(collection.aggregate([{"$group": {"_id": "$sex", "sex": {"$sum": 1}}}]))


def get_companies_with_more_than_n_employees(collection, num):
    """
        This function returns a list of dictionaries representing the companies in the collection with more than a specified number of employees.

        Args:
        collection (pymongo.collection.Collection): The collection for which the companies should be obtained.
        num (int): The minimum number of employees a company must have to be included in the list.

        Returns:
        list: A list of dictionaries with two keys:
            - _id (str): The company name.
            - num_employee (int): The number of employees in that company.
    """
    return list(
        collection.aggregate(
            [
                {"$group": {"_id": "$company", "num_employee": {"$sum": 1}}},
                {"$match": {"num_employee": {"$gt": num}}},
            ]
        )
    )


def get_job_age_pyramid(collection, job):
    """
    This function returns a pyramid representation of the ages of individuals in the collection with the specified job.

    Args:
    collection (pymongo.collection.Collection): The collection from which the pyramid should be built.
    job (str): The job title for which the pyramid should be built.

    Returns:
    list: A list of dictionaries where each dictionary has two keys:
        - _id (dict): A dictionary with one key "age" representing the age group.
        - pyramide (list): A list of dictionaries with two keys:
            - sex (str): The gender.
            - count (int): The number of individuals in that age group with that gender.
    """
    return list(
        collection.aggregate(
            [
                {"$match": {"job": job}},
                {
                    "$project": {
                        "job": 1,
                        "sex": 1,
                        "age": {
                            "$dateDiff": {
                                "startDate": {
                                    "$dateFromString": {"dateString": "$birthdate"}
                                },
                                "endDate": "$$NOW",
                                "unit": "year",
                            }
                        },
                    }
                },
                {
                    "$group": {
                        "_id": {"sex": "$sex", "age": "$age"},
                        "count_age": {"$sum": 1},
                    }
                },
                {
                    "$group": {
                        "_id": {"age": "$_id.age"},
                        "pyramide": {
                            "$push": {"sex": "$_id.sex", "count": "$count_age"}
                        },
                    }
                },
            ]
        )
    )
