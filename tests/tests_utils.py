def check_message(context, expected_message: str) -> bool:
    return expected_message in str(context.exception)
