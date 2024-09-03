from flask import Flask, request, render_template, jsonify
from utils.file_handler import extract_text
from my_models.model import load_model, generate_answer
import logging
import os

# Настройка логирования
logging.basicConfig(
    filename='app.log',  # Имя файла для логов
    level=logging.DEBUG,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)

app = Flask(__name__)

# Загружаем модель NLP
model = load_model()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        logging.debug("Received POST request")
        try:
            # Проверяем, что файл и вопрос присутствуют в запросе
            if 'file' not in request.files:
                logging.error("File not provided in the request")
                return render_template('templates/index.html', error="File not provided"), 400
            if 'question' not in request.form:
                logging.error("Question not provided in the request")
                return render_template('templates/index.html', error="Question not provided"), 400

            file = request.files['file']
            question = request.form['question']
            logging.info(f"File received: {file.filename}")
            logging.info(f"Question received: {question}")

            if file.filename == '':
                logging.warning("No file selected")
                return render_template('templates/index.html', error="No file selected"), 400

            # Сохранение файла и извлечение текста
            file_path = f"data/{file.filename}"
            file.save(file_path)
            logging.info(f"File saved to: {file_path}")

            text = extract_text(file_path)
            logging.debug(f"Extracted text: {text[:100]}...")  # Печать первых 100 символов текста

            answer = generate_answer(model, text, question)
            logging.info(f"Generated answer: {answer}")

            return render_template('templates/index.html', answer=answer)

        except Exception as e:
            logging.error(f"Error occurred: {e}", exc_info=True)
            return render_template('templates/index.html', error=str(e))

    return render_template('templates/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
