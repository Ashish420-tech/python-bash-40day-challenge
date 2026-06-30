import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
logging.warning("Memory Usage High")
logging.error("Something Went Wrong")
