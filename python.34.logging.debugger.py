import logging
print("logging and debugger")

print("""logging level's are
1. NOTSET
2. DEBUG
3. INFO
4. WARNING
5. ERROR
6. CRITICAL
""")

print("by default logging level are warning")
logging.basicConfig(filename="test1.log", filemode="w", level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

print("another method by creating object")

# Creating an object
logger = logging.getLogger()

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

for i in range(2):
    print(i)
    logger.info(i)
    logging.info("in this level valve of i is :" + str(i))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, [10, 11, 12, 13, 14, 15], "string"]
l1, l2 = [], []
for i in l:
    logging.info("we are iterating through our list and our local var is i {}".format(l))
    if type(i) == list:
        logging.info("check list type")
        for j in i:
            logging.info("in another for loop for list inside list element{}".format(i))
            if type(j) == int:
                logging.info("inside if statement" + str(j))
                l1.append(j)
    elif type(i) == int:
        l1.append(i)
    else:
        if type(i) == str:
            l2.append(i)
logging.info("{l1} {l2}".format(l1 = l1, l2 = l2))

