from transformers import pipeline


def load_model():
    # Загружаем предобученную модель для задач вопросов-ответов
    model = pipeline("question-answering")
    return model


def generate_answer(model, context, question):
    result = model(question=question, context=context)
    return result['answer']
