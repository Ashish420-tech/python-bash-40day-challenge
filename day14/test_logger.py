from logger import Logger

log = Logger()

log.create_file("server.log")

log.log_message("server.log", "Server Started")
log.log_message("server.log", "Database Connected")
log.log_message("server.log", "User Login Successful")

log.read_file("server.log")
