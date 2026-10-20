import uuid


def unique_user():
    suffix = uuid.uuid4().hex[:10]
    return {
        "name": f"autotest-{suffix}",
        "email": f"autotest-{suffix}@example.com",
        "password": f"Password_{suffix}9",
    }
