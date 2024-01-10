from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route('/', methods=["GET"])
def get_translation():
    list_languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"
    return render_template(
        "index.html",
        languages=list_languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@translate_controller.route('/', methods=["POST"])
def post_translation():
    body = request.form
    list_languages = LanguageModel.list_dicts()
    t_from = body["translate-from"]
    t_to = body["translate-to"]
    text = body["text-to-translate"]
    translated = GoogleTranslator(source=t_from, target=t_to).translate(text)
    return render_template(
        "index.html",
        languages=list_languages,
        text_to_translate=text,
        translate_from=t_from,
        translate_to=t_to,
        translated=translated
    )


@translate_controller.route('/reverse', methods=["POST"])
def reverse_translation():
    body = request.form
    list_languages = LanguageModel.list_dicts()
    t_from = body["translate-from"]
    t_to = body["translate-to"]
    text = body["text-to-translate"]
    translated = GoogleTranslator(source=t_from, target=t_to).translate(text)
    return render_template(
        "index.html",
        languages=list_languages,
        text_to_translate=translated,
        translate_from=t_to,
        translate_to=t_from,
        translated=text
    )