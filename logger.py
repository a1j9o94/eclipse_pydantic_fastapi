import logging

#log to file and stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='game.log', filemode='w', encoding='utf-8')