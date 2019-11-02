dict_checks = dict()

dict_checks["This check is for numbers being greater than 6"] = {
    "columns": ["a_number", "number_2"],
    "calc_condition": lambda df, col, **kwargs: df[col] <= 6,
    "long_description": lambda df, col, condition, **kwargs:
        "There are numbers less than or equal to 0"
}
