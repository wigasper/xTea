def validate_execution_spec(execution_spec: str):
    if execution_spec not in ["cluster", "serial", "parallel"]:
        raise ValueError(
            f"Invalid execution specification: {execution_spec}. Must be one of 'cluster', 'serial', or 'parallel'"
        )
