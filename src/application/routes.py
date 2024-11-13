import logging
import sys

from flask import Flask, request

from workers import get_response_for_post_balances

logger = logging.getLogger("HomeworkMockFlask")
logger.setLevel(logging.INFO)
logging.basicConfig(
    format="%(asctime)s - %(name)s - "
           "%(funcName)s - %(levelname)s - %(message)s",
    level=logging.INFO, stream=sys.stdout
)

app = Flask(__name__)

@app.route("/info/postBalances", methods=["POST"])
def post_balances():
    data = request.json
    logger.info(f"Получены данные: {data}")
    response = get_response_for_post_balances(data)
    logger.info(f"Отправлены данные: {response}")
    return response