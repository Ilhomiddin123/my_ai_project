# test_model.py

from transformers import pipeline

# Инициализация пайплайна для обработки текста
qa_pipeline = pipeline("question-answering")

# Пример использования модели
context = "OpenAI создала GPT-4, которая является мощной языковой моделью."
question = "Кто создал GPT-4?"

result = qa_pipeline(question=question, context=context)

print("Ответ:", result['answer'])
