TORTOISE_ORM = {
    "connections": {
        "default": "mysql://root:z213146!@localhost:3306/hospital2?charset=utf8mb4"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}